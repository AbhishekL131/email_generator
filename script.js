function generateEmail() {
    const position = document.getElementById("position").value;
    const company = document.getElementById("company").value;
    const name = document.getElementById("name").value;
    const degree = document.getElementById("degree").value;
    const college = document.getElementById("college").value;
    const experience = document.getElementById("experience").value;
    const gradYear = document.getElementById("grad_year").value;

    if (!position || !company || !name || !degree || !college || !gradYear) {
        document.getElementById("result").innerText = "Please fill in all fields.";
        return;
    }

    fetch(`http://127.0.0.1:8000/generate-email?position=${position}&company=${company}&name=${name}&degree=${degree}&college=${college}&experience=${experience}&grad_year=${gradYear}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data.email;
        })
        .catch(error => {
            document.getElementById("result").innerText = "Error generating email. Try again.";
            console.error("Error:", error);
        });
}
