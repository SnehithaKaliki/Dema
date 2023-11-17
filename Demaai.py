from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demaai.db'  # SQLite for simplicity
db = SQLAlchemy(app)

# Define Order and Inventory models
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create List Inventory endpoint
@app.route('/list_inventory', methods=['GET'])

def list_inventory():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)

    inventory = Inventory.query.paginate(page, per_page, error_out=False)

    result = []
    for item in inventory.items:
        orders = Order.query.filter_by(product_id=item.product_id).all()
        result.append({
            'product_id': item.product_id,
            'name': item.name,
            'quantity': item.quantity,
            'orders': [{'order_id': order.id, 'quantity': order.quantity} for order in orders]
        })

    return jsonify({'inventory': result, 'total_pages': inventory.pages})

# Create Update Inventory endpoint
@app.route('/update_inventory/<string:product_id>', methods=['PUT'])

def update_inventory(product_id):
    # Extract the new quantity from the request data
    new_quantity = request.json.get('new_quantity')

    # Retrieve the inventory item by product_id
    inventory_item = Inventory.query.filter_by(product_id=product_id).first()

    # Check if the inventory item exists
    if not inventory_item:
        return jsonify({'error': f'Product with ID {product_id} not found'}), 404

    # Update the quantity
    inventory_item.quantity = new_quantity

    # Commit the changes to the database
    db.session.commit()

    # Retrieve the updated inventory item
    updated_inventory_item = Inventory.query.filter_by(product_id=product_id).first()

    # Return the updated inventory item as JSON response
    return jsonify({
        'product_id': updated_inventory_item.product_id,
        'name': updated_inventory_item.name,
        'quantity': updated_inventory_item.quantity
    })
    
# Create a function to seed data
def load_data():
    import csv

    # Seed orders from orders.csv
    with open('orders.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            order = Order(product_id=(row[1]), quantity=int(row[3]))
            db.session.add(order)

    # Seed inventory from inventory.csv
    with open('inventory.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            inventory_item = Inventory(product_id=(row[0]), name=row[1], quantity=int(row[2]))
            db.session.add(inventory_item)

    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    load_data()
    app.run(debug=True)
