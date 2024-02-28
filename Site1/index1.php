<!DOCTYPE html>
<html>
  <head>
    <title>Payment Form</title>
  </head>
  <body bgcolor="lightblue">
    <?php
        
        // Database configuration
        $servername = "localhost"; // Replace with your server name
        $username = "root"; // Replace with your database username
        $password = ""; // Replace with your database password
        $dbname = "premierplan"; // Replace with your database name
  
        // Create connection
        try {
          $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
          // Set the PDO error mode to exception
          $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
          echo "Connection failed: " . $e->getMessage();
        }
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Gather input data from the form
        $name = $_POST['name'];
        $gender = $_POST['gender'];
        $address = $_POST['address'];
        $email = $_POST['email'];
        $pincode = $_POST['pincode'];
        $card_type = $_POST['card_type'];
        $card_number = $_POST['card_number'];
        $exp_date = $_POST['exp_date'];
        $cvv = $_POST['CVV'];

        // Process the data or perform validations here
        // For example, you can save it to a database or perform further checks

        // Display a success message (for demonstration purposes)
        echo "<h2>Payment Successful!</h2>";
        echo "<p>Name: $name</p>";
        echo "<p>Gender: $gender</p>";
        echo "<p>Address: $address</p>";
        echo "<p>Email: $email</p>";
        echo "<p>Pincode: $pincode</p>";
        echo "<p>Card Type: $card_type</p>";
        echo "<p>Card Number: $card_number</p>";
        echo "<p>Expiration Date: $exp_date</p>";
        echo "<p>CVV: $cvv</p>";
      }
    ?>
    
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
      <h1>Payment Form</h1>
      <p>Required fields are followed by*</p>
      <h2>Contact information</h2>
      <p>Name:* <input type="text" name="name" required=""></p>
      <fieldset>
        <legend>Gender*</legend>
        <p>
          Male <input type="radio" name="gender" value="Male" required="">
          Female <input type="radio" name="gender" value="Female" required="">
        </p>
      </fieldset>
      <p>Address: <textarea name="address" id="address" rows="6" cols="80"></textarea></p>
      <p>Email:* <input type="email" name="email" id="email" value="" required="" /></p> 
      <p>Pincode:* <input type="number" name="pincode" id="pincode" value="" required="" /></p>
      <hr>
      <h2>Payment Information</h2>
      <p>Card Type:*
        <select name="card_type" id="card_type" required="">
          <option value="">---select a Card type---</option>
          <option value="visa">Visa</option>
          <option value="rupay">Rupay</option>
          <option value="master card">Master Card</option>        
        </select>    
      </p>
      <p>
        Card Number *<input type="number" name="card_number" id="card_number" required="">
      </p>
      <p>
        Expiration Date:* <input type="date" name="exp_date" id="exp_date" required="">
      </p>
      <p>
        Card Verification Value * <input type="password" name="CVV" id="CVV" required="">
      </p>
      <input type="submit" value="Pay Now" />
    </form>
  </body>
</html>
