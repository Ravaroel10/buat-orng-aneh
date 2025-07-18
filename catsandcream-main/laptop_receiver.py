from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import os
from datetime import datetime

app = FastAPI()
SAVE_DIR = "received_images"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    filepath = os.path.join(SAVE_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(contents)

    return JSONResponse(content={"message": f"File saved as {filename}"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run("laptop_receiver:app", host="0.0.0.0", port=9000)
