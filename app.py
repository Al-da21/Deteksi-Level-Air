from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model YOLOv8 hasil training (ganti dengan path model kamu)
model = YOLO('weights/best.pt')

# Route halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route upload dan deteksi
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(url_for('index'))

    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Prediksi menggunakan YOLO
        results = model.predict(source=filepath, conf=0.4)
        result_img = results[0].plot()  # Gambar dengan bounding box

        # Simpan hasil deteksi
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
        cv2.imwrite(output_path, result_img)

        # Ambil hasil deteksi (label dan confidence)
        detections = []
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])
            detections.append({'label': label, 'confidence': round(conf, 2)})

        return render_template('index.html', uploaded=True, img_path='uploads/result.jpg', detections=detections)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
