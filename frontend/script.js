const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const frame = document.getElementById('frame');
const snapBtn = document.getElementById('snap');
const downloadBtn = document.getElementById('download');
const retakeBtn = document.getElementById('retake');

// Start video stream
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.error("Error accessing webcam:", err);
  });

// Capture photo
snapBtn.addEventListener('click', () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Mirror the image horizontally
  ctx.save();
  ctx.translate(canvas.width, 0);
  ctx.scale(-1, 1);
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  ctx.restore();

  const frameImg = new Image();
  frameImg.crossOrigin = "anonymous";
  frameImg.onload = () => {
    // Kirim ke server
const imageData = canvas.toDataURL('image/png');

fetch('http://10.5.60.16:8000/upload', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ image: imageData })
})
.then(response => response.json())
.then(data => {
  console.log('Upload success:', data);
})
.catch(error => {
  console.error('Upload failed:', error);
});
    ctx.drawImage(frameImg, 0, 0, canvas.width, canvas.height);
    canvas.style.display = 'block';
    video.style.display = 'none';
    frame.style.display = 'none';
    snapBtn.style.display = 'none';
    retakeBtn.style.display = 'inline-block';
  };
  frameImg.src = frame.src;
});

// Download photo
downloadBtn.addEventListener('click', () => {
  const link = document.createElement('a');
  link.download = 'bleh_photobooth.png';
  link.href = canvas.toDataURL('image/png');
  link.click();
});

// Retake photo
retakeBtn.addEventListener('click', () => {
  canvas.style.display = 'none';
  video.style.display = 'block';
  snapBtn.style.display = 'inline-block';
  retakeBtn.style.display = 'none';
});
