async function sendMessage() {
    const userInputElement = document.getElementById('userInput');
    const userInput = userInputElement.value;
    if (userInput.trim() === '') return;

    // Clear the input box immediately after getting the value
    userInputElement.value = '';

    const outputDiv = document.getElementById('output');
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = 'You: ' + userInput;
    outputDiv.appendChild(userMessage);

    // Send user input to the backend
    const response = await fetch('http://localhost:5000/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    });

    const data = await response.json();
    const aiMessage = document.createElement('div');
    aiMessage.className = 'message ai-message';
    aiMessage.textContent = "AI Response: " + data.response;
    outputDiv.appendChild(aiMessage);

    outputDiv.scrollTop = outputDiv.scrollHeight;
}