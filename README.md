# image-classifier-http-server
Deploy an http server for easy image classification

This an http server that serves a Keras model (VGG) for image classification. Spawn it either with python
`python index.py` or as a docker image.

You can test it with the following command.
`curl  -F "file=@mug.jpg" http://localhost:5000/api/predict`
