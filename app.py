import streamlit as st
import requests
import subprocess
import os

st.title('AGENTIC BASED POWER POINT GENERATOR')

prompt = st.text_area('please write the details of how you want to create the ppt')

pptx_path = "presentation.pptx"     

if st.button('generate ppt'):
    if prompt:
        response = requests.post(
            url="https://chakravardhan06.app.n8n.cloud/webhook-test/82806573-ad5c-4d12-95ac-30d9107686d3",
            json={"prompt": prompt}
        )
        
        if response.status_code == 200:
            st.write('success')

            with open("app1.py", 'w') as file:
                file.write(response.json()['output'].strip("```python"))

            subprocess.run(["python", "app1.py"])

            st.success("PPT generated successfully!")


if os.path.exists(pptx_path):
    with open(pptx_path, "rb") as f1:
        st.download_button(
            label="Download pptx",
            data=f1,
            file_name="generated_presentation.pptx"
        )
else:
    st.info("Generate a PPT to enable the download button.")
