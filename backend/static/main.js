// BASE URL of your Flask backend
const BASE_URL = "http://127.0.0.1:5000";


// ----------------------
// Helper: Show messages
// ----------------------
function showMessage(elemId, text, type = "info") {
  const elem = document.getElementById(elemId);
  elem.innerHTML = `<div class="alert alert-${type} py-2 mb-0">${text}</div>`;
}



// ----------------------
// LOGOUT
// ----------------------
function logout() {
  fetch(`${BASE_URL}/auth/logout`, { method: "POST" })
    .then(() => {
      window.location.href = "/";
    })
    .catch(() => alert("Logout failed"));
}



// ----------------------
// CREATE PROJECT
// ----------------------
document.getElementById("projectForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const projectType = document.getElementById("projectType").value.trim();
  const topic = document.getElementById("topic").value.trim();
  const sectionsRaw = document.getElementById("sections").value.trim();

  const sections = sectionsRaw.split(",").map(s => s.trim()).filter(Boolean);

  if (!topic || sections.length === 0) {
    showMessage("createProjectResult", "Please fill all fields", "danger");
    return;
  }

  try {
    const res = await fetch(`${BASE_URL}/setup/create_project`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        username: "AUTO",   // not used now
        password: "AUTO",
        topic,
        project_type: projectType,
        sections
      })
    });

    const data = await res.json();

    if (!res.ok) {
      showMessage("createProjectResult", data.error || "Error creating project", "danger");
      return;
    }

    showMessage("createProjectResult", `Project created! ID: ${data.project_id}`, "success");

    // Autofill project id
    document.getElementById("projectIdInput").value = data.project_id;

  } catch (err) {
    console.error(err);
    showMessage("createProjectResult", "Network error", "danger");
  }
});



// ----------------------
// GENERATE CONTENT
// ----------------------
document.getElementById("generateBtn").addEventListener("click", async () => {
  const projectId = document.getElementById("projectIdInput").value;

  if (!projectId) {
    showMessage("projectActionResult", "Enter a Project ID.", "warning");
    return;
  }

  showMessage("projectActionResult", "Generating content... wait 5–8 seconds", "info");

  try {
    const res = await fetch(`${BASE_URL}/project/generate/${projectId}`, {
      method: "POST"
    });

    const data = await res.json();

    showMessage("projectActionResult", data.message || "Done!", "success");

    loadSections(projectId);

  } catch (err) {
    console.error(err);
    showMessage("projectActionResult", "Error generating content", "danger");
  }
});



// ----------------------
// LOAD SECTIONS
// ----------------------
document.getElementById("loadSectionsBtn").addEventListener("click", () => {
  const projectId = document.getElementById("projectIdInput").value;

  if (!projectId) {
    showMessage("projectActionResult", "Enter a Project ID.", "warning");
    return;
  }

  loadSections(projectId);
});



async function loadSections(projectId) {
  try {
    const res = await fetch(`${BASE_URL}/project/${projectId}/sections`);
    const data = await res.json();

    if (!res.ok) {
      showMessage("projectActionResult", data.error || "Error loading sections", "danger");
      return;
    }

    // Render all section cards
    renderSections(data);

    // ⭐ ENABLE DOWNLOAD LINKS HERE (AFTER success)
    document.getElementById("docxDownload").href = `${BASE_URL}/export/docx/${projectId}`;
    document.getElementById("pptxDownload").href = `${BASE_URL}/export/pptx/${projectId}`;

  } catch (err) {
    console.error(err);
    showMessage("projectActionResult", "Network error loading sections", "danger");
  }
}



// ----------------------
// RENDER SECTIONS
// ----------------------
function renderSections(projectData) {
  const container = document.getElementById("sectionsContainer");
  container.innerHTML = "";

  const header = document.createElement("h4");
  header.textContent = `Project #${projectData.project_id} — ${projectData.topic}`;
  header.className = "mb-3";
  container.appendChild(header);

  projectData.sections.forEach(sec => {
    const card = document.createElement("div");
    card.className = "card mb-3";

    card.innerHTML = `
      <div class="card-header d-flex justify-content-between">
        <strong>${sec.title}</strong>
        <span class="text-muted">ID: ${sec.id}</span>
      </div>

      <div class="card-body">

        <h6>Generated Content:</h6>
        <pre class="bg-light p-2" style="white-space: pre-wrap;">${sec.content || "(Not generated yet)"}</pre>

        <h6>Refined Content:</h6>
        <textarea id="refined-${sec.id}" class="form-control mb-2" rows="4">${sec.refined_content || ""}</textarea>

        <label class="form-label">Refinement Instruction</label>
        <input id="instruction-${sec.id}" type="text" class="form-control mb-2"
               placeholder="Rewrite in bullet points">

        <button class="btn btn-primary btn-sm" onclick="refineSection(${sec.id})">Refine with AI</button>

        <button class="btn btn-outline-success btn-sm ms-2" onclick="sendFeedback(${sec.id}, 'like')">👍 Like</button>
        <button class="btn btn-outline-danger btn-sm" onclick="sendFeedback(${sec.id}, 'dislike')">👎 Dislike</button>

        <hr>

        <label class="form-label">Add Comment</label>
        <input type="text" id="comment-${sec.id}" class="form-control">
        <button class="btn btn-secondary btn-sm mt-1" onclick="sendComment(${sec.id})">Save Comment</button>

        <div class="mt-2">
          <strong>Feedback:</strong> ${sec.feedback || "None"}<br>
          <strong>Comments:</strong>
          <pre class="bg-light p-2" style="white-space: pre-wrap;">${sec.comments || "(No comments yet)"}</pre>
        </div>

      </div>
    `;

    container.appendChild(card);
  });
}



// ----------------------
// REFINE SECTION
// ----------------------
window.refineSection = async function(sectionId) {
  const instruction = document.getElementById(`instruction-${sectionId}`).value;

  if (!instruction) {
    alert("Please type an instruction.");
    return;
  }

  try {
    const res = await fetch(`${BASE_URL}/section/refine/${sectionId}`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({instruction})
    });

    const data = await res.json();

    if (res.ok) {
      document.getElementById(`refined-${sectionId}`).value = data.refined;
      alert("Refinement done!");
    } else {
      alert(data.error || "Refinement failed");
    }

  } catch (err) {
    console.error(err);
    alert("Network error during refinement.");
  }
};



// ----------------------
// FEEDBACK
// ----------------------
window.sendFeedback = async function(sectionId, feedback) {
  try {
    await fetch(`${BASE_URL}/section/feedback/${sectionId}`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({feedback})
    });

    alert("Feedback saved!");

  } catch (err) {
    console.error(err);
    alert("Feedback failed.");
  }
};


// ----------------------
// COMMENT
// ----------------------
window.sendComment = async function(sectionId) {
  const comment = document.getElementById(`comment-${sectionId}`).value;

  if (!comment) {
    alert("Type a comment first.");
    return;
  }

  try {
    await fetch(`${BASE_URL}/section/comment/${sectionId}`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({comment})
    });

    alert("Comment saved!");

  } catch (err) {
    console.error(err);
    alert("Failed to save comment.");
  }
};
