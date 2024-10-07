import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
# Set page title and icon
st.set_page_config(page_title="Saas Marketplace", page_icon=":chart_with_upwards_trend:", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Choose your page:")
page = st.sidebar.selectbox("", ["Home", "About", "Contact"])

# Main header
st.title("Saas Marketplace")
st.subheader("We provide information about the latest software that are in the industry and helps you meet your software requirements")

def remove_html_tags(html):
        """
        Remove all HTML tags from the given content.
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text(separator="\n").strip()

# Background image or theme (Optional)
def background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://stock.adobe.com/search?k=sunset');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call function for background image
background_image()

# Home Page
if page == "Home":
    # st.write("## Home Page Content")
    # st.write("This is where the main content for your homepage would go. You can add charts, text, images, and more.")
    
    # Example: Image
    image = Image.open("saas marketplace.jpg")
    st.image(image,width=400)

    # # Example: Columns for layout
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.write("Column 1 content")
    # with col2:
    #     st.write("Column 2 content")
    # with col3:
    #     st.write("Column 3 content")
    
    # # Example: Expander for additional information
    # with st.expander("See More"):
    #     st.write("Here's more detailed information on the homepage.")
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

                # Check if there are results in the response
                if "products" in results and results["products"]:
                    for software in results["products"]:
                        name = software.get("name", "N/A")
                        description = software.get("shortDescription", "No description available")
                        long_description= software.get("productDescription", "No description available")
                        benefits = software.get("keyBenefits", "N/A")
                        pricing = software.get("pricing", "No pricing information available")
                        if pricing=="":
                            pricing='No pricing information is available to us'
                        features = software.get("features", "No description available")
                        lines_ben = [sentence.strip() for sentence in remove_html_tags(benefits).replace(':', '.').split('.') if sentence]
                        lines_fet = [sentence.strip() for sentence in remove_html_tags(features).replace(':', '.').split('.') if sentence]
                        st.markdown(f"***<span style='font-size: 24px;'>Software Name : </span>*** {remove_html_tags(name)}", unsafe_allow_html=True)
                        st.markdown(f"***<span style='font-size: 24px;'>Short Description : </span>*** {remove_html_tags(description)}", unsafe_allow_html=True)
                        st.markdown(f"***<span style='font-size: 24px;'>Pricing : </span>*** {remove_html_tags(pricing)}", unsafe_allow_html=True)
                        st.markdown(f"***<span style='font-size: 24px;'>Benefits : </span>***", unsafe_allow_html=True)
                        for line in lines_ben:
                            st.write(f"-  {line}")
                        st.markdown(f"***<span style='font-size: 24px;'>Long Description : </span>*** {remove_html_tags(long_description)}", unsafe_allow_html=True)
                        st.markdown(f"***<span style='font-size: 24px;'>Features : </span>*** ", unsafe_allow_html=True)
                        for line in lines_fet:
                            st.write(f"-  {line}")
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