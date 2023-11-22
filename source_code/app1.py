import os
from ultralytics import YOLO
from flask import Flask , request, render_template,json,jsonify


app = Flask(__name__)

model = YOLO(r"C:\users\aakash\documents\codes\runs\classify\train5\weights\last.pt")
print("Model loaded successfully!")

with open('insect_data_1.json') as json_file:
    data = json.load(json_file)
                 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():

    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)

        print(filepath)
        results=model(filepath)
        prob_list = results[0].probs.data.tolist()
        names_dict=results[0].names


        insect_name = names_dict[prob_list.index(max(prob_list))]

        print(insect_name)
        #text= insect_name

        details,pesticides = get_insect_details(insect_name)

        response_data = {
            'insect_name': insect_name,
            'details': details,
            'pesticides': pesticides
        }
        return jsonify(response_data)
    
    
def get_insect_details(ins):
    for insect in data['insects']:
        if insect['insect_name'].replace(" ", "").lower() == ins.replace(" ", "").lower():
            return insect['details'],insect['pesticides']
    return "Info not available"
      
        
    #return text
if __name__ == '__main__':
    app.run(debug = False, threaded = False)
