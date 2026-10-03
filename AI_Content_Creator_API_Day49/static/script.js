async function generateContent() {
    const topic = document.getElementById("topic").value.trim();
    const contentType = document.getElementById("contentType").value;
    const output = document.getElementById("output");
    const status = document.getElementById("status");
    const button = document.getElementById("generateBtn");

    if (!topic) {
        output.textContent = "Please enter a topic.";
        return;
    }

    button.disabled = true;
    button.textContent = "Generating...";
    status.textContent = "AI is generating your content...";
    output.textContent = "";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({topic, content_type: contentType})
        });

        const data = await response.json();
        if (!response.ok || !data.success) {
            throw new Error(data.error || "Generation failed.");
        }

        output.textContent = data.content;
        status.textContent = "Content generated successfully.";
    } catch (error) {
        output.textContent = "Error: " + error.message;
        status.textContent = "";
    } finally {
        button.disabled = false;
        button.textContent = "Generate Content";
    }
}

async function copyContent() {
    try {
        await navigator.clipboard.writeText(document.getElementById("output").textContent);
        document.getElementById("status").textContent = "Content copied to clipboard.";
    } catch {
        document.getElementById("status").textContent = "Copy failed.";
    }
}
