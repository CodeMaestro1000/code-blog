// Modal Implementation
const modals = document.querySelectorAll(".modal");
const open_modal_btns = document.querySelectorAll(".modal-btn");
const close_spans = document.querySelectorAll(".close") //span to close the modal
const cancel_btn = document.querySelector("#cancel");

open_modal_btns.forEach((btn, index) => {
    btn.addEventListener('click', ()=>{
        modals[index].classList.remove("d-none");
        modals[index].classList.add("d-block");
});// close btn event listener 
}); // close forEach iter 

close_spans.forEach((span, index) =>{
    span.addEventListener('click', ()=>{
        modals[index].classList.remove("d-block");
        modals[index].classList.add("d-none");
});
}); // end close_spans forEach iter

window.addEventListener('click', (e)=>{ // clicking anywhere on the window removes the modal
    if (e.target == modals[0]){
        modals[0].classList.remove("d-block");
        modals[0].classList.add("d-none");
    }
    else if (e.target == modals[1]){
        modals[1].classList.remove("d-block");
        modals[1].classList.add("d-none");
    }
    
});

// cancel button included in modal to close modal (only applies to delete modal)
cancel_btn.addEventListener('click', (e)=>{
    e.preventDefault();
    modals[0].classList.remove("d-block");
    modals[0].classList.add("d-none");
});

$( document ).ready(function() {
    const body = document.querySelector(".project-body");
    const regex = /```.*?```/g; // regex to parse img src attribute (text in-between ```-``` quotes)
    const matches = body.textContent.match(regex); 
    const img_src = matches[0].split('```')[1];
    
    // Add image to page by using regex to parse the src attribute o
    const newHtml = body.textContent.replace(regex, `<div class="image-container"><img src="${`http://127.0.0.1:8000/${img_src}`}"/></div>`);
    body.innerHTML = newHtml;
});

