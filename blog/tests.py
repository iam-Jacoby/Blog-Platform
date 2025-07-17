================================================= B A S E . H T M L =========================================================

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}Blog Platform{% endblock %}</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">


  <style>
    html, body {
      height: 100%;
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background-color: #f8f9fa;
    }

    body {
      display: flex;
      flex-direction: column;
    }

    .content-wrapper {
      flex: 1;
      padding-top: 80px;
    }

    .navbar {
      background-color: #343a40;
    }

    .navbar-brand, .nav-link {
      color: #fff !important;
    }

    .nav-link:hover {
      color: #ffc107 !important;
    }

    .footer {
      background-color: #343a40;
      color: #fff;
      padding: 1rem;
      text-align: center;
    }

    .navbar .container-fluid {
      padding-left: 0;
      padding-right: 0;
    }

    .search-form input {
      border-radius: 20px;
      padding-left: 15px;
    }

    .search-form button {
      border-radius: 20px;
    }

    .comment-section {
    background-color: #f0f4f8;
    border-radius: 16px;
    padding: 2rem;
    }

    .comment-card {
        background-color: white;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    textarea.form-control:focus {
    border-color: #86b7fe;
    box-shadow: 0 0 0 0.2rem rgba(13, 110, 253, 0.25);
    }

    .btn-primary:hover {
        background-color: #0d6efd;
        box-shadow: 0 4px 12px rgba(13, 110, 253, 0.3);
    }

    .bg-light-blue {
        background-color: #f1f4f9 !important;
    }

    :root {
        --bg: #f8f9fa;
        --text: #212529;
        --card-bg: #fff;
        --nav-bg: #343a40;
    }

    body {
        background-color: var(--bg);
        color: var(--text);
        font-family: 'Poppins', sans-serif;
        transition: background-color 0.3s, color 0.3s;
    }

    .card, .bg-white {
        background-color: var(--card-bg) !important;
    }

    /* Dark Mode Variables */
    body.dark-mode {
        --bg: #121212;
        --text: #e4e4e4;
        --card-bg: #1e1e1e;
        --nav-bg: #212529;
    }

    .navbar {
        background-color: var(--nav-bg) !important;
    }

    .footer {
        background-color: var(--nav-bg);
        color: #fff;
    }

     /* Position the icon inside the toggle knob */
    .form-check-input {
        width: 60px; /* Increased width */
        height: 28px;
        cursor: pointer;
        position: relative;
        background-color: #ccc;
        border: none;
    }

    /* Custom knob icon inside switch */
    .toggle-knob-icon {
        position: absolute;
        top: 2px;
        left: 2px;
        width: 24px;
        height: 24px;
        background-color: white;
        border-radius: 50%;
        transition: all 0.3s ease;
        z-index: 1;
        font-size: 16px;
        pointer-events: none;
    }

    .form-check-input:checked + .toggle-knob-icon {
        left: calc(100% - 26px); /* Moves to right side */
        background-color: #333;
        color: white;
    }

    /* Optional: Remove default Bootstrap blue ring */
    .form-check-input:focus {
        box-shadow: none;
    }

    /* Optional dark mode for body */
    .dark-mode {
        background-color: #121212;
        color: white;
    }

    /* Dark Mode Toggle Custom */
    #darkModeToggle {
    width: 60px;
    height: 30px;
    position: relative;
    background-color: #ccc;
    border-radius: 30px;
    appearance: none;
    -webkit-appearance: none;
    cursor: pointer;
    transition: background 0.3s ease;
    }

    #darkModeToggle::before {
    content: "☀️";
    position: absolute;
    height: 26px;
    width: 26px;
    top: 2px;
    left: 2px;
    background-color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    transition: all 0.3s ease;
    }

    /* When Checked (Dark Mode) */
    #darkModeToggle:checked::before {
    transform: translateX(30px);
    content: "🌙";
    }

    body.dark-mode .card {
    background-color: #1f1f1f;
    color: #e0e0e0;
    }

    body.dark-mode .card-title,
    body.dark-mode .card-text,
    body.dark-mode .card-subtitle {
    color: #f0f0f0;
    }

    .card {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    body, .card, .navbar, .footer {
    transition: background-color 0.3s ease, color 0.3s ease;
    }
  </style>

  {% block extra_css %}{% endblock %}
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg fixed-top">
  <div class="container-fluid px-4">
    <a class="navbar-brand ms-3" href="/">My Blog</a>

    <!-- Search Bar -->
    <div class="mx-auto" style="max-width: 500px; width: 100%;">
        <form class="d-flex search-form" role="search" method="GET" action="{% url 'blog_list' %}">
            <input class="form-control me-2" type="search" name="q" placeholder="Search posts..." aria-label="Search">
            <button class="btn btn-outline-warning" type="submit">Search</button>
        </form>
    </div>


    <div class="d-flex ms-auto me-3 align-items-center">

        <!-- Dark Mode Toggle Switch with Icon -->
        <div class="form-check form-switch position-relative">
            <input class="form-check-input" type="checkbox" id="darkModeToggle">
            <div class="toggle-knob-icon d-flex justify-content-center align-items-center">
                <i id="toggleIcon" class="bi bi-sun-fill"></i>
            </div>
        </div>

      <!-- Links -->
      <a class="nav-link d-inline me-2" href="#">About</a>
      <a class="nav-link d-inline me-2" href="#">Contact</a>
    </div>
  </div>
</nav>

<!-- Main Content -->
<div class="content-wrapper container" style="padding-top: 80px;">
  {% block content %}{% endblock %}
</div>

<!-- Footer -->
<footer class="footer mt-auto">
  &copy; {{ year }} Blog Platform. All rights reserved.
</footer>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

<script>
    const toggle = document.getElementById("darkModeToggle");
    const icon = document.getElementById("toggleIcon");
    const body = document.body;

    // Load saved preference
    if (localStorage.getItem("theme") === "dark") {
        toggle.checked = true;
        body.classList.add("dark-mode");
        icon.className = "bi bi-moon-fill";
    }

    toggle.addEventListener("change", () => {
        body.classList.toggle("dark-mode");
        if (toggle.checked) {
            icon.className = "bi bi-moon-fill";
            localStorage.setItem("theme", "dark");
        } else {
            icon.className = "bi bi-sun-fill";
            localStorage.setItem("theme", "light");
        }
    });
</script>


{% block extra_js %}{% endblock %}
</body>
</html>
