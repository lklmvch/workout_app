//// Making a GET request to fetch data
//fetch('/api/v1/courses/')
//    .then(response => {
//        if (!response.ok) {
//            throw new Error('Network response was not ok');
//        }
//        return response.json(); // Parse the JSON from the response
//    })
//    .then(data => {
//        console.log(data); // Use the data in your frontend
//    })
//    .catch(error => {
//        console.error('There was a problem with the fetch operation:', error);
//    });
//
//// Making a POST request to send data
//fetch('/api/v1/register/', {
//    method: 'POST',
//    headers: {
//        'Content-Type': 'application/json',
//        'Authorization': 'Bearer your-token-here' // For protected routes
//    },
//    body: JSON.stringify({
//        first_name: 'John',
//        last_name: 'Doe',
//        email: 'john.doe@example.com',
//        phone_number: '+375123456789',
//        course: 1 // Example course ID
//    })
//})
//.then(response => response.json())
//.then(data => {
//    console.log('Success:', data);
//})
//.catch(error => {
//    console.error('Error:', error);
//});
