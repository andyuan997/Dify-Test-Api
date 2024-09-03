import requests
import json

# Dify api
api_key = 'your-api'

# 設置URL
url = 'https://api.dify.ai/v1/workflows/run'

# 依照你的工作流輸入資料定義
payload = {
    "inputs": {"input": "今天天氣如何?"},
    "response_mode": "streaming",
    "user": "abc-123"
}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# 發送POST
response = requests.post(url, json=payload, headers=headers, stream=True)

# 逐行解析
if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8').strip()
            if decoded_line.startswith("data:"):
                json_data = decoded_line[5:].strip()  # 去掉 "data:" 前缀
                try:
                    data = json.loads(json_data)
                    print("解析後的數據:", data)
                except ValueError:
                    print("無法解析的行:", decoded_line)
else:
    print('請求失敗:', response.status_code, response.text)
