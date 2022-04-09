// Modal Implementation
const modal = document.querySelector("#delete-modal");
const open_modal_btn = document.querySelector("#modal-btn");
const close_span = document.querySelector(".close") //span to close the modal
const cancel_btn = document.querySelector("#cancel");

open_modal_btn.addEventListener('click', ()=>{
    modal.classList.remove("d-none");
    modal.classList.add("d-block");
});

close_span.addEventListener('click', ()=>{
    modal.classList.remove("d-block");
    modal.classList.add("d-none");
});

window.addEventListener('click', (e)=>{ // clicking anywhere on the window removes the modal
    if (e.target == modal){
        modal.classList.remove("d-block");
        modal.classList.add("d-none");
    }
    
});

// cancel button included in modal to close modal
cancel_btn.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.remove("d-block");
    modal.classList.add("d-none");
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

