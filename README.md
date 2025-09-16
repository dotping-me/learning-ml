# Sentiment Analysis on News articles
The aim of this project is to learn the basics of machine learning and to learn how to integrate AI/ML into applications.

## 📚 Resources
I used the following resources to learn about AI/ML implementation:
- [Logistic Regression (and why it's different from Linear Regression)](https://www.youtube.com/watch?v=3bvM3NyMiE0)
- [House Price Prediction in Python - Full Machine Learning Project](https://www.youtube.com/watch?v=Wqmtf9SA_kk)

## ⚙ Prerequisites
- Python 3.11.3 or higher  
[Install Python Here!](https://www.python.org/downloads/)

## 💻 Setup & Usage
Follow these steps to get your development environment set up and operational:  
1. **Clone the Repository**
    ```bash
    git clone https://github.com/dotping-me/learning-ml.git
    cd learning-ml
    ```
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Generate database using utility script**
    ```bash
    python ./utils/dataset_builder.py
    ```

4. **Manually go through genetated dataset `./data/news.csv` and label data**
    - Sample example of `news.csv` with manually included column `label`:
    ```csv
    content,label
    Lorem ipsum dolor,neutral
    ...,...
    ```
5. **Train and Export Model using Jupyter Notebook**

6. **Run API App**
    ```bash
    uvicorn app.main:app --reload
    ```

7. **Test Routes using Postman or Curl**
   - `curl` Example:
   ```bash
   curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"text\": \"Hello World!\"}"
   ``` 

***Note to Self:** `__file__` doesn't work in `.ipynb` files!*