from fastapi import FastAPI
import re
import g4f

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Error Helper API"}


@app.get("/helper/{language}/{codeLine}")
async def helper(language: str, codeLine: str):
    pattern = r'```(.*?)\n(.*?)\n```'
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user",
                   "content": "{language}. fix code line: {codeLine}".format(language=language, codeLine=codeLine)}],
    )

    matches = re.findall(pattern, response)

    if matches:
        return {"response_type": "OK", "response": matches[0][1]}
    else:
        print(response)
        return {"response_type": "error", "response": "Error: No code block found or code correct"}
