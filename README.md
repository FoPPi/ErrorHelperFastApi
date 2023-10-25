<div align=center>
   <img width=250 src=https://i.ibb.co/BTsjBGh/IMG-20231025-141200-539.png alt='logo' />
   <h1>ErrorHelperFastApi - FastAPI for Error Helper Extension</h1>
</div>

**ErrorHelperFastApi** is a FastAPI project that provides an API for the "Error Helper" Visual Studio Code extension. This API allows the extension to request code fixes for selected code lines and receive improved code from the server.

## Features

- Offers an API endpoint for code fixes.
- Integrates seamlessly with the "Error Helper" Visual Studio Code extension.
- Provides quick responses to code fix requests.

## Installation

1. Clone the ErrorHelperFastApi repository from GitHub.

   ```bash
   git clone https://github.com/yourusername/ErrorHelperFastApi.git
   ```

2. Change into the project directory.

   ```bash
   cd ErrorHelperFastApi
   ```

3. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server.

   ```bash
   uvicorn main:app --reload
   ```

The API should now be accessible at `http://127.0.0.1:8000`.

## API Endpoint

### `/helper/{language}/{codeLine}`

- `GET` Request
- Parameters:
  - `{language}`: The language of the code (e.g., `python`, `cpp`).
  - `{codeLine}`: The selected code line that requires fixing.

**Example Request:**

```bash
curl http://127.0.0.1:8000/helper/python/def%20hello%28%29%3A%0A%20%20pritn%28%22Hello%2C%20World!%22%29
```

**Example Response:**

```json
{
  "response_type": "OK",
  "response": "def hello():\n    print('Hello, World!')",
  "all_response": [[
    "python",
    "def hello():\n    print('Hello, World!')"
  ]],
  "full_response": "text"
}
```

## Usage with Error Helper Extension

1. Install and configure the "Error Helper" extension in Visual Studio Code.

2. Open a code file in Visual Studio Code.

3. Select a code line that you want to fix.

4. Right-click to open the context menu and choose the "Fix Code Line" option.

5. The extension sends a request to the ErrorHelperFastApi server, which responds with an improved code line.

6. The extension replaces the selected code line with the improved code.

## Known Issues

Please check the [GitHub Issues](https://github.com/yourusername/ErrorHelperFastApi/issues) for known issues and report any new ones you come across.

## Contribute

If you would like to contribute to this project or have ideas for improvements, please check our [GitHub repository](https://github.com/yourusername/ErrorHelperFastApi) for guidelines on contributing and open issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
