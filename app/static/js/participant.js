document.addEventListener(
    "DOMContentLoaded",
    () => {

        let currentParticipantId = null;

        const searchInput =
            document.getElementById("searchInput");

        const createForm =
            document.getElementById(
                "createParticipantForm"
            );

        const editForm =
            document.getElementById(
                "editParticipantForm"
            );

        const createFields = {
            fullName:
                document.getElementById(
                    "createFullName"
                ),
            email:
                document.getElementById(
                    "createEmail"
                ),
            organization:
                document.getElementById(
                    "createOrganization"
                ),
            conference:
                document.getElementById(
                    "createConference"
                )
        };

        const editFields = {
            fullName:
                document.getElementById(
                    "editFullName"
                ),
            email:
                document.getElementById(
                    "editEmail"
                ),
            organization:
                document.getElementById(
                    "editOrganization"
                ),
            conference:
                document.getElementById(
                    "editConference"
                )
        };

        function getParticipantPayload(fields) {

            return {
                full_name:
                fields.fullName.value,

                email:
                fields.email.value,

                organization:
                fields.organization.value,

                conference_name:
                fields.conference.value
            };

        }

        async function request(
            url,
            method,
            body = null
        ) {

            const options = {
                method
            };

            if (body) {

                options.headers = {
                    "Content-Type":
                        "application/json"
                };

                options.body =
                    JSON.stringify(body);

            }

            const response =
                await fetch(
                    url,
                    options
                );

            if (!response.ok) {

                const error =
                    await response.json();

                throw new Error(
                    error.detail ||
                    "Ошибка запроса"
                );

            }

            return response;

        }

        // Поиск

        if (searchInput) {

            searchInput.addEventListener(
                "input",
                function () {

                    const filter =
                        this.value.toLowerCase();

                    const rows =
                        document.querySelectorAll(
                            "#participantsTable tbody tr"
                        );

                    rows.forEach(row => {

                        const text =
                            row.textContent.toLowerCase();

                        row.style.display =
                            text.includes(filter)
                                ? ""
                                : "none";

                    });

                }
            );

        }

        // Создание

        if (createForm) {

            createForm.addEventListener(
                "submit",
                async (event) => {

                    event.preventDefault();

                    try {

                        console.log(getParticipantPayload(
                            createFields
                        ))

                        await request(
                            "/participants",
                            "POST",
                            getParticipantPayload(
                                createFields
                            )
                        );

                        location.reload();

                    } catch (error) {

                        alert(
                            error.message
                        );

                    }

                }
            );

        }

        // Открытие модалки редактирования

        document
            .querySelectorAll(".edit-btn")
            .forEach(button => {

                button.addEventListener(
                    "click",
                    () => {

                        currentParticipantId =
                            button.dataset.id;

                        editFields.fullName.value =
                            button.dataset.fullName;

                        editFields.email.value =
                            button.dataset.email;

                        editFields.organization.value =
                            button.dataset.organization;

                        editFields.conference.value =
                            button.dataset.conference;

                    }
                );

            });

        // Обновление

        if (editForm) {

            editForm.addEventListener(
                "submit",
                async (event) => {

                    event.preventDefault();

                    if (
                        !currentParticipantId
                    ) {
                        return;
                    }

                    try {

                        await request(
                            `/participants/${currentParticipantId}`,
                            "PUT",
                            getParticipantPayload(
                                editFields
                            )
                        );

                        location.reload();

                    } catch (error) {

                        alert(
                            error.message
                        );

                    }

                }
            );

        }

        // Удаление

        document
            .querySelectorAll(".delete-btn")
            .forEach(button => {

                button.addEventListener(
                    "click",
                    async () => {

                        const confirmed =
                            confirm(
                                "Удалить участника?"
                            );

                        if (!confirmed) {
                            return;
                        }

                        try {

                            await request(
                                `/participants/${button.dataset.id}`,
                                "DELETE"
                            );

                            location.reload();

                        } catch (error) {

                            alert(
                                error.message
                            );

                        }

                    }
                );

            });

    }
);