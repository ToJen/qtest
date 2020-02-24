from qiskit import QuantumCircuit
from qiskit import QiskitError, execute, BasicAer
from qiskit.tools.visualization import plot_histogram


sim_backend = BasicAer.get_backend('statevector_simulator')

circ = QuantumCircuit.from_qasm_file("qasm/qft.qasm")
print(circ)

sim_result = execute(circ, sim_backend).result()

probAmpltitudes = sim_result.get_statevector(circ)

print(probAmpltitudes)

