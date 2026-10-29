document.addEventListener("DOMContentLoaded", () => {
  // Mostrar e ocultar senhas
  document.querySelectorAll(".toggle").forEach((botao) => {
    botao.addEventListener("click", () => {
      const campo = document.getElementById(botao.dataset.alvo);

      // Evita erros se o campo não existir
      if (!campo) return;

      const mostrando = campo.type === "text";

      campo.type = mostrando ? "password" : "text";

      botao.classList.toggle("visivel", !mostrando);

      botao.setAttribute(
        "aria-label",
        mostrando ? "Mostrar senha" : "Ocultar senha",
      );
    });
  });

  // Fechar notificações
  document.querySelectorAll(".toast").forEach((aviso) => {
    const fechar = () => {
      // Evita executar o fechamento várias vezes
      if (aviso.classList.contains("sairDiv")) return;

      aviso.classList.add("sairDiv");

      setTimeout(() => {
        aviso.remove();
      }, 300);
    };

    aviso.addEventListener("click", fechar);

    setTimeout(fechar, 6000);
  });
});