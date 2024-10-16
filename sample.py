import streamlit as st
import re
from PIL import Image
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Set page title and icon
import json
import time
st.set_page_config(page_title="SaaS Marketplace", page_icon=":chart_with_upwards_trend:", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Choose your page:")
page = st.sidebar.selectbox("", ["Home", "About Us", "Contact","Software Reviews","Github"])

# Main header
# st.title("SaaS Marketplace")
# st.subheader("We provide information about the latest software that are in the industry and helps you meet your software requirements")

def remove_html_tags(html_content):
    # $ is reserved for latex expression in streamlit so replace it
    html_content = html_content.replace('$', r'\$')
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
elif page == "About Us":
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

elif page=="Software Reviews":
    # Define the API endpoint and authorization token
    API_URL = "https://app.reviewflowz.com/api/v2/accounts/1900/listings"
    LISTINGS_API_URL = "https://app.reviewflowz.com/api/v2/accounts/1900/listings?count=10000"
    AUTH_TOKEN = "biebfR5mWeg36dVubbTUGEx5"  # Replace with your actual token
    # Streamlit app setup
    st.markdown('<h1><span class="jazzee-title">Jazzee</span> Software Reviews</h1>', unsafe_allow_html=True)

    # Input fields for the user
    software_name = st.text_input("Enter the software name:")
    platform = st.selectbox("Select the platform name:", ["G2", "Capterra"])
    base_url = "https://www.g2.com/products/{software}/reviews"
    exp_site_url = base_url.format(software=software_name)
    site_url= st.text_input("Enter the url",value=f"{exp_site_url}")


    # Function to make API request and extract the ID
    def create_listing(software_name, platform, site_url):
        headers = {
            "accept": "*/*",
            "Authorization": f"Bearer {AUTH_TOKEN}",
            "Content-Type": "application/json",
        }
        data = {
            "profile_name": software_name,
            "url": site_url,
            "platform": platform,
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            # Assuming the response contains JSON data with a 'profile_id' field
            response_data = response.json()  # Get the JSON response
            profile_id = response_data.get("profile_id", None)  # Extract 'profile_id'
            return profile_id, response.status_code
        else:
            return None, response.status_code


    # Function to get all listings
    def get_listings(auth_token):
        headers = { 
            "accept": "application/json",
            "Authorization": f"Bearer {auth_token}",
        }

        response = requests.get(LISTINGS_API_URL, headers=headers)
        
        if response.status_code == 200:
            return response.json()  # Return the JSON response
        else:
            st.error(f"Failed to fetch listings. Status Code: {response.status_code}")
            return None

    # Function to get account id    
    def get_account_id(listing,have_id):
        for i in range(len(listing['data'])):
            if listing['data'][i]['platform']==platform and listing['data'][i]['profile_name'].lower()==software_name.lower():
                have_id=1
                # st.write(listing['data'][i]['id'])
                return have_id,listing['data'][i]['id']
        return 0,0
        
    # Function to fetch the review
    def fetch_review(platform, token_number):
        api_url = "https://app.reviewflowz.com/api/v2/accounts/1900/reviews"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer biebfR5mWeg36dVubbTUGEx5"  
        }
        
        params = {
            "platform": platform,
            "review_listing_ids[]": token_number
        }
        
        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return the review data in JSON format
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def extract_text_after_question(paragraph):
        # Split the paragraph at the first occurrence of the question mark '?'
        parts = paragraph.split('?', 1)  # The '1' ensures splitting only at the first question mark
        
        # Check if there was a question mark and return the part after it
        if len(parts) > 1:
            return parts[1].strip()  # Strip to remove leading or trailing spaces
        else:
            return paragraph
    
    def delete_listing(id):
        url = f'https://app.reviewflowz.com/api/v2/accounts/1900/listings/{id}'
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer biebfR5mWeg36dVubbTUGEx5'
        }

        response = requests.delete(url, headers=headers)

        if response.status_code == 200:
            print("Listing deleted successfully.")
        else:
            print(f"Failed to delete listing. Status code: {response.status_code}")

    # Submit button    
    if st.button("Fetch Reviews"):
        listing=get_listings(AUTH_TOKEN)
        # st.write(listing)
        if listing['pagination']['count']>=44:
            first_id=listing['data'][0]['id']
            delete_listing(first_id)
        done=0
        while True:
            listing=get_listings(AUTH_TOKEN)
            account_id=0
            have_id=0
            #to display all the listing 
            # st.write(listing)

            have_id,account_id=get_account_id(listing,have_id)
            if software_name and platform and site_url and have_id!=1:
                # st.write("I am running")
                profile_id, status_code = create_listing(software_name, platform, site_url)
                if status_code == 200 and profile_id:
                    st.success(f"Listing created successfully for {software_name} on {platform}.")
                    dashboard_url = f"https://app.reviewflowz.com/review_profiles/{profile_id}"
                    st.write(f"Visit the dashboard: {dashboard_url}")
                    new_listing=get_listings(AUTH_TOKEN)
                    have_id,account_id=get_account_id(new_listing,have_id)

                    st.write(f"Your id is {account_id}")
                # elif have_id!=1:
                #     st.error(f"Failed to create listing due to incorrect configurations . Status Code: {status_code}")
            elif have_id!=0:
                have_id=have_id
            else:
                st.error("Please fill out all fields.")
            new_listing=get_listings(AUTH_TOKEN)
            # st.write(new_listing)
            have_id,account_id=get_account_id(new_listing,have_id)
            # st.write(account_id)
            
            review_data = fetch_review(platform, account_id)
            if "error" in review_data:
                st.error(f"Failed to fetch the review: {review_data['error']}")
            elif review_data['data']!=[]:
                review=review_data
                sum1=0
                for i in range(len(review['data'])):
                    sum1+=review['data'][i]['rating']
                overall_rating=sum1/len(review['data'])
                # st.write(review_data)
                st.markdown(f"**<span style='font-size: 28px;'>Overall Rating : {round(overall_rating,2)}</span>**",unsafe_allow_html=True)
                st.markdown("__________________________")
                for i in range(len(review['data'])):
                    st.markdown(f"**<span style='font-size: 24px;'>{review['data'][i]['title']}</span>**",unsafe_allow_html=True)
                    st.markdown(f"**<span style='font-size: 20px;'>Rating : {review['data'][i]['rating']}</span>**",unsafe_allow_html=True)
                    st.markdown(f"<span style='font-size: 18px;'>{extract_text_after_question(review['data'][i]['overall'])}</span>",unsafe_allow_html=True)
                    st.markdown(f"**<span style='font-size: 18px;'>Pros :</span>** {review['data'][i]['pros']}",unsafe_allow_html=True)
                    st.markdown(f"**<span style='font-size: 18px;'>Cons :</span>** {review['data'][i]['cons']}",unsafe_allow_html=True)
                    st.markdown("__________________________")
                break
elif page=="Github":
    if st.button("Analysis"):
        software_name = 'Github'
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
                            # st.markdown(f"**<span style='font-size: 40px;'>{name}</span>** ", unsafe_allow_html=True)
                            # st.write("\n")
                            # remove_html_tags((description))
                            # st.markdown(f"***<span style='font-size: 24px;'>Pricing</span>*** {remove_html_tags(pricing)}", unsafe_allow_html=True)
                            st.title("GitHub Analysis")
                            st.write("GitHub provides code hosting services that allow people to build software for open source and private projects.")

                            st.header("Pros")
                            st.markdown("""
                            - **Collaboration**: Seamless version control and team collaboration.
                            - **Integration**: Connects with various CI/CD and developer tools.
                            - **Community**: A huge open-source ecosystem.
                            - **Security Features**: Advanced scanning and alerts.
                            """)

                            st.header("Cons")
                            st.markdown("""
                            - **Pricing for Private Repos**: Can be costly for large teams.
                            - **Learning Curve**: Complexity for beginners.
                            - **Performance**: May face issues with large repositories.
                            """)
                            st.markdown("-" * 40)
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
        API_URL = "https://app.reviewflowz.com/api/v2/accounts/1900/listings"
        LISTINGS_API_URL = "https://app.reviewflowz.com/api/v2/accounts/1900/listings?count=10000"
        AUTH_TOKEN = "biebfR5mWeg36dVubbTUGEx5"  # Replace with your actual token
        # Streamlit app setup
        st.markdown('<h1>Software Reviews</h1>', unsafe_allow_html=True)

        # Input fields for the user
        software_name = 'github'
        platform = 'G2'
        # base_url = "https://www.g2.com/products/{software}/reviews"
        # exp_site_url = base_url.format(software=software_name)
        site_url= "https://www.g2.com/products/github/reviews"


        # Function to make API request and extract the ID
        def create_listing(software_name, platform, site_url):
            headers = {
                "accept": "*/*",
                "Authorization": f"Bearer {AUTH_TOKEN}",
                "Content-Type": "application/json",
            }
            data = {
                "profile_name": software_name,
                "url": site_url,
                "platform": platform,
            }

            response = requests.post(API_URL, headers=headers, data=json.dumps(data))
            
            if response.status_code == 200:
                # Assuming the response contains JSON data with a 'profile_id' field
                response_data = response.json()  # Get the JSON response
                profile_id = response_data.get("profile_id", None)  # Extract 'profile_id'
                return profile_id, response.status_code
            else:
                return None, response.status_code


        # Function to get all listings
        def get_listings(auth_token):
            headers = { 
                "accept": "application/json",
                "Authorization": f"Bearer {auth_token}",
            }

            response = requests.get(LISTINGS_API_URL, headers=headers)
            
            if response.status_code == 200:
                return response.json()  # Return the JSON response
            else:
                st.error(f"Failed to fetch listings. Status Code: {response.status_code}")
                return None

        # Function to get account id    
        def get_account_id(listing,have_id):
            for i in range(len(listing['data'])):
                if listing['data'][i]['platform']==platform and listing['data'][i]['profile_name'].lower()==software_name.lower():
                    have_id=1
                    # st.write(listing['data'][i]['id'])
                    return have_id,listing['data'][i]['id']
            return 0,0
            
        # Function to fetch the review
        def fetch_review(platform, token_number):
            api_url = "https://app.reviewflowz.com/api/v2/accounts/1900/reviews"
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer biebfR5mWeg36dVubbTUGEx5"  
            }
            
            params = {
                "platform": platform,
                "review_listing_ids[]": token_number
            }
            
            try:
                response = requests.get(api_url, headers=headers, params=params)
                response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
                return response.json()  # Return the review data in JSON format
            except requests.exceptions.RequestException as e:
                return {"error": str(e)}
        
        def extract_text_after_question(paragraph):
            # Split the paragraph at the first occurrence of the question mark '?'
            parts = paragraph.split('?', 1)  # The '1' ensures splitting only at the first question mark
            
            # Check if there was a question mark and return the part after it
            if len(parts) > 1:
                return parts[1].strip()  # Strip to remove leading or trailing spaces
            else:
                return paragraph
        
        def delete_listing(id):
            url = f'https://app.reviewflowz.com/api/v2/accounts/1900/listings/{id}'
            headers = {
                'accept': 'application/json',
                'Authorization': 'Bearer biebfR5mWeg36dVubbTUGEx5'
            }

            response = requests.delete(url, headers=headers)

            if response.status_code == 200:
                print("Listing deleted successfully.")
            else:
                print(f"Failed to delete listing. Status code: {response.status_code}")

        # Submit button    
        # if st.button("Fetch Reviews"):
        listing=get_listings(AUTH_TOKEN)
        # st.write(listing)
        if listing['pagination']['count']>=44:
            first_id=listing['data'][0]['id']
            delete_listing(first_id)
        done=0
        while True:
            listing=get_listings(AUTH_TOKEN)
            account_id=0
            have_id=0
            #to display all the listing 
            # st.write(listing)

            have_id,account_id=get_account_id(listing,have_id)
            if software_name and platform and site_url and have_id!=1:
                # st.write("I am running")
                profile_id, status_code = create_listing(software_name, platform, site_url)
                if status_code == 200 and profile_id:
                    st.success(f"Listing created successfully for {software_name} on {platform}.")
                    dashboard_url = f"https://app.reviewflowz.com/review_profiles/{profile_id}"
                    st.write(f"Visit the dashboard: {dashboard_url}")
                    new_listing=get_listings(AUTH_TOKEN)
                    have_id,account_id=get_account_id(new_listing,have_id)

                    st.write(f"Your id is {account_id}")
                # elif have_id!=1:
                #     st.error(f"Failed to create listing due to incorrect configurations . Status Code: {status_code}")
            elif have_id!=0:
                have_id=have_id
            else:
                st.error("Please fill out all fields.")
            new_listing=get_listings(AUTH_TOKEN)
            # st.write(new_listing)
            have_id,account_id=get_account_id(new_listing,have_id)
            # st.write(account_id)
            
            review_data = fetch_review(platform, account_id)
            if "error" in review_data:
                st.error(f"Failed to fetch the review: {review_data['error']}")
            elif review_data['data']!=[]:
                review=review_data
                sum1=0
                for i in range(len(review['data'])):
                    sum1+=review['data'][i]['rating']
                overall_rating=sum1/len(review['data'])
                # st.write(review_data)
                st.markdown(f"**<span style='font-size: 28px;'>Overall Rating : {round(overall_rating,2)}</span>**",unsafe_allow_html=True)
                st.markdown("__________________________")
                for i in range(len(review['data'])):
                    st.markdown(f"**<span style='font-size: 24px;'>{review['data'][i]['title']}</span>**",unsafe_allow_html=True)
                    st.markdown(f"**<span style='font-size: 20px;'>Rating : {review['data'][i]['rating']}</span>**",unsafe_allow_html=True)
                    st.markdown(f"<span style='font-size: 18px;'>{extract_text_after_question(review['data'][i]['overall'])}</span>",unsafe_allow_html=True)
                    st.markdown(f"**<span style='font-size: 18px;'>Pros :</span>** {review['data'][i]['pros']}",unsafe_allow_html=True)
                    st.markdown(f"**<span style='font-size: 18px;'>Cons :</span>** {review['data'][i]['cons']}",unsafe_allow_html=True)
                    st.markdown("__________________________")
                break
        st.header("Some reviews fetched from Socials")
        st.markdown("____________________________________________")

        st.markdown(f"**<span style='font-size: 24px;'>Why Github Won</span>**",unsafe_allow_html=True)
        st.markdown("Posted on HackerNews")
        st.markdown("Posted by : bluGill")
        st.markdown("I still miss hg. I migrated to github years ago because github is a much better workflow, but I miss hg which can answer questions that git cannot.")
        st.markdown("[Open the post](https://news.ycombinator.com/item?id=41491592)")

        st.markdown("____________________________________________")

        st.markdown(f"**<span style='font-size: 24px;'>Do you publish your code on crates.io?</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted on Rust</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted by : Jesper</span>**",unsafe_allow_html=True)
        st.markdown(f"<span style='font-size: 18px;'>For a lot of things github is good enough - easy to specify a toplevel github dependency in Cargo.toml.</span>",unsafe_allow_html=True)
        st.markdown("[Open the post](https://users.rust-lang.org/t/do-you-publish-your-code-on-crates-io/119443/20)",unsafe_allow_html=True)

        st.markdown("____________________________________________")

        st.markdown(f"**<span style='font-size: 18px;'>Career Switchers In Cybersecurity Whats Your Story</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted on r/cybersecurity</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted by : Lumnatic</span>**",unsafe_allow_html=True)
        st.markdown(f'''<span style='font-size: 18px;'>GitHub is good, but I'd say that depends on what you're trying to apply for/become. If what you're applying for isn't somewhere centered around scripting/automation, or maybe IaC, etc, I'd be worried that whomever would be looking at my resume wouldn't be familiar enough with GitHub to navigate the repos and branches.

For me personally, I just paid for like a 2-3 year domain hosting plan on one of the myriad web hosting services, and made blog-style posts on my projects. For example, when I was looking to become an analyst, I started up a small cluster of VMs on different operating systems in Oracle VirtualBox and stood up the open-source SIEM Wazuh. Showcased enrolling the hosts as agents with the manager and went through looking at some vulnerabilities and alerts, with screenshots and descriptions of how I did things and my thought process. Also went through a few posts of myself doing CTFs.</span>''',unsafe_allow_html=True)
        st.markdown("[Open the post](https://www.reddit.com/r/cybersecurity/comments/1ew4frm/comment/lj7kn9e/)")

        st.markdown("____________________________________________")

        st.markdown(f"**<span style='font-size: 24px;'>Are You Using Llms In Your Devops Work</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted on r/devops</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted by : Antebios</span>**",unsafe_allow_html=True)
        st.markdown(f"<span style='font-size: 18px;'>This week GitHub Copilot saved my ass and hours of work with a codebase that I was not familiar with at work. I had to fix a crucial vulnerability for a react app. But there were breaking changes that were introduced. It took me a while but with Copilot's help I was able to fix the impossible in one day!!!</span>",unsafe_allow_html=True)
        st.markdown("[Open the post](https://www.reddit.com/r/devops/comments/1g2j06f/comment/lrqjcj1/)",unsafe_allow_html=True)

        st.markdown("____________________________________________")

        st.markdown(f"**<span style='font-size: 24px;'>Ais Effect On Coding</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted on r/devlopersPak</span>**",unsafe_allow_html=True)
        st.markdown(f"**<span style='font-size: 18px;'>Posted by : No-Dot755</span>**",unsafe_allow_html=True)
        st.markdown(f'''<span style='font-size: 18px;'>Tell me you last used AI in 2023 without telling me you last used AI in 2023.

Okay, didn’t mean to be salty here - sorry.

Don’t use GitHub CoPilot - it genuinely is shit. Try Cursor with Claude 3.5 as the model, or o1-preview.

It will very likely change your opinion (don’t try it to ‘prove me wrong’, try it out of curiosity).</span>''',unsafe_allow_html=True)
        st.markdown("[Open the post](https://www.reddit.com/r/developersPak/comments/1fwm9g3/comment/lqfpt65/)",unsafe_allow_html=True)
        
        st.markdown("____________________________________________")
