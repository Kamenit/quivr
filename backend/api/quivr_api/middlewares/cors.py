from fastapi.middleware.cors import CORSMiddleware


from dotenv import load_dotenv
import os
load_dotenv()




origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "https://quivr.app",
    "https://www.quivr.app",
    "http://quivr.app",
    "http://www.quivr.app",
    "https://chat.quivr.app",
    os.getenv("NEXT_PUBLIC_FRONTEND_URL", ""),
    "*",
]


def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
