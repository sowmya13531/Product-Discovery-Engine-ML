# 🛒 Product Recommendation Discovery Engine 

A **ML NLP based product recommendation system** that suggests the **Top 10 most similar products** to a selected item.  
Built with **Machine Learning (Cosine Similarity)** and deployed using **Streamlit** for an interactive UI.  

## ✨ Features
- 🔍 Search or select a product from the dropdown.  
- 🤖 Get **Top 10 recommended products** instantly.  
- 🖼️ Product **images displayed** for easy visualization.  
- ⚡ Fast & lightweight — powered by **cosine similarity**.  
- 🌐 Worked by using Amazon Sales Dataset 2023.
  
## 📸 Demo
### App Interface
![App Screenshot](demo.png)  
  

## 🚀 Tech Stack
- **Python** 🐍  
- **Pandas, NumPy** → Data processing  
- **Pickle** → Model persistence  
- **Cosine Similarity** → Recommendation engine  
- **Streamlit** → Web application  

## ⚙️ How It Works
1. **Data Preparation**  
   - Collected product dataset (`data.pkl`) with `name`, `image`, and other details.  
   - Computed similarity matrix (`similarity.pkl`) using **cosine similarity**.  

2. **Recommendation Engine**  
   - Takes input product → finds its index → retrieves top 10 most similar items.  

3. **Streamlit UI**  
   - Simple dropdown for selecting product.  
   - Displays product images & names beautifully.  

## 📂 Project Structure

 📦 product-recommendation-engine 
 ┣ 📜 app.py                
   Streamlit app 
 ┣ 📜 data.pkl              
   Product dataset 
 ┣ 📜 similarity.pkl       
   Similarity matrix 
 ┣ 📜 demo.png             
   Screenshot of app
 ┣ 📜 requirements.txt     
   Dependencies 
 ┗ 📜 README.md            
   Project documentation


## ▶️ Run Locally
Clone the project:
```bash
git clone https://github.com/sowmya13531/Product-Discovery-Engine-ML.git
cd Product-Discovery-Engine-ML
```

### Install dependencies:

```pip install -r requirements.txt```

### Run the Streamlit app:

*streamlit run app.py*

## Locally Running (LocalHost)
https://localhost/8501

### 🛠️ Future Improvements

- Add search bar (instead of dropdown).

- Add filters (price, category, brand).

- Add clickable links to product pages.

- Deploy on Streamlit Cloud for global access.

