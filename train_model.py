import DAE

dae=DAE.DAE(32)
dae.initModel()
# dae.loadModel()
dae.train(0.0001,0.5,100000)
dae.close()