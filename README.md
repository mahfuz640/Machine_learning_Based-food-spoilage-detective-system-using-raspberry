# 🍎 Machine Learning Based Food Spoilage Detection System Using Raspberry Pi

## 📌 Overview

The Machine Learning Based Food Spoilage Detection System is an intelligent IoT solution that detects and predicts food spoilage using environmental sensor data and machine learning algorithms. The system utilizes a Raspberry Pi to collect real-time data such as temperature, humidity, and gas concentration, then analyzes the data to determine the freshness status of food products.

This project aims to reduce food waste, improve food safety, and provide an affordable smart monitoring solution for households, restaurants, and food storage facilities.

---

## 🚀 Features

- Real-time food condition monitoring
- Temperature and humidity sensing
- Gas sensor-based spoilage detection
- Machine Learning prediction model
- Raspberry Pi-based processing
- LCD/Web Dashboard display
- Alert notifications for spoiled food
- Data logging and visualization
- Low-cost IoT implementation

---

## 🛠 Hardware Components

| Component | Quantity |
|------------|-----------|
| Raspberry Pi 4 / 3B+ | 1 |
| DHT22 Temperature & Humidity Sensor | 1 |
| MQ-135 Gas Sensor | 1 |
| LCD Display (I2C) | 1 |
| Buzzer | 1 |
| Breadboard | 1 |
| Jumper Wires | Several |
| Power Supply | 1 |

---

## 💻 Software Requirements

- Raspberry Pi OS
- Python 3.x
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Flask (Optional)
- OpenCV (Optional)

Install required libraries:

```bash
pip install numpy pandas scikit-learn matplotlib flask
```

---

## 🧠 Machine Learning Model

The system uses supervised machine learning techniques to classify food conditions into:

- Fresh
- Moderately Fresh
- Spoiled

### Input Parameters

- Temperature (°C)
- Humidity (%)
- Gas Concentration (PPM)

### Algorithms Used

- K-Nearest Neighbors (KNN)
- Random Forest
- Support Vector Machine (SVM)

---

## 📂 Project Structure

```text
Machine_learning_Based-food-spoilage-detective-system-using-raspberrypi/
│
├── dataset/
│   └── food_spoilage_dataset.csv
│
├── model/
│   └── spoilage_model.pkl
│
├── sensors/
│   ├── dht22.py
│   └── mq135.py
│
├── app/
│   ├── main.py
│   ├── predict.py
│   └── dashboard.py
│
├── images/
│   ├── architecture.png
│   └── prototype.jpg
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ System Architecture

1. Sensors collect environmental data.
2. Raspberry Pi processes sensor readings.
3. Data is sent to the machine learning model.
4. The model predicts food freshness status.
5. Results are displayed on the dashboard/LCD.
6. Alerts are triggered if spoilage is detected.

---

## 📊 Dataset

The dataset contains:

| Feature | Description |
|-----------|------------|
| Temperature | Storage temperature |
| Humidity | Relative humidity |
| Gas Level | Ethylene/Ammonia concentration |
| Status | Fresh / Spoiled |

---

## 🔧 Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/Machine_learning_Based-food-spoilage-detective-system-using-raspberrypi.git
```

Navigate to the project:

```bash
cd Machine_learning_Based-food-spoilage-detective-system-using-raspberrypi
```

Run the application:

```bash
python main.py
```

---

## 📈 Future Improvements

- Deep Learning Integration
- Cloud-Based Monitoring
- Mobile Application Support
- Multi-Food Classification
- AI-Based Shelf Life Prediction

---

## 🎯 Applications

- Smart Refrigerators
- Food Warehouses
- Restaurants
- Grocery Stores
- Household Food Storage

---

## 🤝 Contributors

- Md. Mahfuzur Rahman
- Project Team Members

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please give it a star ⭐ on GitHub and contribute to future improvements.
