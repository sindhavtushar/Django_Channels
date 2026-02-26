console.log("Sanity check from index.js");

document.addEventListener("DOMContentLoaded", function() {
    const roomInput = document.querySelector("#roomInput");
    const roomConnect = document.querySelector("#roomConnect");
    const roomSelect = document.querySelector("#roomSelect");

    roomInput.focus();

    // submit on Enter
    roomInput.addEventListener("keyup", function(e) {
        if (e.key === "Enter") roomConnect.click();
    });

    // connect button
    roomConnect.addEventListener("click", function() {
        let roomName = roomInput.value.trim();
        if (!roomName) {
            alert("Please enter a room name.");
            return;
        }
        roomName = roomName.replace(/\s+/g, "_"); // optional: replace spaces with underscores
        window.location.pathname = "/chat/" + roomName + "/";
    });

    // select room from list
    roomSelect.addEventListener("change", function() {
        let roomName = roomSelect.value.split(" (")[0].trim();
        if (!roomName) return;
        roomName = roomName.replace(/\s+/g, "_");
        window.location.pathname = "/chat/" + roomName + "/";
    });
});