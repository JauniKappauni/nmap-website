from flask import Flask, render_template, request
import nmap

app = Flask(__name__)

scanner = nmap.PortScanner()

@app.route("/", methods=["GET", "POST"])
def function1():
    output = ""
    if request.method == "POST":
        target = request.form.get("domain/ip-address")
        scanner.scan(target)
        for host in scanner.all_hosts():
            output += f"Host: {host}\n"
            output += f"State: {scanner[host].state()}\n"
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                output += f"Protocol: {scanner[host][proto].keys()}\n"
                for port in ports:
                    output += f"Port: {port}, State: {scanner[host][proto][port]['state']}\n"
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")