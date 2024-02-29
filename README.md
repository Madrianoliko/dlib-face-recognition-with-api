# dlib-face-recognition-with-api
Face recognition python app with API.

<code> docker build -t face_recognition:1.0 . </code>
<br>
<code>docker run -p 8000:8000 face_recognition:1.0</code>

swagger will be at:
localhost:8000/docs

If you want to add more people to be recognized than Donald Trump and Barack Obama, you need to add more directories in train_dir before building docker. The directory name will be the label of the recognized face.

Example:<br>
![signal-2024-02-21-224324_002](https://github.com/Madrianoliko/dlib-face-recognition-with-api/assets/51478114/11e6a838-5380-4a35-af96-4b96344ce5ad)
