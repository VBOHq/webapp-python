import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
print('Hash_password', hashed_passwords)

st.markdown(
    f'<style>{open("assets/style.css").read()}</style>',
    unsafe_allow_html=True
)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# intiate the login wigdet
name, authentication_status, username = authenticator.login('Login', 'main')

# authenticating the user
if authentication_status:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

