function  leerCarta()                 { return(aux_leerCartaEspañola())       }

// Nivel 1
function aux_leerCartaEspañola() {
  // PRECONDICIÓN: hay una carta destapada en la celda actual
  if (not aux_hayCartaEspañola())      { BOOM("No hay una carta española que pueda leer") }
  if (aux_laCartaEspañolaEstáTapada()) { BOOM("No puedo leer una carta española tapada")  }
  return(aux_cartaEspañolaParaElCódigo(aux_leerDato()))
}         

// Nivel 2
function aux_hayCartaEspañola() { return (aux_hayTipoCartaEspañola() && aux_hayDatoCartaEspañola()) }

function aux_laCartaEspañolaEstáTapada() { 
  // PRECONDICIÓN: hay una carta española
  return (aux_hayAtributoReverso())
}

function aux_cartaEspañolaParaElCódigo(códigoCarta) {
  // PRECONDICIÓN: el códigoDatoCarta corresponde a los de una carta válida
  if (not aux_esCódigoParaLaCartaEspañola(códigoCarta)) { BOOM("No es un código de carta válido") }
  let (códigoValor, códigoPalo) := aux_analizarDatoCarta(códigoCarta)
  return(choose
           aux_armarComodín()                                    when (aux_esCódigoParaElComodín(códigoPalo))
           aux_armarCartaEspañola(
               aux_valorDeCartaEspañolaParaElCódigo(códigoValor)
              ,aux_paloDeCartaEspañolaParaElCódigo(códigoPalo))  otherwise
  )
}

// NIVEL 3
function aux_hayTipoCartaEspañola() { return (aux_esTipoCartaEspañola(aux_leerTipo())) }
function aux_hayDatoCartaEspañola() { return (aux_esDatoCartaEspañola(aux_leerDato())) }

function  aux_hayAtributoReverso()  { return (nroBolitas(aux_colorParaElAtributo())==aux_códigoParaElAtributoReverso()) }

function aux_esCódigoParaLaCartaEspañola(códigoCartaEspañola) {
  let (códigoValor, códigoPalo) := aux_analizarDatoCarta(códigoCartaEspañola)
  return (aux_sonValorYPaloDeCartaEspañola(códigoValor, códigoPalo))
}

function aux_analizarDatoCarta(códigoCartaEspañola) {
  return (códigoCartaEspañola mod 100, códigoCartaEspañola div 100)
}



// NIVEL 4
function aux_esTipoCartaEspañola(código) { return (código == aux_códigoParaElTipoCartaEspañola()) }
function aux_esDatoCartaEspañola(dato)   { return (aux_esCódigoParaLaCartaEspañola(dato)) }

function  aux_códigoParaElAtributoReverso() { return(1) }
