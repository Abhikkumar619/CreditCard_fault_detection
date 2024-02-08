from flask import Flask, render_template, request, send_file
import os , sys
from src.Credit_card_project.pipeline.predict import PredictPipeline
from src.Credit_card_project.entity.config_entity import PredictConfig
from src.Credit_card_project.config.configuration import PredictConfig
from pathlib import Path



app=Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    return render_template("index.html")

@app.route('/training', methods=['GET'])
def training(): 
    os.system("python main.py")
    
    
@app.route('/predict', methods=['GET','POST'])
def prediction():
    if request.method=='POST': 
        
        prediction_pipe=PredictPipeline(PredictConfig, request)
        prediction_pipe.run_pipeline()
        
        
        # config=PredictConfig()
        
        ## Now for downloading the predicted file. 
        send_file(Path(os.path.join('predication', 'predicted_file.csv')), as_attachment=True)
        
        
    else: 
        return render_template('index.html')
        
        
        


if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)