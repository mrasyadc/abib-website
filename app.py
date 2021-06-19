from flask import Flask, render_template, request
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.keras.models import model_from_json
import numpy as np

app = Flask(__name__)

target_size  = (128,128)
classes =6

json_file = open('model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('model1.h5')
poro =  loaded_model

json_file = open('turto1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("turto1.h5")
turto =  loaded_model

json_file = open('ssa1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("ssa1.h5")
ssa =  loaded_model

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def machlearn():
    imagefile = request.files['image']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    image = load_img(image_path, target_size=(128,128))
    image = img_to_array(image)
    image = np.reshape(image,[1,128,128,3])
    prediksi = poro.predict(image)
    hasil = np.zeros(classes)
    for i in range(classes):
        hasil[i] = prediksi[0][i]
    if hasil[0] == 1:
        hasil_poro = "1-5 %"
    if hasil[1] == 1:
        hasil_poro = "6-10 %"
    if hasil[2] == 1:
        hasil_poro = "11-15 %"
    if hasil[3] == 1:
        hasil_poro = "16-20 %"
    if hasil[4] == 1:
        hasil_poro = "21-25 %"
    if hasil[5] == 1:
        hasil_poro = "26-30 %"

    prediksi_turto = turto.predict_classes(image)
    hasil_turto = []
    if prediksi_turto == [0]:
        hasil_turto = "Connected"
    elif prediksi_turto == [1]:
        hasil_turto = "Unconnected"

    prediksi_ssa = ssa.predict_classes(image)
    hasil_ssa = []
    if prediksi_ssa == [0]:
        hasil_ssa = "14-30"
    elif prediksi_ssa == [1]:
        hasil_ssa = "31-37"
    elif prediksi_ssa == [2]:
        hasil_ssa = "48-43"
    elif prediksi_ssa == [3]:
        hasil_ssa = "44-51"
    elif prediksi_ssa == [4]:
        hasil_ssa = "51-116"
    
    return render_template('index.html', data1=hasil_poro, data2=hasil_turto, data3=hasil_ssa)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')