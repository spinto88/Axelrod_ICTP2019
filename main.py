from axelrod_py import *
import matplotlib.pyplot as plt

N = 1024
F = 10
q = 30

rand.seed(123454)

mysys = Axl_network(n = N, f = F, q = q, phi = 0.01, topology = 'lattice')

fig = plt.figure()

plt.ion()
for i in range(200):
	mysys.evolution(25)
	mysys.lattice_image(fig)
plt.ioff()

print 'Biggest fragment size {}'.format(mysys.biggest_fragment()['size'])

label = mysys.biggest_fragment()['label']

print 'Biggest fragment state ', 
print mysys.agent[label].feat[:F]

print 'Mass Media state ',
print mysys.mass_media.feat[:F]

mysys.save_fragments_distribution('frag.dat')
