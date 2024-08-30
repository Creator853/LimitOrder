class LimitOrderAgent:
    def __init__(self, execution_client):
        self.execution_client = execution_client
        self.orders = []

    def add_order(self, side, product_id, amount, limit_price):
        order = {
            'side': side,
            'product_id': product_id,
            'amount': amount,
            'limit_price': limit_price
        }
        self.orders.append(order)

    def price_tick(self, product_id, price):
        for order in self.orders:
            if order['product_id'] == product_id:
                if (order['side'] == 'buy' and price <= order['limit_price']) or \
                   (order['side'] == 'sell' and price >= order['limit_price']):
                    self.execution_client.execute_order(order)
                    self.orders.remove(order)
