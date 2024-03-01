import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SUPABASE_URL = os.getenv("SUPABASE_URL", "")
    if not SUPABASE_URL:
        raise ValueError("No SUPABASE_URL set for application")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
    if not SUPABASE_KEY:
        raise ValueError("No SUPABASE_KEY set for application")
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for application")
    SESSION_KEY = "supabase.auth.token"
