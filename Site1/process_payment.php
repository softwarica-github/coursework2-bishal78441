<?php
include 'connect.php'; // Include the database connection script

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'] ?? '';
    $gender = $_POST['gender'] ?? '';
    $address = $_POST['address'] ?? '';
    $email = $_POST['email'] ?? '';
    $pincode = $_POST['pincode'] ?? '';
    $card_type = $_POST['card_type'] ?? '';
    $card_number = $_POST['card_number'] ?? '';
    $exp_date = $_POST['exp_date'] ?? '';
    $cvv = $_POST['CVV'] ?? '';

    // Insert into a table (assuming a table named 'payments' exists)
    $sql = "INSERT INTO payments (name, gender, address, email, pincode, card_type, card_number, exp_date, cvv)
    VALUES ('$name', '$gender', '$address', '$email', '$pincode', '$card_type', '$card_number', '$exp_date', '$cvv')";

    if ($conn->query($sql) === TRUE) {
        echo "Payment processed successfully!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
?>
