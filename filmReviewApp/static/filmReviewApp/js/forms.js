window.onload = function () {
    let form = null;
    document.querySelectorAll("form").forEach((formElem) => {
        formElem.addEventListener("submit", function (e) {
            clearMessages(this);
            form = this;
            e.preventDefault();
            fetch(form.action, {
                method: "POST",
                headers: {
                "X-CSRFToken": form.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new FormData(form)
            })
            .then(response =>response.json())
            .then(data => {
                if (data.redirected) {
                    window.location.href = data.url;
                    return;
                }
                if (data.message) {
                    let successElement = form.querySelector(".success-message");
                    if (successElement) {
                        successElement.textContent = data.message;
                    }
                    form.reset();
                } else if (data.errors) {
                    let errorKeys = Object.keys(data.errors);
                    errorKeys.forEach(key => {
                        let errorElement = form.querySelector(`.error-${key}`);
                        if (errorElement) {
                            errorElement.textContent = data.errors[key].join("<br>");
                        } else {
                            let nonFieldErrorElement = form.querySelector(".error-non_field_errors");
                            if (nonFieldErrorElement) {
                                nonFieldErrorElement.textContent = data.errors[key].join("<br>");
                            }
                        }
                    });
                }
            })
        });
    });
}

function clearMessages(form) {
    form.querySelectorAll(".error").forEach(elem => elem.textContent = "");
    form.querySelectorAll(".success-message").forEach(elem => elem.textContent = "");
}   
