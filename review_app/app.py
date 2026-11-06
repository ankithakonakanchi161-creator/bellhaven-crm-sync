from flask import Flask
import json

app = Flask(__name__)

with open("../crm_findings.json", "r", encoding="utf-8") as f:
    findings = json.load(f)

@app.route("/")
def home():

    html = """
    <h1>Bellhaven Review Queue</h1>
    <hr>
    """

    for finding in findings:

        html += "<div style='margin-bottom:20px;'>"

        html += f"<h2>{finding['type']}</h2>"

        for key, value in finding.items():
            html += f"<p><b>{key}</b>: {value}</p>"

        html += """
        <button>Approve</button>
        <button>Reject</button>
        <hr>
        """

        html += "</div>"

    return html

if __name__ == "__main__":
    app.run(debug=True)