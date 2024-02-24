# pip install -q -U google-generativeai
import google.generativeai as genai

# define api key
api_key = 'AIzaSyB_gNzSd-1rLD1ciM0vU82-ISMIcECNP-I'
genai.configure(api_key=api_key)

# listing the available models
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# selecting the model
model = genai.GenerativeModel('gemini-pro')

# passing the prompt : basic response
prompt = 'philosophical definition of life?'
response = model.generate_content(prompt)

# can customize the saftey settings
# streming the output
print(response.text.replace(',','\n').replace('.','\n'))
