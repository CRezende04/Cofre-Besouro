const slides = document.querySelectorAll('.slider-container img');
const nextBtn = document.querySelector('.slider-btn.next');
const prevBtn = document.querySelector('.slider-btn.prev');
let current = 0;

function showSlide(index) {
    slides.forEach((img, i) => {
        img.classList.toggle('active', i === index);
    });
}

nextBtn.addEventListener('click', () => {
    current = (current + 1) % slides.length;
    showSlide(current);
});

prevBtn.addEventListener('click', () => {
    current = (current - 1 + slides.length) % slides.length;
    showSlide(current);
});

// Troca automática a cada 5s
setInterval(() => {
    current = (current + 1) % slides.length;
    showSlide(current);
}, 5000);

// Botão de voltar ao topo
const backToTopButton = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTopButton.classList.add("show");
  } else {
    backToTopButton.classList.remove("show");
  }
});

backToTopButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});

// ===== MENU MOBILE FULLSCREEN =====
const menuBtn = document.querySelector(".menu-btn");
const mobileMenu = document.querySelector(".mobile-menu");
const closeMenu = document.querySelector(".close-menu");
const mobileLinks = document.querySelectorAll(".mobile-link");

// Abrir menu
menuBtn.addEventListener("click", () => {
  mobileMenu.classList.add("active");
});

// Fechar menu pelo botão X
closeMenu.addEventListener("click", () => {
  mobileMenu.classList.remove("active");
});

// Fechar menu ao clicar em qualquer link
mobileLinks.forEach(link => {
  link.addEventListener("click", () => {
    mobileMenu.classList.remove("active");
  });
});
/* ===== Hover touch apenas na imagem da seção horários ===== */
document.querySelectorAll(".schedule-image-container").forEach(box => {
  
  // Ativa efeito no toque
  box.addEventListener("touchstart", () => {
    box.classList.add("touch-active");
  }, { passive: true });

  // Remove efeito quando o toque termina
  box.addEventListener("touchend", () => {
    setTimeout(() => box.classList.remove("touch-active"), 200);
  });

  // Se arrastar o dedo, remove o efeito
  box.addEventListener("touchmove", () => {
    box.classList.remove("touch-active");
  }, { passive: true });
});
