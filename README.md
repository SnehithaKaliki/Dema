
###Problem Description:

At Dema, e-commerce platforms and tooling are at the core and we will build one of the
functionalities around them. We will be building an inventory service, which will give an overview
of how the current inventory looks and products sold, and ability to update inventory.
Preface
1. Create a backend service using a web framework of your choice, based on the Python ecosystem.
2. For storing and managing data in the service, it’s open to use any of SQL/NoSQL databases.
3. We will be using two datasets (for database seeding) to query the data from and make changes to.
4. Orders Dataset: Contains orders done on the e-commerce platform. (orders.csv)
5. Inventory Dataset: Contains inventory information, including products description and their available quantities. (Inventory.csv)

Requirements
1. List Inventory: An endpoint/query to list inventory on the store. It returns a list of all products, each item in the list containing information about the product and orders placed on that product. This list endpoint should support pagination for querying data.
2. Update Inventory: An endpoint/mutation to update the product information and available quantity for a particular product. It should return the updated product and its order data.

###Steps to run the application:
Open command prompt, navigate to project folder and run the following command.

python demaai.py


Open your browser or use a tool like curl to test the endpoints:

List Inventory: http://localhost:5000/list_inventory
Update Inventory (Example for product_id=1): http://localhost:5000/update_inventory/1



###Update inventory:

Product ID used to to create endpoint for updating inventory.

Since, Product ID contains special characters, for simple update request, I have used Invoke-RestMethod to update the inventory in the following example.
If the product ID not found/invalid, returns error 404

Example:
Open PowerShell in Windows and run the following lines. 

$productId = 'prod3214#prod117021007065'
$encodedProductId = [uri]::EscapeDataString($productId)
$url = "http://localhost:5000/update_inventory/$encodedProductId"
Invoke-RestMethod -Method Put -Uri $url -Headers @{"Content-Type"="application/json"} -Body '{"new_quantity": 1000}'



####Output:

name         product_id                quantity
----         ----------                --------
Leather belt prod3214#prod117021007065     1000
