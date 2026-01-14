// ============================================
// DOM Elements
// ============================================
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const typingIndicator = document.getElementById('typing-indicator');
const charCount = document.getElementById('char-count');

// ============================================
// Configuration
// ============================================
const API_URL = 'http://127.0.0.1:5000/chat';
const WELCOME_URL = 'http://127.0.0.1:5000/welcome';
let sessionId = null;

// ============================================
// Initialize
// ============================================
window.addEventListener('load', async () => {
    // Load welcome message
    await loadWelcomeMessage();

    // Focus input
    userInput.focus();
});

// ============================================
// Load Welcome Message
// ============================================
async function loadWelcomeMessage() {
    try {
        const response = await fetch(WELCOME_URL);
        const data = await response.json();

        // Display welcome messages with delay
        for (let i = 0; i < data.messages.length; i++) {
            await new Promise(resolve => setTimeout(resolve, 500 * i));
            addBotMessage(data.messages[i].content, data.messages[i].type);
        }
    } catch (error) {
        console.error('Failed to load welcome message:', error);
        addBotMessage('👋 Hello! I\'m your SRS Ambiguity Detection Assistant. Send me your requirements!');
    }
}

// ============================================
// Character Counter
// ============================================
userInput.addEventListener('input', () => {
    const length = userInput.value.length;
    charCount.textContent = length;

    // Auto-resize textarea (max 10 lines)
    userInput.style.height = 'auto';
    const newHeight = Math.min(userInput.scrollHeight, 240); // ~10 lines max
    userInput.style.height = newHeight + 'px';

    // Warn if approaching limit
    if (length > 9500) {
        charCount.style.color = '#f5576c';
    } else {
        charCount.style.color = 'var(--text-muted)';
    }
});

// ============================================
// Send Message
// ============================================
sendBtn.addEventListener('click', sendMessage);

userInput.addEventListener('keydown', (e) => {
    // Send on Enter (but allow Shift+Enter for new line)
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) {
        return;
    }

    // Add user message to chat
    addUserMessage(message);

    // Clear input
    userInput.value = '';
    userInput.style.height = 'auto';
    charCount.textContent = '0';

    // Show typing indicator
    showTyping();

    // Disable input while processing
    userInput.disabled = true;
    sendBtn.disabled = true;

    try {
        // Send to API
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to get response');
        }

        // Store session ID
        sessionId = data.session_id;

        // Hide typing indicator
        hideTyping();

        // Display bot messages with delay
        for (let i = 0; i < data.bot_messages.length; i++) {
            await new Promise(resolve => setTimeout(resolve, 400));
            const msg = data.bot_messages[i];
            addBotMessage(msg.content, msg.type, msg.data);
        }

    } catch (error) {
        console.error('Error:', error);
        hideTyping();
        addBotMessage('❌ Sorry, I encountered an error. Please try again.');
    } finally {
        // Re-enable input
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
}

// ============================================
// Add Messages to Chat
// ============================================
function addUserMessage(content) {
    const messageDiv = createMessageElement('user', content);
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function addBotMessage(content, type = 'text', data = null) {
    const messageDiv = createMessageElement('bot', content, type, data);
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function createMessageElement(role, content, type = 'text', data = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;

    // Avatar
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = role === 'bot' ? '🤖' : '👤';

    // Content
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';

    if (type === 'suggestion') {
        contentDiv.classList.add('suggestion');
    }

    // Parse markdown-style formatting
    const formattedContent = formatMessageContent(content);
    contentDiv.innerHTML = formattedContent;

    // Add download button if type is 'download'
    if (type === 'download' && data && data.download_url) {
        const downloadBtn = document.createElement('a');
        downloadBtn.href = data.download_url;
        downloadBtn.className = 'download-btn';
        downloadBtn.innerHTML = '📥 Download PDF';
        downloadBtn.download = data.filename || 'improved_srs.pdf';
        downloadBtn.target = '_blank';
        contentDiv.appendChild(document.createElement('br'));
        contentDiv.appendChild(downloadBtn);
    }

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(contentDiv);

    return messageDiv;
}

function formatMessageContent(content) {
    // Convert **text** to <strong>text</strong>
    let formatted = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Convert line breaks to <br>
    formatted = formatted.replace(/\n/g, '<br>');

    return formatted;
}

// ============================================
// Typing Indicator
// ============================================
function showTyping() {
    typingIndicator.classList.remove('hidden');
    scrollToBottom();
}

function hideTyping() {
    typingIndicator.classList.add('hidden');
}

// ============================================
// Scroll to Bottom
// ============================================
function scrollToBottom() {
    setTimeout(() => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 100);
}

// ============================================
// Console Welcome
// ============================================
console.log('%c🤖 SRS Ambiguity Detection Chatbot', 'font-size: 20px; font-weight: bold; color: #667eea;');
console.log('%cChat Mode Activated', 'color: #764ba2;');
console.log('%cPowered by Flask & NLP', 'color: #f5576c;');
