import streamlit as st
import re
from PIL import Image
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

def remove_html_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    flag=0
    for element in soup:
        if element.name == 'p':
            st.markdown(element.text.strip())
            flag=1
        elif element.name == 'h3':
            st.markdown(f"**<span style='font-size: 20px;'>{element.text.strip()}</span>**",unsafe_allow_html=True)
            flag=1
        elif element.name == 'ul':
            for li in element.find_all('li'):
                strong_tag = li.find('strong')
                if strong_tag:
                    # Get the strong text and remaining text, strip spaces
                    strong_text = strong_tag.text.strip()
                    remaining_text = li.get_text(separator=' ', strip=True).replace(strong_tag.text, '', 1).strip()
                    st.markdown(f"- **{strong_text}** {remaining_text}")
                    flag=1
                else:
                    st.markdown(f"- {li.get_text(separator=' ', strip=True)}")
                    flag=1
        elif element.name == 'h1':
            st.markdown(f"**<span style='font-size: 30px;'>{element.text.strip()}</span>**",unsafe_allow_html=True)
            flag=1
        elif element.name == 'h2':
            st.markdown(f"**<span style='font-size: 25px;'>{element.text.strip()}</span>**",unsafe_allow_html=True)
            flag=1
    if flag==0:
        st.markdown(html_content)

#jazzee logo style
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
# Home Page
if page == "Home":
    # st.write("## Home Page Content")
    # st.write("This is where the main content for your homepage would go. You can add charts, text, images, and more.")
    
    # Example: Image
    # image = Image.open("saas marketplace.jpg")
    # st.image(image,width=400)
    
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
                        st.markdown(f"**<span style='font-size: 40px;'>{name}</span>** ", unsafe_allow_html=True)
                        # st.write("\n")
                        remove_html_tags((description))
                        # st.markdown(f"***<span style='font-size: 24px;'>Pricing</span>*** {remove_html_tags(pricing)}", unsafe_allow_html=True)
                        st.write("\n")
                        st.markdown(f"**<span style='font-size: 36px;'>Benefits</span>**", unsafe_allow_html=True)
                        remove_html_tags(benefits)
                        st.write("\n")
                        st.markdown(f"**<span style='font-size: 36px;'>Description</span>** ", unsafe_allow_html=True)
                        remove_html_tags(long_description)
                        st.write("\n")
                        st.markdown(f"**<span style='font-size: 36px;'>Features</span>** ", unsafe_allow_html=True)
                        remove_html_tags(features)
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
    st.markdown('<h1>About <span class="jazzee-title">Jazzee</span> Assist</h1>', unsafe_allow_html=True)

    st.write(
    "Welcome to **Jazzee Assist**, your ultimate guide in making informed software choices! Created by **Jazzee**, "
    "Jazzee Assist is designed to simplify your decision-making process by providing detailed and accurate information "
    "about various software solutions available in the marketplace."
)

    # Key Features
    st.subheader("Key Features of Jazzee Assist:")
    features = [
        "Comprehensive software information at your fingertips",
        "Easy comparisons between different tools",
        "User ratings and reviews to guide your decision",
        "Up-to-date pricing and feature details"
    ]

    # Displaying the features in a bullet list
    for feature in features:
        st.write(f"- {feature}")

    # Conclusion
    st.write(
        "No more endless searching—let Jazzee Assist do the heavy lifting for you. Make your software decisions with "
        "confidence and ease!"
    )
    st.title("Our Vision")
    st.markdown('''
Empower customers to make the right choice, every time.
Disrupt traditional marketplaces by offering an experience built on trust, transparency, and efficiency.
Foster growth by ensuring customers have access to the best tools that drive their success.
At Jazzee, we strive to make software selection seamless and stress-free, while pushing the boundaries of what a marketplace can do. We believe in forging strong partnerships with SaaS providers and our customers, ensuring that together, we shape the future of business technology.

Join us on this journey to transform the way you choose, use, and experience software.
''')
    
# Contact Page
elif page == "Contact":
    def send_email(name, email, message):
        # Set up the server and email credentials
        smtp_server = "smtp.gmail.com"  # Change this if you are using a different email provider
        smtp_port = 587
        sender_email = "your_email@gmail.com"  # Replace with your email
        sender_password = "your_password"  # Replace with your email password

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg['Subject'] = f"Contact Form Submission from {name}"

        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the server and send the email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Use TLS for security
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    # Streamlit page
    st.title("Contact Us")

    # Form for user input
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        # Submit button
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if send_email(name, email, message):
                st.success("Your message has been sent successfully!")
            else:
                st.error("There was an error sending your message. Please try again.")
