from fastapi import FastAPI
import re
import g4f

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Error Helper API"}


@app.get("/helper/{language}/{codeLine}")
async def helper(language: str, codeLine: str):
    pattern = r'```([\s\S]*?)\n([\s\S]*?)\n```'
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user",
                   "content": "No text. Only code in answer. {language}. Fix code line: {codeLine}".format(language=language, codeLine=codeLine)}],
    )

    matches = re.findall(pattern, response)

    if matches:
        return {"response_type": "OK",
                "response": matches[0][1],
                "all_response": matches}
    else:
        return {"response_type": "error",
                "response": "Error: No code block found or code correct.",
                "full_response": response}
