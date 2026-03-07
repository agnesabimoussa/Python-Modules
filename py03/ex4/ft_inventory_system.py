import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    else:
        try:
            inventory = {}
            for arg in sys.argv[1:]:
                if (arg.find(":") == -1):
                    raise Exception("Error in parsing arguments!")
                parts = arg.split(":")
                d = {parts[0]: {"type": "normal",
                            "quantity": int(parts[1]), "value": 0}}
                inventory.update(d)
            total_qty = 0
            for _, v in inventory.items():
                total_qty += v['quantity']
            print(f"Total items in inventory: {total_qty}")
            print(f"Unique item types: {len(inventory.keys())}\n")
            print("=== Current Inventory ===")
            # compute percentage share per item without using non-authorized functions
            for _, v in inventory.items():
                if total_qty > 0:
                    v['value'] = (v['quantity'] * 100) // total_qty
                else:
                    v['value'] = 0
            for k, v in inventory.items():
                print(f"{k}: {v['quantity']} units ({v['value']}%)")
            print("\n=== Inventory Statistics ===")
            # find most/least abundant items without using non-authorized built-ins
            most_name = None
            most_qty = None
            least_name = None
            least_qty = None
            for name, data in inventory.items():
                q = data['quantity']
                if most_qty is None or q > most_qty:
                    most_qty = q
                    most_name = name
                if least_qty is None or q < least_qty:
                    least_qty = q
                    least_name = name
            if most_name is not None:
                print(f"Most abundant: {most_name} ({most_qty} units)")
            if least_name is not None:
                print(f"Least abundant: {least_name} ({least_qty} units)")

        except Exception as e:
            print(e)
