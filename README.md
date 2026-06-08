# Dynamic File Compression Utility

A Python-based file compression system that uses Huffman Coding to compress and decompress text files efficiently. The project also includes a FastAPI backend, interactive API documentation, benchmarking against popular compression algorithms, and a simple web frontend.

## Features

- Huffman Coding Compression
- File Decompression
- File Verification
- Compression Ratio Calculation
- Benchmark Comparison
  - Gzip
  - Bzip2
  - LZMA
  - Brotli
  - Zstandard
- FastAPI REST API
- Swagger API Documentation
- HTML/CSS/JavaScript Frontend
- Compression Statistics Display

---

## Project Structure

```text
Dynamic-File-Compression-Utility/
│
├── api.py
├── main.py
├── requirements.txt
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── src/
│   ├── compressor.py
│   ├── decompressor.py
│   ├── huffman.py
│   ├── detector.py
│   ├── strategy.py
│   ├── benchmark.py
│   ├── verify.py
│   └── bit_utils.py
│
├── input_files/
├── compressed_files/
├── decompressed_files/
├── uploads/
└── tests/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Dynamic-File-Compression-Utility.git

cd Dynamic-File-Compression-Utility
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Compress File

```bash
python main.py compress input_files/sample.txt
```

### Decompress File

```bash
python main.py decompress compressed_files/sample.huff
```

### Verify Compression

```bash
python main.py verify
```

### Benchmark Algorithms

```bash
python main.py benchmark input_files/sample.txt
```

---

## API Server

Run FastAPI server:

```bash
uvicorn api:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend

Start frontend server:

```bash
cd frontend

python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

---

## Sample Result

| Metric | Value |
|----------|----------|
| Original Size | 134 bytes |
| Compressed Size | 67 bytes |
| Compression Ratio | 50% |

---

## Technologies Used

- Python
- Huffman Coding
- FastAPI
- HTML
- CSS
- JavaScript
- Uvicorn

---

## Future Improvements

- Drag and Drop Upload
- Download Compressed Files
- Automatic Compression Strategy Selection
- User Authentication
- Compression History
- Cloud Deployment (Render / Railway)
- Docker Support

---

## Author

Bablu Kumar

Computer Science Engineering Student
