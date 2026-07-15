# backend/config.py
"""
Configuration settings for AI Automation Platform
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = "claude-3-5-sonnet-20241022"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ai_automation.db")

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Frontend URL
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8050")

# Google OAuth
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")

# Salesforce OAuth
SALESFORCE_CLIENT_ID = os.getenv("SALESFORCE_CLIENT_ID", "")
SALESFORCE_CLIENT_SECRET = os.getenv("SALESFORCE_CLIENT_SECRET", "")

# Logging
LOG_LEVEL = "INFO"
