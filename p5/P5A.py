import matplotlib.pyplot as plt
import plonk

# Load the snapshot

snap = plonk.load_snap('data/disc_00000.h5')

y=snap.available_arrays()
print(y)

gas = snap['gas']

fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(12, 5))

plonk.visualize.plot(
    snap=gas,
    quantity='density',
    interp='cross_section',
    z_slice=2.5,
    extent=(-120, 120, -120, 120),
    cmap='coolwarm',
    ax=axs[0],
 )

plonk.visualize.plot(
    snap=gas,
    quantity='velocity',
    interp='cross_section',
    z_slice=2.5,
    extent=(-120, 120, -120, 120),
    cmap='coolwarm',
    ax=axs[1],
 )
fig.savefig("Denisty and Velocity of Cough")
plt.show()