from flask import Flask, request, jsonify
from flask_cors import CORS
from spark_ai_python.core import ChatSparkLLM, ChunkPrintHandler
from spark_ai_python.core.messages import ChatMessage

app = Flask(__name__)
CORS(app)

print("Flask app initialized")

# 配置参数
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
SPARKAI_APP_ID = '5a515d4c'
SPARKAI_API_SECRET = 'MmYwMzk5Yjg2YTNhNzI1MDY1NDE2ZDVi'
SPARKAI_API_KEY = 'c0fcc14f93a2be176374856a78c17cdd'
SPARKAI_DOMAIN = 'lite'

# 初始化星火认知大模型
print("Initializing Spark model...")
spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)

print("Spark model initialized")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    messages = [ChatMessage(role="user", content=user_message)]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])
    return jsonify(response)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, port=5001)
