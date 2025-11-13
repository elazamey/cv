// قائمة الهاتف المحمول
document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("mobile-menu-button");
  const menu = document.getElementById("mobile-menu");

  if (toggleBtn && menu) {
    toggleBtn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  }
});
