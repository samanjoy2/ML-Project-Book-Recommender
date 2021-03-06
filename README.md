# ML-Project-Book-Recommender

## Basics

This Machine Learning project is a Book Recommendation System.
A working prototype made by Streamlit can be found here: https://mlproject-books-recommender.herokuapp.com/

![Sample GIF](https://i.ibb.co/4j38FJx/ezgif-1-c41863263d.gif)

## Project Description

After a user selects a book of their preference, the system recommends 5 books with their titles and Book Covers that are similar to that selected book.

How the system selects the similar books:
- All the books informations are converted as tags and those tags are then converted into vectors. These vectors help us to find the similar books as only sorting through them gives us the most similar books.
- The .ipynb file has all the information on how it fully works.

The website is deployed using streamlit library which uses the pickled files for data uses.

## Used

Datasets used: https://www.kaggle.com/tanguypledel/science-fiction-books-subgenres

- Python 
- - For Data Manipulation & Tags Making : Pandas, NumPy, nltk, ast
- - For Vectorization: sklearn
- - For converting GoodReads Urls to Books cover Image URLs: BeautifulSoup
- - For data extraction: pickle
- - Implementation: StreamLit, Heroku

## License

ML-Project-Book-Recommender is
- © Saman Sarker Joy 
