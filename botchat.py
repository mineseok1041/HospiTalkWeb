import openai
import flask
from flask_cors import CORS

# OpenAI API Key 설정
openai.api_key = ""

# 대화 생성 함수
def getResponse(prompt):    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.7)        
        
        result = response.choices[0].message.content
        
        return result
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

app = flask.Flask(__name__)
CORS(app)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    prompt = flask.request.form['message']
    result = getResponse(prompt)
    return result

if(__name__ == '__main__'):
    app.run()

