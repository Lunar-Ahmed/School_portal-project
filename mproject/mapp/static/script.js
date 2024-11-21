document.getElementById('import-btn').addEventListener('click', function() {
    document.getElementById('file-input').click();
});

document.getElementById('file-input').addEventListener('change', function() {
    console.log(this.files[0]); // Log the selected file for demonstration
});


document.getElementById('id_profile_picture').addEventListener('change', function(event) { const [file] = event.target.files; 
    if (file) { const reader = new FileReader(); reader.onload = function(e) { const img = document.getElementById('profile-picture-preview');
         img.src = e.target.result; img.style.display = 'block';} 
         reader.readAsDataURL(file); } });


        // Add event listener to the file input
        document.addEventListener("DOMContentLoaded", function () {
            const passportInput = document.querySelector("input[type='file'][name='passport']");
            if (passportInput) {
                passportInput.addEventListener("change", function (event) {
                    const file = event.target.files[0];
                    const preview = document.getElementById('passport-preview');
                    if (file) {
                        const reader = new FileReader();
                        reader.onload = function (e) {
                            preview.src = e.target.result;
                            preview.style.display = 'block';
                        };
                        reader.readAsDataURL(file);
                    }
                });
            }
        });
 