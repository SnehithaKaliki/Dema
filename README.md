###Steps to run the application:
Open command prompt, navigate to project folder and run the following command.

python demaai.py


Open your browser or use a tool like curl to test the endpoints:

List Inventory: http://localhost:5000/list_inventory
Update Inventory (Example for product_id=1): http://localhost:5000/update_inventory/1



###Update inventory:

Product ID used to create endpoint for updating inventory.

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
