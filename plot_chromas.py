import jams
import mir_eval
import numpy as np
import matplotlib.pyplot as plt

# create chroma from chord label
def labchroma(l):
    r,c,b = mir_eval.chord.encode(l)
    return np.roll(c,r)

# plot the chromas of the annotators of song s
def plotchroma(s):
    jam = jams.load('jams/' + str(s) + '.jams')

    nannotations = len(jam['annotations'])
    f, axarr = plt.subplots(nannotations, sharex=False, sharey=True, figsize=(10, 5))
    for (ann, ax) in zip(jam['annotations'],axarr):
        chroma = np.array([labchroma(lab.value) for lab in ann.data])
        im = ax.matshow(chroma.T, aspect='auto', cmap=plt.cm.Blues)
        ax.set_ylabel(ann.annotation_metadata.annotator.id)
        ax.get_yaxis().set_ticks([])
    f.tight_layout()
    fname = 'img/' + str(s) + '_chroma.png'
    plt.savefig(fname, bbox_inches='tight')
    plt.close()
    print (fname + ' saved.')

# Example for readme
plotchroma(92)
