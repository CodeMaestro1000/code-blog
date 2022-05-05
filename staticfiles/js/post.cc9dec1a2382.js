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
if (cancel_btn){ // only run if there is a prescence of delete modal and by implication a cancel button
    cancel_btn.addEventListener('click', (e)=>{
        e.preventDefault();
        modals[0].classList.remove("d-block");
        modals[0].classList.add("d-none");
    });
}


$( document ).ready(function() {
    const body = document.querySelector(".project-body");
    const img_regex = /%%.*?%%/g; // regex to parse img src attribute (text in-between ```-``` quotes)
    const code_regex = /```.*?```/sg; // `xxx` for code, s modifier is for multiline code snippets
    const img_matches = body.textContent.match(img_regex); 
    const code_matches = body.textContent.match(code_regex);
    
    let newHtml = body.textContent;
    
    // regex to match images
    let i = 0;
    newHtml = newHtml.replace(img_regex, function () {
        i += 1;
        let string = img_matches[i-1].split('%%')[1];
        if (string.includes('https') || (string.includes('/static/images/'))){
            return `<div class="image-container"><img src="${img_matches[i-1].split('%%')[1]}"/></div>`; 
        }
        else return `<div class="image-container"><img src="/static/images/${img_matches[i-1].split('%%')[1]}"/></div>`;} 
    ); // end replace statement

    // regex to match code snippets
    i = 0;
    newHtml = newHtml.replace(code_regex, function () {
        let code_text = ''
        i += 1;
        let text_object = code_matches[i-1].split('\n');
        if (text_object.length > 1){ // multi-line code formatting
            for (let text of text_object) {
                if (text != '```'){
                    // Rule -> For multi-line code, ensure that the code starts on a new line after # and ends on a line before #
                    text = formatCode(text);
                    code_text += `${text}\n`;
                }
            } // end for
            return `<pre class="code-container"><code>${code_text}</code></pre>`
        } // end outer if
        else { 
            // single line code formatting
            let splits = text_object[0].split('```');
            code_text = splits[1];
            return `<code class="inline-code code-container">${code_text}</code>`;
        }
        } // close function block
    ); // end replace statement
    
    
    body.innerHTML = newHtml; // update body
});

function formatCode(text) {
    const keywords = [  'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'del', 
                        'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
                        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    const keyword_regex = new RegExp("\\b(?:" + keywords.join("|") + ")\\b", "g");
    const comment_regex = /#(.*)/g;
    const function_name_regex = /\b(?<=def\b).*/g; // for styling function names
    const def_keyword_regex = /\bdef\b/g; // for styling the class regex
    const string_regex = /'.*?'/g; 
    //const class_regex = /class/g;
    const class_name_regex = /(?<=class<\/span>).*/g; // for styling class names

    // These matches are useful for the replace function operation
    let keyword_matches = text.match(keyword_regex);
    let comment_matches = text.match(comment_regex); 
    let function_name_matches = text.match(function_name_regex);  
    let def_keyword_matches = text.match(def_keyword_regex);
    let string_matches = text.match(string_regex);
    
    
    let j = 0;
    text = text.replace(keyword_regex, function() {
        j += 1;
        return `<span class="keyword">${keyword_matches[j-1]}</span>`;
    });

    j = 0;
    text = text.replace(comment_regex, function() {
        j += 1;
        return `<span class="code-comment">${comment_matches[j-1]}</span>`;
    });

    j = 0;
    text = text.replace(function_name_regex, function() {
        j += 1;
        return `<span class="function">${function_name_matches[j-1]}</span>`;
    });

    j = 0;
    text = text.replace(def_keyword_regex, function() {
        j += 1;
        return `<span class="keyword">${def_keyword_matches[j-1]}</span>`;
    });

    j = 0;
    text = text.replace(string_regex, function() {
        j += 1;
        return `<span class="string">${string_matches[j-1]}</span>`;
    });

    j = 0;
    let class_name_matches = text.match(class_name_regex);
    text = text.replace(class_name_regex, function() {
        j += 1;
        return `<span class="class-name">${class_name_matches[j-1]}</span>`;
    });
    return text;
}
