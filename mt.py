import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, ipv4_address):
        self.ipv4_address = ipv4_address
        self.tape = []
        self.head_position = 0
        self.current_state = 'START'
        self.result = None

    def convert_ipv4_to_ipv6_hybrid(self):
        self.tape = list(self.ipv4_address)
        while self.current_state != 'HALT':
            self.step()
        return self.result

    def step(self):
        if self.current_state == 'START':
            if self.validate_ipv4():
                self.current_state = 'CONVERT'
            else:
                self.current_state = 'ERROR'

        elif self.current_state == 'CONVERT':
            ipv6_hybrid = self.ipv4_to_ipv6_hybrid()
            self.result = ipv6_hybrid
            self.current_state = 'HALT'

        elif self.current_state == 'ERROR':
            self.result = None
            self.current_state = 'HALT'

    def validate_ipv4(self):
        octets = self.ipv4_address.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit() or not 0 <= int(octet) <= 255:
                return False
        return True

    def ipv4_to_ipv6_hybrid(self):
        return f"::ffff:{self.ipv4_address}"

class IPv4ToIPv6ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor IPv4 a IPv6 Híbrido")
        root.geometry("400x200")

        # Etiqueta de entrada
        self.label = tk.Label(root, text="Ingrese la dirección IPv4:")
        self.label.pack(pady=10)

        # Campo de entrada de texto
        self.entry = tk.Entry(root, width=20)
        self.entry.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convertir", command=self.convert_ipv4_to_ipv6)
        self.convert_button.pack(pady=10)

        self.output_label = tk.Label(root, text="Dirección IPv6 (híbrida):", font=("Arial", 12))
        self.output_label.pack(pady=10)
        self.output = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.output.pack()

    def convert_ipv4_to_ipv6(self):
        ipv4_address = self.entry.get().strip()
        machine = TuringMachine(ipv4_address)
        ipv6_address = machine.convert_ipv4_to_ipv6_hybrid()

        if ipv6_address:
            self.output.config(text=ipv6_address)
        else:
            messagebox.showerror("Error", "Dirección IPv4 inválida. Por favor, ingrese una dirección válida.")

root = tk.Tk()
app = IPv4ToIPv6ConverterApp(root)
root.mainloop()
