const comment_button_element = document.getElementById("comment-button");
const comment_input_element = document.getElementById("user-input");

async function send_comment(comment, city, country) {
    const data = await fetch(
        `/api/comment?comment=${comment}&country=${country}&city=${city}`
    );
    const data_returned = data.json();

    console.log(data_returned);
}

comment_button_element.addEventListener("click", (e) => {
    if (comment_input_element.value != "") {
        const comment_data = comment_input_element.value
        comment_input_element.value = ""

        const city = window.location.href.split("/")[5];
        const country = document.querySelector("#country").innerText;
        send_comment(comment_data, city, country)
    } 
});