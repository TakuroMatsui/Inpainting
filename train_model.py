import DAE

dae=DAE.DAE(10)
# dae.loadModel()
dae.train(0.001,0.5,100000)
dae.close()