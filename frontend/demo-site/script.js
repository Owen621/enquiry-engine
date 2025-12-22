const form = document.getElementById("enquiry-form");
const status = document.getElementById("form-status");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  status.textContent = "Sending...";
  status.style.color = "#0f172a";

  const data = Object.fromEntries(new FormData(form));

  try {
    const res = await fetch("https://enquiry-engine.onrender.com/enquiry", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await res.json();

    if (res.ok) {
      status.textContent = "Thanks — we’ll be in touch shortly.";
      status.style.color = "green";
      form.reset();
    } else {
      status.textContent = result.error || "Something went wrong.";
      status.style.color = "red";
    }
  } catch (err) {
    status.textContent = "Network error. Please try again.";
    status.style.color = "red";
  }
});
