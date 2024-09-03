import google.generativeai as genai

gemini_api_key = "Enter your key"

genai.configure(api_key=gemini_api_key)

client = genai.GenerativeModel('gemini-1.5-flash')

user_question = "Write an essay about How to use AI Responsibily"

response = client.generate_content(user_question)
print(response.text)

streaming_response = client.generate_content(user_question, stream=True)
final_output = ''
for delta in streaming_response:
    print(delta.text)
    final_output += delta.text

print("\nFinal Output:")
print(final_output)

