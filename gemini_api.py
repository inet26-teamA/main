"""
・geminiからのメッセージを受け取る
ask_gemini('プロンプト')
"""

import google.generativeai as genai

genai.configure(api_key='AIzaSyAHDMoyXQwswmJA3501X1NP0gpLKzuoQ2A')

def ask_gemini(prompt):
    gemini_pro = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro.generate_content(prompt)
    return response.text

#print(ask_gemini('こんばんは'))