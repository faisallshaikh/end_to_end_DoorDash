from flask import Flask ,render_template,request
from src.pipeline.predicting_pipeline import CustomData
from src.pipeline.predicting_pipeline import PredictData


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_val():
    data = CustomData(
    market_id = int(request.form.get('market_id')),
    store_id = int(request.form.get('store_id')),
    order_protocol = int(request.form.get('order_protocol')),
    total_items = request.form.get('total_items'),
    subtotal = request.form.get('subtotal'),
    num_distinct_items = request.form.get('num_distinct_items'),
    total_onshift_dashers = request.form.get('total_onshift_dashers'),
    total_busy_dashers = request.form.get('total_busy_dashers'),
    total_outstanding_orders = request.form.get('total_outstanding_orders'),
    estimated_order_place_duration = request.form.get('estimated_order_place_duration'),
    estimated_store_to_consumer_driving_duration = request.form.get('estimated_store_to_consumer_driving_duration'),
    non_null_primary_category = request.form.get('non_null_primary_category'),
    time = int(request.form.get('time'))

    )

    pred = data.get_data_as_df()
    predict_data = PredictData()
    result = predict_data.Predict(pred)
    print(f"Value predicted : {result}")


    return render_template('index.html', result=result)

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=8080)