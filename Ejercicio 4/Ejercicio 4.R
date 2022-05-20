conjunto_cartas<-c("A","2","3","4","5","6","7","8","9","10","J","Q","K")
cartas<-c(rep(conjunto_cartas,4))
cartas
Tipos_de_cartas<-c("Corazon", "Diamante", "Trebol", "Espada")
tipos<-c(rep(Tipos_de_cartas,rep(13,4)))
tipos
baraja=data.frame(cartas,tipos)
baraja
