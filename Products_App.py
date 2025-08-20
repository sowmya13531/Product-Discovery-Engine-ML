import streamlit as st
import pandas as pd
import numpy as np
import pickle

products = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommender(product):
    product_index = products[products['name'] == product].index[0]
    similarity_list = list(enumerate(similarity[product_index]))
    top_10_similar_product = sorted(similarity_list, key=lambda x : x[1], reverse = True)[1:11]

    similarity_product = []
    for idx, similary in top_10_similar_product:
        product_info = {
            'name':products.loc[idx]['name'],
            'image':products.loc[idx]['image'],
        }

        similarity_product.append(product_info)
    return similarity_product

st.title('Product Recommendation Discovery Engine ML')

product_name = st.selectbox('Select a product:', products['name'])

if st.button("Search"):
    search_product = recommender(product_name)
    st.write('Top 10 recommended for -> your ', {product_name} )

    for rec in search_product:
        st.image(rec['image'], width=150)
        st.write(f"***{rec['name']}***")














