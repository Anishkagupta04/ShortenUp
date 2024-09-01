
import streamlit as st

st.set_page_config(
    page_title="ShortenUp",
    page_icon="🔗",
    layout="wide"
)

def shorten_url(input_url):
    if input_url:
        # shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(input_url)
        return short_url
    else:
        return None

# Streamlit dashboard
st.title("ShortenUp")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("url.webp", width=250)  # Replace with your image path

with col2:
    input_url = st.text_input("Enter URL to be shortened")
    button = st.button("Submit")

if button:
    short_url = shorten_url(input_url)
    if short_url:
        st.success(f"Shortened URL: {short_url}")
        st.write(f"[Click here to access the shortened URL]({short_url})")
    else:
        st.error("Please enter a valid URL.")

# Additional features
st.markdown("---")
st.header("About")
st.write("This URL shortener app provides a convenient way to shorten long URLs.")
st.write("**Features:**")
st.write("- Shortens URLs using the TinyURL service")
st.write("- Provides a user-friendly interface")
st.write("- Displays the shortened URL and a clickable link")
