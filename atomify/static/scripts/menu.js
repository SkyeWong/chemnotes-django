$(function () {
    function toggleScrolled() {
        $(".nav-container").toggleClass("sticky", window.scrollY > 0 && window.innerWidth > 1100);
    }

    // initial check to see if page is loaded as already scrolled
    toggleScrolled();

    // if the page is scrolled down, make the header shrink
    $(window).on("scroll", toggleScrolled);

    function setAriaExpandedFalse() {
        $(".dropdown-btn").each(
            function () { $(this).attr("aria-expanded", "false") }
        );
    }

    function closeDropdownMenu() {
        $(".dropdown").each(function () {
            $(this).removeClass("active");
        });
    }

    $(".dropdown-btn").each(function () {
        $(this).on("click", function (e) {
            const dropdownIndex = this.dataset.dropdown;

            $("#" + dropdownIndex).toggleClass("active");
            $(".dropdown").each(function () {
                if ($(this).attr("id") !== dropdownIndex) {
                    $(this).removeClass("active");
                }
            });
            e.stopPropagation()

            $(this).attr(
                "aria-expanded",
                $(this).attr("aria-expanded") === "false" ? "true" : "false"
            );
        });
    });

    // close dropdown menu when the dropdown links are clicked
    $(".dropdown a").each(function () {
        $(this).on("click", function () {
            closeDropdownMenu();
            setAriaExpandedFalse();
        })
    });

    // close dropdown menu when you click on the document body
    $(document).on("click", function (e) {
        const target = $(e.target).parentsUntil(".menu-bar>li", ".dropdown");
        if (!$(target).hasClass("dropdown") && window.innerWidth > 1200) {
            closeDropdownMenu();
            setAriaExpandedFalse();
        }
    });

    // close dropdown when the escape key is pressed
    $(document).on("keydown", function (e) {
        if (e.key === "Escape") {
            closeDropdownMenu();
            setAriaExpandedFalse();
        }
    });

    $("#hamburger").on("click", function () {
        $("nav").toggleClass("show");
        $("#hamburger").attr(
            "aria-expanded",
            $("#hamburger").attr("aria-expanded") === "false" ? "true" : "false"
        ).toggleClass("active");
    });
});