function like(slug) {
    var element = document.getElementById("like-" + slug);
    var count = document.getElementById("count-" + slug);

    $.get(`/article/${slug}/like/`).then(res => {
        if (res.response === "liked") {
            element.className = "fa fa-heart";
            count.innerText = Number(count.innerText) + 1;
        } else {
            element.className = "fa fa-heart-o";
            count.innerText = Number(count.innerText) - 1;
        }
    });
}
