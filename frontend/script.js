const backendUrl = "http://localhost:5000";

async function addNote() {
    const noteInput = document.getElementById("noteInput");
    const note = noteInput.value;
    if (!note) return alert("Type a note");

    const response = await fetch(`${backendUrl}/notes`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({note})
    });

    if (response.ok) {
        noteInput.value = "";
        getNotes();
    } else {
        alert("Failed to add note");
    }
}

async function getNotes() {
    const response = await fetch(`${backendUrl}/notes`);
    const data = await response.json();
    const notesList = document.getElementById("notesList");
    notesList.innerHTML = "";
    data.notes.forEach(n => {
        const li = document.createElement("li");
        li.textContent = n;
        notesList.appendChild(li);
    });
}

getNotes();
