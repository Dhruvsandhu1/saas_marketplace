import streamlit as st
import re
from PIL import Image
import requests
from bs4 import BeautifulSoup
# Set page title and icon
import streamlit as st
st.set_page_config(page_title="SaaS Marketplace", page_icon=":chart_with_upwards_trend:", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Choose your page:")
page = st.sidebar.selectbox("", ["Home", "About", "Contact"])

# Main header
# st.title("SaaS Marketplace")
# st.subheader("We provide information about the latest software that are in the industry and helps you meet your software requirements")

def remove_html_tags(text):
    """
    Converts basic HTML tags to Markdown-style formatting in Streamlit.
    Handles <p>, <ul>, <li>, <strong>, and other basic HTML tags.
    """
    # Handle <li> by replacing with bullet points
    text = re.sub(r'<li>(.*?)</li>', r'\n• \1', text)

    # Handle <ul> by adding spacing before and after unordered list
    text = re.sub(r'<ul>', r'\n', text)
    text = re.sub(r'</ul>', r'\n', text)

    # Handle empty <p></p> by just adding two newlines
    text = re.sub(r'<p></p>', r'__________________________', text)

    # Handle <p> by adding two newlines (to simulate paragraph spacing)
    text = re.sub(r'<p>(.*?)</p>', r'\n\n\1\n\n', text)

    # Handle <strong> for bold text (Streamlit uses Markdown: **bold**)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)

    # Handle HTML entities
    text = re.sub(r'&amp;', '&', text)  # Convert &amp; to &

    # Remove any other remaining HTML tags (optional, as needed)
    text = re.sub(r'<.*?>', '', text)

    # Clean up any excess newlines
    text = re.sub(r'\n+', '\n\n', text)  # Collapse multiple newlines into two

    # Return the formatted text
    return text.strip()



# def remove_html_tags(text):
#     """
#     Remove or format specific HTML tags from the given content.
#     Handles <p>, <ul>, <li>, <strong>, and other basic HTML tags.
#     """
#     soup = BeautifulSoup(text, "html.parser")

#     # Handle <li> elements by adding bullet points
#     for li in soup.find_all("li"):
#         li.insert_before("<br>• ")
#         li.insert_after("<br>")

#     # Handle <ul> by adding newlines before and after the unordered list
#     for ul in soup.find_all("ul"):
#         ul.insert_before("<br>")  # Optional: You can choose to add before if needed
#         ul.insert_after("<br>")

#     # Handle <p> by collecting text and adding <br> tags
#     new_paragraphs = []
#     for p in soup.find_all("p"):
#         paragraph_text = p.get_text().strip()  # Strip whitespace
#         if paragraph_text:  # Only add non-empty paragraphs
#             new_paragraphs.append(f"<br><br>{paragraph_text}<br><br>")  # Collect text with <br>

#     # Replace <p> elements with the collected text
#     for p in soup.find_all("p"):
#         if p.get_text().strip():  # Replace only non-empty <p> tags
#             p.replace_with(BeautifulSoup(new_paragraphs.pop(0), "html.parser"))

#     # Handle <strong> tags for bold text using markdown (i.e., **bold**)
#     for strong in soup.find_all("strong"):
#         strong.replace_with(f"*****{strong.get_text()}*****")

#     # Remove other HTML tags and return plain text
#     return soup.get_text(separator="").strip()  # Remove separator to avoid new lines




# Home Page
if page == "Home":
    # st.write("## Home Page Content")
    # st.write("This is where the main content for your homepage would go. You can add charts, text, images, and more.")
    
    # Example: Image
    # image = Image.open("saas marketplace.jpg")
    # st.image(image,width=400)
    st.markdown(
    """
    <style>
    .jazzee-title {
                    display: inline;
                    background: linear-gradient(93.59deg, orange 3.13%, #f6be58 85.77%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 1em;
                    font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

    # Example of using the custom class in an HTML element
    st.markdown('<h1><span class="jazzee-title">Jazzee</span> Assist</h1>', unsafe_allow_html=True)
    software_name = st.text_input("Software Name", placeholder="Enter software name here...")
    if software_name:
        def search_software_nachonacho(api_key, software_name, page=1):
        # API endpoint with the given page number
            api_url = f"https://public-api.nachonacho.com/products/{page}"

            # The search query parameter
            params = {
                'search': software_name
            }

            # Headers for the API key (assuming it's passed in the headers)
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }

            # Send a GET request to NachoNacho API
            response = requests.get(api_url, params=params, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                results = response.json()
                # st.write(results)
                # Check if there are results in the response
                if "products" in results and results["products"]:
                    for software in results["products"]:
                        name = software.get("name", "N/A")
                        description = software.get("shortDescription", "No description available")
                        if description=="":
                            description="No description available."
                        long_description= software.get("productDescription", "No description available")
                        if long_description=="":
                            long_description="No description available."
                        benefits = software.get("keyBenefits", "N/A")
                        if benefits=="":
                            benefits="No information about benefits is available."
                        pricing = software.get("pricing", "No pricing information available")
                        if pricing=="":
                            pricing='No pricing information available.'
                        features = software.get("features", "No description available")
                        if features=="":
                            features="No information about features is available."
                        st.markdown(f"***<span style='font-size: 30px;'>{remove_html_tags(name)}</span>*** ", unsafe_allow_html=True)
                        # st.write("\n")
                        st.markdown(f"***<span style='font-size: 18px;'>{remove_html_tags((description))}</span>*** ", unsafe_allow_html=True)
                        # st.markdown(f"***<span style='font-size: 24px;'>Pricing : </span>*** {remove_html_tags(pricing)}", unsafe_allow_html=True)
                        st.write("\n")
                        st.markdown(f"***<span style='font-size: 24px;'>Benefits : </span>***", unsafe_allow_html=True)
                        st.markdown(remove_html_tags(benefits))
                        st.write("\n")
                        st.markdown(f"***<span style='font-size: 24px;'>Description : </span>*** {remove_html_tags(long_description)}", unsafe_allow_html=True)
                        st.write("\n")
                        st.markdown(f"***<span style='font-size: 24px;'>Features : </span>*** ", unsafe_allow_html=True)
                        st.markdown(remove_html_tags(features))
                        # st.markdown(features)
                        # st.markdown(remove_html_tags(features))
                        st.markdown("-" * 40)

                else:
                    st.write("No results found.")
            else:
                st.write(f"Failed to fetch data. Status code: {response.status_code}")

        # Example usage
        api_key = "NN_cm1xrqiq100000ami1pcq20j3_Qn52ZWLOj7UcSVj48R75JlASr"
        search_software_nachonacho(api_key, software_name, page=1)

    
# About Page
elif page == "About":
    st.write("""
            About Us
             

Welcome to Jazzee, where we believe that choosing the right product should be simple, personalized, and empowering.

At Jazzee, our mission is to help customers make informed decisions, cutting through the noise of the marketplace to find the perfect software solutions that truly meet their needs. Whether you're a small business owner looking for efficiency tools, a developer seeking cutting-edge solutions, or an enterprise evaluating the best SaaS options, we’re here to guide you every step of the way.

Our Vision
We’re not just a platform—we’re a disruptor in the SaaS marketplace. In an industry flooded with overwhelming choices, our goal is to revolutionize how software is discovered and purchased. By combining smart technology with a deep understanding of the marketplace, we’re reshaping the customer experience to be intuitive, transparent, and tailored to individual needs.

Our vision is simple:

Empower customers to make the right choice, every time.
Disrupt traditional marketplaces by offering an experience built on trust, transparency, and efficiency.
Foster growth by ensuring customers have access to the best tools that drive their success.
At Jazzee, we strive to make software selection seamless and stress-free, while pushing the boundaries of what a marketplace can do. We believe in forging strong partnerships with SaaS providers and our customers, ensuring that together, we shape the future of business technology.

Join us on this journey to transform the way you choose, use, and experience software.
             """)
    
# Contact Page
elif page == "Contact":
    st.write("## Contact Us")
    st.write("Feel free to reach out to us via the form below.")
    st.text_input("Name")
    st.text_area("Message")
    st.button("Submit")
