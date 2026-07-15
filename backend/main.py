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

# 3. The New Stats Endpoint (Fixes the 404 and the .map() crash)
@app.get("/api/stats")
async def get_stats():
    # Returns an array of data so your React frontend can .map() over it to draw the chart
    return [
        {"name": "Mon", "requests": 4000, "latency": 200},
        {"name": "Tue", "requests": 3000, "latency": 150},
        {"name": "Wed", "requests": 2000, "latency": 400},
        {"name": "Thu", "requests": 2780, "latency": 350},
        {"name": "Fri", "requests": 1890, "latency": 220},
    ]

# 4. Your Automation Endpoint
@app.post("/api/automate")
async def run_automation(request: AutomateRequest):
    # Note: If you had specific Python logic here for your platform,
    # you can paste it back inside this function!
    return {
        "status": "success",
        "message": f"Successfully received task: {request.task}"
    }
