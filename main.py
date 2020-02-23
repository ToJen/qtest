from qiskit import QuantumCircuit
from qiskit import QiskitError, execute, BasicAer
from qiskit.tools.visualization import plot_histogram
# from qiskit.providers.aer.noise import NoiseModel

sim_backend = BasicAer.get_backend('qasm_simulator')
# noise_model = NoiseModel.from_backend(sim_backend)

circ = QuantumCircuit.from_qasm_file("qasm/qft.qasm")
circ.draw(output='mpl')

job_sim = execute(circ, sim_backend)
sim_result = job_sim.result()

counts = sim_result.get_counts(circ)
print(counts)
print(plot_histogram(counts))

