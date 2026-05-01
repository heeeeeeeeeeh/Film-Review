window.onload = function () {
    let form = null;
    document.querySelectorAll("form").forEach((formElem) => {
        formElem.addEventListener("submit", function (e) {
            form = this;
            e.preventDefault();
            fetch(form.action, {
                method: "POST",
                headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new FormData(form)
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                    console.log("Success:", form);
                    form.reset();
                } else if (data.errors) {
                    alert("Email: " + data.errors.email);
                }
            })
        });
    });
}
