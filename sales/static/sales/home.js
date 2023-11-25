
const reportBtn = document.getElementById('report-btn');
const img       = document.getElementById('img');
const modalBody = document.getElementById('modal-body');

const reportName    = document.getElementById('id_name');
const reportRemarks = document.getElementById('id_remarks');
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
const reportForm = document.getElementById('report-form')
console.log(reportName)
console.log(reportRemarks)
console.log(csrf)

if ( img ) {
    reportBtn.classList.remove('not-visible');
}

reportBtn.addEventListener('click', ()=>{
    console.log('clicked');
    img.setAttribute('class', 'w-100');
    modalBody.prepend(img);

    reportForm.addEventListener('submit', e=>{
        e.preventDefault();
        const formData = new FormData();
        //formData.append('csrfmiddlewaretoken', csrf);
        formData.append('name', reportName.value);
        formData.append('remarks', reportRemarks.value);
        formData.append('image', img.src)

        $.ajax({ 
            headers: { "X-CSRFToken": csrf },
            type: 'POST',
            url:  'reports/save/',
            data: formData,
            success: function(response){
                console.log("SUCCESS:")                
                console.log(response);
            },
            error: function(response){
                console.log("ERROR:")
                console.log(response);
            },
            processData: false,
            contentType: false,
        })
    })
})