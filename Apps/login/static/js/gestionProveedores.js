(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Desea eliminar este curso?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();