def make_readable(segundos):
    hrs,min=0,0
    string_tempo=''
    while (segundos-60)>=0:
        segundos-=60
        min+=1
    while (min-60)>=0:
        min-=60
        hrs+=1
    tempo=[hrs,min,segundos]
    tempo_novo=[]
    for t in tempo:
        
        if t<10:
            tempo_novo.append('0'+ str(t))
        else:
            tempo_novo.append(str(t))
    return ":".join(tempo_novo)
  
  
  #outra forma de resolver 
  
  
  def make_readable(segundos):
    hrs,min,seg=int(segundos/3600),(segundos//60)% 60,segundos % 60 
    tempo=[hrs,min,seg]
    tempo_novo=[]
    for t in tempo:
        
        if t<10:
            tempo_novo.append('0'+ str(t))
        else:
            tempo_novo.append(str(t))
    return ":".join(tempo_novo)
