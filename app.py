import pandas as pd
import streamlit as st
import pickle


def reco(bookname):
    index = books.index
    cond = books['Book_Title'] == bookname
    index = index[cond][0]

    similarity_score = list(enumerate(similarity[index]))
    sorted_sim = sorted(similarity_score, key=lambda x: x[1], reverse=True)[:6]
    rrr = []
    link = []
    for book in sorted_sim:
        index = book[0]
        a = books.iloc[index][0]
        b = books.iloc[index][2]
        rrr.append(a)
        link.append(b)

    return rrr, link

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


books_list = pickle.load(open('books.pkl', 'rb'))
books = pd.DataFrame(books_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Books Recommender")

selected_book = st.selectbox('Select a Book:', books['Book_Title'].values)

if st.button('Recommend'):
    st.write('Your Selected Book:')
    recco0 = reco(selected_book)[0]
    recco1 = reco(selected_book)[1]
    st.write(recco0[0])
    st.image(recco1[0])
    st.write('Recommended for you:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(recco0[1])
        st.image(recco1[1])
    with col2:
        st.write(recco0[2])
        st.image(recco1[2])
    with col3:
        st.write(recco0[3])
        st.image(recco1[3])
    with col4:
        st.write(recco0[4])
        st.image(recco1[4])
    with col5:
        st.write(recco0[5])
        st.image(recco1[5])
