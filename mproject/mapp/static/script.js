document.getElementById('import-btn').addEventListener('click', function() {
    document.getElementById('file-input').click();
});

document.getElementById('file-input').addEventListener('change', function() {
    console.log(this.files[0]); // Log the selected file for demonstration
});