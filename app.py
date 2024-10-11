from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# تحميل النموذج المحفوظ
model = pickle.load(open('best_house_price_model.pkl', 'rb'))

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # الحصول على البيانات المدخلة من المستخدم وتحويلها بالشكل المطلوب
    carpet_area = int(request.form['carpet_area'])
    bathroom = int(request.form['bathroom'])
    balcony = int(request.form['balcony'])
    furnishing = int(request.form['furnishing'])
    floor = int(request.form['floor'])
    facing = int(request.form['facing'])

    # تحويل المدخلات إلى تنسيق numpy array
    features = np.array([[carpet_area, bathroom, balcony, furnishing, floor, facing]])
    
    # عمل التنبؤ باستخدام النموذج
    prediction = model.predict(features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Predicted House Price: {output} rupees')

if _name_ == "_main_":
    app.run(debug=True)
