async function compressFile() {

    const file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(
        "http://127.0.0.1:8000/compress",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Compression Result</h3>

        <p>Original Size: ${data.original_size}</p>

        <p>Compressed Size: ${data.compressed_size}</p>

        <p>Compression Ratio: ${data.compression_ratio}%</p>
    `;
}