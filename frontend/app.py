# frontend/app.py
"""
AI Automation Platform - Simple HTML Dashboard
"""

from flask import Flask, render_template_string, request, jsonify
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Automation Platform</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
background: #0f172a;
color: #f8fafc;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
min-height: 100vh;
}

header {
background: #1e293b;
border-bottom: 1px solid #334155;
padding: 24px;
display: flex;
justify-content: space-between;
align-items: center;
}

header h1 { font-size: 28px; font-weight: 700; }
header p { color: #60a5fa; font-size: 14px; margin-top: 4px; }

.container { max-width: 1200px; margin: 0 auto; padding: 24px; }

.card {
background: #1e293b;
border: 1px solid #334155;
border-radius: 8px;
padding: 24px;
margin-bottom: 24px;
}

.card h2 { font-size: 24px; margin-bottom: 12px; }
.card p { color: #94a3b8; line-height: 1.6; }

.button-group {
display: flex;
gap: 12px;
margin-top: 16px;
}

button {
padding: 12px 24px;
border-radius: 6px;
border: none;
cursor: pointer;
font-weight: 600;
font-size: 14px;
}

.btn-primary {
background: #3b82f6;
color: white;
}

.btn-primary:hover { background: #2563eb; }

.btn-secondary {
background: #1e293b;
color: #3b82f6;
border: 1px solid #3b82f6;
}

.stats {
display: flex;
gap: 16px;
margin-bottom: 24px;
}

.stat-card {
flex: 1;
background: #1e293b;
border: 1px solid #334155;
border-radius: 8px;
padding: 20px;
text-align: center;
}

.stat-label { font-size: 12px; color: #94a3b8; }
.stat-value { font-size: 32px; color: #3b82f6; margin-top: 8px; font-weight: bold; }

.test-section {
background: #1e293b;
border: 1px solid #334155;
border-radius: 8px;
padding: 24px;
margin-bottom: 24px;
}

textarea {
width: 100%;
height: 80px;
padding: 12px;
border-radius: 6px;
border: 1px solid #334155;
background: #0f172a;
color: #f8fafc;
font-family: monospace;
font-size: 14px;
margin-bottom: 12px;
}

#result {
margin-top: 16px;
padding: 12px;
background: #0f172a;
border-radius: 6px;
border: 1px solid #334155;
min-height: 40px;
color: #f8fafc;
}

.loading { color: #60a5fa; }
.success { color: #10b981; }
.error { color: #ef4444; }
</style>
</head>
<body>
<header>
<div>
<h1>AI Automation Platform</h1>
<p>Enterprise AI Automation Dashboard</p>
</div>
<span style="font-size: 12px; color: #94a3b8;" id="time"></span>
</header>

<div class="container">
<!-- Welcome Card -->
<div class="card">
<h2>Welcome to AI Automation</h2>
<p>Automate your business processes with Claude Sonnet 5. Connect your apps, create workflows, and let AI handle the rest.</p>
<div class="button-group">
<button class="btn-primary">Connect Apps</button>
<button class="btn-secondary">View Automations</button>
</div>
</div>

<!-- Stats -->
<div class="stats">
<div class="stat-card">
<div class="stat-label">Connected Apps</div>
<div class="stat-value">0</div>
</div>
<div class="stat-card">
<div class="stat-label">Active Automations</div>
<div class="stat-value">0</div>
</div>
<div class="stat-card">
<div class="stat-label">Tasks Completed</div>
<div class="stat-value">0</div>
</div>
</div>

<!-- Test Claude -->
<div class="test-section">
<h3 style="margin-bottom: 16px;">Test Claude Sonnet 5 AI</h3>
<textarea id="task" placeholder="Enter a task for AI to automate..."></textarea>
<button class="btn-primary" onclick="runAutomation()">Run Automation</button>
<div id="result"></div>
</div>

<!-- Getting Started -->
<div class="card">
<h3 style="margin-bottom: 16px;">Getting Started</h3>
<ol style="color: #94a3b8; line-height: 1.8; margin-left: 20px;">
<li>Connect your Gmail account</li>
<li>Connect Google Sheets</li>
<li>Create your first automation</li>
<li>Let Claude Sonnet 5 AI handle the rest!</li>
</ol>
</div>
</div>

<script>
// Update time
function updateTime() {
const now = new Date();
document.getElementById('time').textContent = now.toLocaleString();
}
updateTime();
setInterval(updateTime, 60000);

// Run automation
async function runAutomation() {
const task = document.getElementById('task').value;
const resultDiv = document.getElementById('result');

if (!task) {
resultDiv.textContent = 'Please enter a task.';
resultDiv.className = 'error';
return;
}

resultDiv.textContent = 'Running...';
resultDiv.className = 'loading';

try {
const response = await fetch('http://localhost:8000/api/automate', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ task: task, context: 'User request' })
});

const data = await response.json();
resultDiv.textContent = '✅ Result: ' + data.result;
resultDiv.className = 'success';
} catch (error) {
resultDiv.textContent = '❌ Error: ' + error.message;
resultDiv.className = 'error';
}
}
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=8050, host='127.0.0.1')