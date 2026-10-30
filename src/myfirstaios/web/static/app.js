const chat = document.getElementById("chat");
const input = document.getElementById("message");
const button = document.getElementById("send");
const fileInput = document.getElementById("upload");

function appendMessage(sender, text) {
  const div = document.createElement("div");
  div.innerHTML = `<strong>${sender}:</strong><br>${text}`;
  div.style.marginBottom = "12px";
  chat.appendChild(div);
}

button.addEventListener("click", async () => {
  const message = input.value.trim();
  if (!message) return;

  appendMessage("You", message);
  input.value = "";

  if (fileInput && fileInput.files.length) {
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    await fetch("/upload", {
      method: "POST",
      body: formData
    });
  }

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  appendMessage("Assistant", data.reply);
});

input.addEventListener("keydown", async (event) => {
  if (event.key === "Enter") {
    button.click();
  }
});
