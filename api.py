from fastapi import FastAPI, UploadFile, File
import shutil
import os

from src.compressor import FileCompressor

app = FastAPI(
    title="Dynamic File Compression API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Dynamic File Compression Utility API"
    }


@app.post("/compress")
async def compress_file(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    input_path = f"uploads/{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = (
        f"compressed_files/"
        f"{file.filename}.huff"
    )

    compressor = FileCompressor()

    result = compressor.compress_file(
        input_path,
        output_path
    )

    return {
        "status": "success",
        "original_size": result["original_size"],
        "compressed_size": result["compressed_size"],
        "compression_ratio":
            result["compression_ratio"]
    }

from src.benchmark import benchmark


@app.post("/benchmark")
async def benchmark_file(
        file: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return benchmark(path)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)