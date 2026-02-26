console.log("Sanity check from room.js");

const roomNameElement = document.getElementById("roomName");
const roomName = JSON.parse(roomNameElement.textContent);

if (!roomName || roomName.trim() === "") {
    alert("Room name missing. Redirecting to home.");
    window.location.href = "/chat/";
    throw new Error("Room name is empty");
}

const chatLog = document.getElementById("chatLog");
const chatInput = document.getElementById("chatMessageInput");
const chatSend = document.getElementById("chatMessageSend");
const onlineUsers = document.getElementById("onlineUsersSelector");

// helpers
function addOnlineUser(user) {
    if (!document.querySelector(`option[value='${user}']`)) {
        const option = document.createElement("option");
        option.value = user;
        option.innerHTML = user;
        onlineUsers.appendChild(option);
    }
}
function removeOnlineUser(user) {
    const option = document.querySelector(`option[value='${user}']`);
    if (option) option.remove();
}

// focus input
chatInput.focus();

// send message on Enter
chatInput.addEventListener("keyup", function(e) {
    if (e.key === "Enter") chatSend.click();
});

// send message on click
chatSend.addEventListener("click", function() {
    const msg = chatInput.value.trim();
    if (!msg) return;
    chatSocket.send(JSON.stringify({ type: "chat_message", message: msg }));
    chatInput.value = "";
});

// websocket connection
let chatSocket;
function connect() {
    chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`);

    chatSocket.onopen = () => console.log("WebSocket connected");
    chatSocket.onclose = () => {
        console.log("WebSocket closed, retrying in 2s...");
        setTimeout(connect, 2000);
    };
    chatSocket.onerror = err => {
        console.error("WebSocket error:", err);
        chatSocket.close();
    };
    chatSocket.onmessage = e => {
        const data = JSON.parse(e.data);
        switch (data.type) {
            case "chat_message":
                chatLog.value += data.message + "\n";
                chatLog.scrollTop = chatLog.scrollHeight;
                break;
            case "user_join":
                addOnlineUser(data.username);
                break;
            case "user_leave":
                removeOnlineUser(data.username);
                break;
            default:
                console.error("Unknown message type:", data.type);
        }
    };
}

// connect immediately
connect();