"""
Interactive Web Scientific Calculator
Author: Anees Shaikh
Description: Python Web HTTP Server & Modern Calculator UI.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import math
import webbrowser

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scientific Calculator — Python 3</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }
        body { background: #0f172a; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .calc-card { background: #1e293b; width: 360px; padding: 24px; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
        .header { text-align: center; font-size: 14px; font-weight: 700; color: #38bdf8; letter-spacing: 1px; margin-bottom: 12px; }
        .screen { background: #0f172a; padding: 16px; border-radius: 10px; text-align: right; margin-bottom: 20px; border: 1px solid #334155; }
        .screen-expr { font-size: 13px; color: #64748b; height: 18px; }
        .screen-val { font-size: 28px; font-weight: 700; color: #f8fafc; overflow-x: auto; }
        .btn-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
        button { background: #334155; color: #f8fafc; border: none; padding: 14px; border-radius: 10px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.15s; }
        button:hover { background: #475569; transform: translateY(-1px); }
        button.op { background: #0284c7; color: white; }
        button.op:hover { background: #0369a1; }
        button.clear { background: #dc2626; color: white; }
        button.clear:hover { background: #b91c1c; }
        button.eq { background: #16a34a; color: white; grid-column: span 2; }
        button.eq:hover { background: #15803d; }
    </style>
</head>
<body>
    <div class="calc-card">
        <div class="header">SCIENTIFIC CALCULATOR</div>
        <div class="screen">
            <div class="screen-expr" id="expr"></div>
            <div class="screen-val" id="val">0</div>
        </div>
        <div class="btn-grid">
            <button class="clear" onclick="clearScreen()">C</button>
            <button onclick="press('(')">(</button>
            <button onclick="press(')')">)</button>
            <button class="op" onclick="press('/')">÷</button>

            <button onclick="pressFunc('sin')">sin</button>
            <button onclick="pressFunc('cos')">cos</button>
            <button onclick="pressFunc('log')">log</button>
            <button class="op" onclick="press('*')">×</button>

            <button onclick="press('7')">7</button>
            <button onclick="press('8')">8</button>
            <button onclick="press('9')">9</button>
            <button class="op" onclick="press('-')">-</button>

            <button onclick="press('4')">4</button>
            <button onclick="press('5')">5</button>
            <button onclick="press('6')">6</button>
            <button class="op" onclick="press('+')">+</button>

            <button onclick="press('1')">1</button>
            <button onclick="press('2')">2</button>
            <button onclick="press('3')">3</button>
            <button onclick="pressFunc('sqrt')">√</button>

            <button onclick="press('0')">0</button>
            <button onclick="press('.')">.</button>
            <button class="eq" onclick="calculate()">=</button>
        </div>
    </div>

    <script>
        let current = '';

        function press(char) {
            current += char;
            document.getElementById('val').innerText = current;
        }

        function clearScreen() {
            current = '';
            document.getElementById('expr').innerText = '';
            document.getElementById('val').innerText = '0';
        }

        function pressFunc(func) {
            if (!current) return;
            fetch('/api/calc_func', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({func: func, val: parseFloat(current)})
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    document.getElementById('expr').innerText = `${func}(${current})`;
                    current = data.result.toString();
                    document.getElementById('val').innerText = current;
                }
            });
        }

        function calculate() {
            if (!current) return;
            fetch('/api/eval', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({expr: current})
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('val').innerText = 'Error';
                } else {
                    document.getElementById('expr').innerText = current;
                    current = data.result.toString();
                    document.getElementById('val').innerText = current;
                }
            });
        }
    </script>
</body>
</html>
"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(content_length).decode("utf-8"))

        if self.path == "/api/eval":
            expr = body.get("expr", "")
            try:
                res = eval(expr)
                self.send_json({"result": res})
            except ZeroDivisionError:
                self.send_json({"error": "Cannot divide by zero"})
            except Exception:
                self.send_json({"error": "Invalid expression"})

        elif self.path == "/api/calc_func":
            func = body.get("func")
            val = body.get("val", 0)
            try:
                if func == "sin":
                    res = math.sin(math.radians(val))
                elif func == "cos":
                    res = math.cos(math.radians(val))
                elif func == "log":
                    res = math.log10(val)
                elif func == "sqrt":
                    res = math.sqrt(val)
                else:
                    res = val
                self.send_json({"result": round(res, 6)})
            except Exception as e:
                self.send_json({"error": str(e)})

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

def run():
    port = 5001
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    url = f"http://localhost:{port}"
    print(f"✓ Scientific Calculator Web Server running at {url}")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")

if __name__ == "__main__":
    run()
