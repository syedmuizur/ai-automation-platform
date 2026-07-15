from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 1. CORS Security: Allows your Vercel frontend to talk to this backend
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# Request model for your automation endpoint
class AutomateRequest(BaseModel):
	task: str
	# Add any other fields your frontend sends here

# 2. Basic Health Check
@app.get("/")
async def root():
	return {"status": "online", "message": "Backend is live on Vercel!"}

# 3. The UPDATED Stats Endpoint (Perfectly matches your React frontend)
@app.get("/api/stats")
async def get_stats():
	return {
		"performanceData": [
			{"name": "Mon", "requests": 4000, "latency": 240, "errors": 24},
			{"name": "Tue", "requests": 3000, "latency": 139, "errors": 13},
			{"name": "Wed", "requests": 2000, "latency": 980, "errors": 45},
			{"name": "Thu", "requests": 2780, "latency": 390, "errors": 28},
			{"name": "Fri", "requests": 3100, "latency": 210, "errors": 18}
		],
		"modelUsageData": [
			{"name": "Claude 3.5 Sonnet", "value": 75},
			{"name": "Claude 3 Opus", "value": 25}
		],
		"recentActivity": [
			{"id": 1, "task": "Backend Connected!", "status": "success", "time": "Just now", "model": "System"}
		],
		"topWorkflows": [
			{"name": "Lead Generation", "calls": "1.2k", "success": "99%", "trend": "+5%"}
		]
	}

# 4. Your Automation Endpoint
@app.post("/api/automate")
async def run_automation(request: AutomateRequest):
	return {
		"status": "success",
		"message": f"Successfully received task: {request.task}"
	}
