<?php

class foo_mysqli extends mysqli {
	public function __construct($host, $user, $pass, $db) {
		parent::__construct($host, $user, $pass, $db);

		if (mysqli_connect_error()) {
			die('Connect Error (' . mysqli_connect_errno() . ') '
				. mysqli_connect_error());
		}
	}
}

$db = new foo_mysqli("example.com", "user", "password", "database");

$stmt = $db->prepare("UPDATE product SET description = ? , name = ? WHERE product_id = ?");
// Check whether the prepare() succeeded 
if ($stmt === false) {
	trigger_error($db->error, E_USER_ERROR);
}

 // Assuming the POST paramenters are named the following way.
$stmt->bindParam(1, $_POST['description']);
$stmt->bindParam(2, $_POST['name']); 
$stmt->bindParam(3, $_POST['product_id']);

$status = $stmt->execute();
// Check whether the execute() succeeded 
if ($status === false) {
	trigger_error($stmt->error, E_USER_ERROR);
}

$db->close();
?>