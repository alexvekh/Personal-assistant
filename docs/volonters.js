// Get the element with id "volunteers-list" from the HTML
const volunteerList = document.getElementById("volunteers-list");

// Assuming "data.json" is in the same folder as your HTML
fetch("./../package/src/data.json") // Adjust the path if necessary
  .then((response) => response.json())
  .then((data) => {
    data.records.forEach((volunteer) => {
      const volunteerItem = document.createElement("li");
      volunteerItem.innerHTML = `
        <h3>${volunteer.name}</h3>
        <p>Телефони: ${volunteer.phones.join(", ")}</p>
        <p>День народження: ${volunteer.birthday}</p>
        <p>Електронні адреси: ${volunteer.emails.join(", ")}</p>
        <p>Адреса: ${volunteer.addresses.join(", ")}</p>
        <p>Останній внесок: ${volunteer.amount} грн</p>
      `;
      volunteerList.appendChild(volunteerItem);
    });
  });
<<<<<<< HEAD
exit;
=======
>>>>>>> site
