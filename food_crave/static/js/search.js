const search =

    document.getElementById(
        "globalSearch"
    );

if (search) {

    search.addEventListener(

        "keyup",

        function () {

            let value =

                this.value
                    .toLowerCase();

            document
                .querySelectorAll(
                    ".search-item"
                )

                .forEach(

                    card => {

                        let text =

                            card
                                .querySelector(
                                    ".search-name"
                                )
                                .innerText
                                .toLowerCase();

                        if (

                            text.includes(
                                value
                            )

                        ) {

                            card.style.display =
                                "block";

                        }

                        else {

                            card.style.display =
                                "none";

                        }

                    }

                );

        }

    );

}