# Attendance Management System using Face Recognition  

## 📌 Overview  
This project is a **Face Recognition-based Attendance Management System** built with Python, OpenCV, and Streamlit.  
It allows users to register their face data, train a recognition model, and mark attendance automatically in real time.  
Attendance is stored as CSV files and can be viewed through a simple Streamlit dashboard.  

## 🚀 Features  
- Capture and store user face data  
- Train a KNN model for face recognition  
- Real-time attendance marking with webcam  
- Automatic CSV file generation (per day)  
- Streamlit dashboard to view daily attendance  
- Voice feedback when attendance is recorded  

## 🛠️ Tech Stack  
- **Python**  
- **OpenCV** (Face detection with Haarcascade)  
- **scikit-learn** (KNN model for recognition)  
- **Streamlit** (Attendance dashboard)  
- **pickle** (Storing training data)  
- **CSV** (Attendance records)  

## 📂 Project Structure  
```
Attendance-Face-Recognition/
│-- data/                          # Stores face encodings and labels (names.pkl, faces_data.pkl)
│-- Attendance/                    # Stores daily attendance CSV files
│-- haarcascade_frontalface_default.xml  # Haarcascade for face detection
│-- main.py                        # Streamlit dashboard to view attendance
│-- ml.py                          # Recognition and attendance marking script
│-- test.py                        # Face data collection script
│-- requirements.txt               # Project dependencies
│-- README.md                      # Project documentation
```

## ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/attendance-face-recognition.git
   cd attendance-face-recognition
   ```

2. (Optional) Create a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage  

### 1. Collect Face Data  
Run the `test.py` script and enter your name:  
```bash
python test.py
```  
This will capture 10 face samples and save them in `data/`.

### 2. Run Attendance System  
Start the recognition + attendance marking:  
```bash
python ml.py
```  
- Press **O** to mark attendance  
- Press **Q** to quit  

Attendance is saved in `Attendance/Attendance_<date>.csv`.

### 3. View Attendance Dashboard  
Run the Streamlit app:  
```bash
streamlit run main.py
```  
This will open a dashboard in your browser showing attendance records.  

## 📊 Example Output  
- ✅ **Attendance CSV:**  
```
NAME, TIME
John, 10:45-30
Alice, 10:47-12
```
- ✅ **Dashboard:**  
Displays daily attendance in a styled table.  

## 📜 Requirements  
Create a file named `requirements.txt` with:  
```
opencv-python
numpy
pandas
scikit-learn
streamlit
streamlit-autorefresh
pywin32 ; sys_platform == 'win32'
```

## 📊 Future Enhancements  
- Web dashboard with authentication  
- Cloud database integration  
- Mobile app support  

## 🤝 Contributing  
Contributions, issues, and feature requests are welcome!  

## 📜 License  
This project is licensed under the MIT License.  
