# Import library
import streamlit as st

# Title
st.title("Belajar Machine Learning")

# Header
st.header("Welcome Machine Learning")

# Subheader
st.subheader("Bismillahirrahmanirrahim")

# Text
st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

# Markdown
st.markdown("# Markdown1")
st.markdown("## Markdown2")
st.markdown("### Markdown3")
st.markdown("#### Markdown4")

# Markdown warna
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')

# Markdown emoji
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# Markdown multibaris
multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# Code block
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

#LaTex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')









