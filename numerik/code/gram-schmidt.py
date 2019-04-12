def gram-schmidt(v):
  (n,m) = v.shape # n vectors with m coefficients
  for j in range(n):
    delta = np.zeros(m)
    for i in range(j-1):
      r = sprod(v[j,:],v[i,:])
      delta += r*v[i,:]
    v[j,:] -= delta
    norm = np.sqrt(sprod(v[j,:],v[j,:]))
    v[j,:] /= norm
