
import xdis.std as dis

# aritmatika
kode = """
a = 10
b = 3
hasil = (a * 5) + (b ** 2) - (100 / 4)
"""
bytecode = dis.Bytecode(kode)

print("=== Bytecode Analisis ===")
print("OPCODE              ARGUMENT")
print("----------------------------")
for instr in bytecode:
    print("{:<20} {}".format(
        instr.opname,
        instr.argval if instr.argval else ''
    ))

# Eksekusi kode untuk melihat hasilnya
print("\n=== Hasil Eksekusi ===")
exec(kode)
print("hasil =", hasil)  # Output
