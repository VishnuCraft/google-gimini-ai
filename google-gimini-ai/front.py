def get_html():
    return '''
    <html>
    <head>
        <title>Generative Gemini AI Prompt</title>
        <style>
            body { font-family: Arial, sans-serif; justify-content: center; align-items: center; height: 100vh; background-color: #f4f4f9; margin: 0; }
            h1 { color: #333; }
            form { max-width: 400px; padding: 20px; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 8px; }
            label, input, button, h3, div#response { display: block; width: 100%; margin-bottom: 10px; }
            input[type="text"], input[type="file"] { padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; }
            button { padding: 10px; background-color: #007bff; color: #fff; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
            div#response { padding: 10px; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 4px; min-height: 50px; font-size: 14px; color: #333; }
        </style>
        <script>
            async function generateContent(event) {
                event.preventDefault();

                const promptInput = document.getElementById('prompt');
                const imageInput = document.getElementById('image');
                const prompt = promptInput.value;
                const responseDiv = document.getElementById('response');

                responseDiv.textContent = "Generating...";
                
                const formData = new FormData();
                formData.append('prompt', prompt);
                if (imageInput.files[0]) {
                    formData.append('image', imageInput.files[0]);
                }
                
                try {
                    const res = await fetch('/generate', {
                        method: 'POST',
                        body: formData
                    });

                    const data = await res.json();
                    responseDiv.textContent = data.response;

                    promptInput.value = "";
                    imageInput.value = ""; // Clear the image input
                } catch (error) {
                    console.error('Error:', error);
                    responseDiv.textContent = "Failed to generate response.";
                }
            }
        </script>
    </head>
    <body>
        <form onsubmit="generateContent(event)">
            <h1>Generate Gemini AI Response</h1>
            <label for="prompt">Enter your prompt:</label>
            <input type="text" id="prompt" name="prompt" required>
            <label for="image">Upload an image (optional):</label>
            <input type="file" id="image" name="image" accept="image/*">
            <button type="submit">Generate</button>
            <h3>Response:</h3>
            <div id="response"></div>
        </form>
    </body>
    </html>
    '''
