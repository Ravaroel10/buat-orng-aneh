from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import base64
import os
from datetime import datetime

app = FastAPI()

# Izinkan akses dari semua origin (biar bisa diakses dari frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_photo(request: Request):
    try:
        data = await request.json()
        image_data = data.get("image")

        if not image_data:
            return {"status": "error", "message": "No image provided."}

        # Pisahkan header base64
        header, encoded = image_data.split(",", 1)
        binary_data = base64.b64decode(encoded)

        # Simpan ke folder
        os.makedirs("photos", exist_ok=True)
        filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join("photos", filename)

        with open(filepath, "wb") as f:
            f.write(binary_data)

        print(f"[✔] Photo saved at: {filepath}")
        return {"status": "success", "filename": filename}
    
    except Exception as e:
        print(f"[✘] Upload failed: {e}")
        return {"status": "error", "message": str(e)}
