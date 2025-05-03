const form = document.getElementById('loginForm');
      const container = document.getElementById('loginBox');

      form.addEventListener('submit', function (e) {
        e.preventDefault(); // evita envio imediato
        container.classList.add('fade-out');

        // envia o form após a animação (~500ms)
        setTimeout(() => {
          form.submit();
        }, 500);
      });