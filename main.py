import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os

from patient_face_recognition import train, predict, show_prediction_labels_on_image

app = FastAPI()

# Ścieżka do tymczasowego katalogu, gdzie będziemy przechowywać przesłane pliki
TEMP_DIR = "temp"


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Tworzymy katalog tymczasowy, jeśli nie istnieje
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)

        # Ścieżka, pod którą będzie przechowywane tymczasowo przesłane zdjęcie
        file_location = f"{TEMP_DIR}/{file.filename}"

        # Otwieramy plik w trybie binarnym i zapisujemy do niego dane z przesłanego pliku
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        frame = cv2.imread(file_location)
        img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        test = predict(img, model_path="trained_knn_model.clf")
        # name, (top, right, bottom, left) = predict(img, model_path="trained_knn_model.clf")
        # frame = show_prediction_labels_on_image(frame, predictions)
        # Dodajemy zmienną int do odpowiedzi
        # recognized_patient = name

        return JSONResponse(status_code=200, content={"message": "Upload successful", "name": test[0][0]})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Upload failed: {str(e)}"})

@app.get("/check")
async def check_connection():
    return JSONResponse(status_code=200, content={"message": "connection successful"})


if __name__ == "__main__":
    print("Training KNN classifier...")
    classifier = train("train_dir", model_save_path="trained_knn_model.clf", n_neighbors=2)
    print("Training complete!")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


