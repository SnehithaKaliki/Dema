Problem Description:
At Dema, e-commerce platforms and tooling are at the core, and we are developing a functionality centered around them. The goal is to build an inventory service that provides an overview of the current inventory, products sold, and the ability to update inventory.

Preface:
Create a backend service using a web framework of your choice within the Python ecosystem. For storing and managing data in the service, feel free to use any SQL/NoSQL databases. We will utilize two datasets (for database seeding) to query and modify data:

Orders Dataset: Contains orders made on the e-commerce platform. (orders.csv)
Inventory Dataset: Contains inventory information, including product descriptions and their available quantities. (Inventory.csv)
Requirements:
List Inventory:

An endpoint/query to list inventory on the store.
It returns a list of all products, with each item containing information about the product and orders placed on that product.
This list endpoint should support pagination for querying data.
Update Inventory:

An endpoint/mutation to update the product information and available quantity for a particular product.
It should return the updated product and its order data.
Steps to run the application:
Open the command prompt, navigate to the project folder, and run the following command:

Copy code
python demaai.py
Open your browser or use a tool like curl to test the endpoints:

List Inventory: http://localhost:5000/list_inventory
Update Inventory (Example for product_id=1): http://localhost:5000/update_inventory/1
Update inventory:
The product ID is used to create an endpoint for updating inventory. Since the Product ID may contain special characters, for a simple update request, Invoke-RestMethod is used in the following example. If the product ID is not found/invalid, it returns error 404.

Example:
Open PowerShell in Windows and run the following lines:

powershell
Copy code
$productId = 'prod3214#prod117021007065'
$encodedProductId = [uri]::EscapeDataString($productId)
$url = "http://localhost:5000/update_inventory/$encodedProductId"
Invoke-RestMethod -Method Put -Uri $url -Headers @{"Content-Type"="application/json"} -Body '{"new_quantity": 1000}'
Output:
name	product_id	quantity
Leather belt	prod3214#prod117021007065	1000
