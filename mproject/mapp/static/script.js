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
 
        // ===========Table=============

        function calculateTotal() {
            var input1 = parseFloat(document.getElementById('id_input1').value) || 0;
            var input2 = parseFloat(document.getElementById('id_input2').value) || 0;
            var input3 = parseFloat(document.getElementById('id_input3').value) || 0;
            var total = input1 + input2 + input3;
            document.getElementById('total').innerText = total;
            return total;
        }

        function validateInputs() {
            var total = calculateTotal();
            var errorElement = document.getElementById('error-message');
            if (total > 40) {
                errorElement.innerText = 'The total should not exceed 40.';
                return false;
            } else {
                errorElement.innerText = '';
                return true;
            }
        }

        function toggleEdit() {
            var inputs = document.querySelectorAll('input[type=number]');
            var editButton = document.getElementById('editButton');
            var isEditable = editButton.innerText === 'Edit';

            inputs.forEach(function(input) {
                input.readOnly = !isEditable;
                if (isEditable) {
                    input.addEventListener('input', validateInputs);
                    input.classList.remove('gray-input');
                } else {
                    input.removeEventListener('input', validateInputs);
                    input.classList.add('gray-input');
                }
            });

            editButton.innerText = isEditable ? 'Done' : 'Edit';

            if (!isEditable && validateInputs()) {
                // This part can be used to save the form when 'Done' is clicked
                document.querySelector('form').submit();
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('id_input1').addEventListener('input', calculateTotal);
            document.getElementById('id_input2').addEventListener('input', calculateTotal);
            document.getElementById('id_input3').addEventListener('input', calculateTotal);
            document.getElementById('editButton').addEventListener('click', toggleEdit);
            calculateTotal(); // Initial calculation
        });