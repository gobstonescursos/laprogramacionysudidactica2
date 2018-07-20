Redactar bien el readme...

1. Copiar aquellos archivos que se desea utilizar
2. Comentar aquellas operaciones de interfaz que no se desea que sean accesibles 
   (las interfaces son la primera sección de cada archivo, indicada claramente con comentarios)
3. Poner todos los archivos resultantes juntos en un archivo extra.gbs en el proyecto 
   (teniendo en cuenta las dependencias indicadas al comienzo de cada archivo)
   Se pueden agregar más operaciones, siempre que no entren en conflicto de nombres
4. Construir la caja de herramientas para GobstonesJr según las operaciones que se desea sean visibles
   Una caja recomendada, con la mayoría de las operaciones necesarias 
    (faltan algunas operaciones básicas: siguiente, previo, opuesto y programas interactivos) 
   es:

    <category name="Comandos básicos">
      <category name="Primitivos">
        <block type="Poner__Veces"></block>
        <block type="Sacar__Veces"></block>
        <block type="Mover__Veces"></block>
        <block type="SacarTodas"></block>
        <block type="SacarTodas_"></block>
        <block type="IrAlBorde"></block>
        <block type="IrAlOrigen"></block>
        <block type="PasarASiguientePosición"></block>
        <block type="BOOM"></block>
      </category>
      <category name="Combinaciones">
        <block type="RepeticionSimple"></block>
        <block type="AlternativaCompleta"></block>
        <block type="RepeticionCondicional"></block>
        <block type="Asignacion"></block>
      </category>
    </category>
    <category name="Expresiones básicas">
      <category name="Primitivos">
        <block type="math_number"></block>
        <block type="ColorSelector"></block>
        <block type="DireccionSelector"></block>
        <block type="nroBolitas"></block>
        <block type="puedeMover"></block>
      </category>
      <category name="Operadores">
        <block type="OperadorNumerico"></block>
        <block type="OperadorDeComparacion"></block>
        <block type="OperadorLogico"></block>
        <block type="not"></block>
      </category>
    </category>
    <category name="Operaciones de Números por Dígitos">
      <category name="Creación">
        <block type="númeroPorDígitosActual"></block>
        <block type="númeroPorDígitosOculto"></block>
      </category>
      <category name="Manipulación">
        <block type="PonerNúmeroPorDígitos_"></block>
        <block type="SacarNúmeroPorDígitosActual"></block>
        <block type="OcultarNúmeroPorDígitosActual"></block>
        <block type="RevelarNúmeroPorDígitosActual"></block>
        <block type="hayNúmeroPorDígitos"></block>
        <block type="hayNúmeroPorDígitosNoOculto"></block>
        <block type="hayNúmeroPorDígitosOculto"></block>
      </category>
    </category>
    <category name="Operaciones de Números">
      <category name="Creación">
        <block type="númeroActual"></block>
        <block type="númeroOculto"></block>
      </category>
      <category name="Manipulación">
        <block type="PonerNúmero_"></block>
        <block type="SacarNúmeroActual"></block>
        <block type="hayNúmero"></block>
        <block type="hayNúmeroNoOculto"></block>
        <block type="hayNúmeroOculto"></block>
        <block type="elNúmeroEstáOculto"></block>
        <block type="OcultarNúmeroActual"></block>
        <block type="RevelarNúmeroActual"></block>
      </category>
    </category>
    <category name="Operaciones de Letras">
      <category name="Creación">
        <block type="letra_"></block>
        <block type="minLetra"></block>
        <block type="maxLetra"></block>
        <block type="letraActual"></block>
        <block type="letraOculta"></block>
      </category>
      <category name="Manipulación">
        <block type="PonerLetra_"></block>
        <block type="SacarLetraActual"></block>
        <block type="OcultarLetraActual"></block>
        <block type="RevelarLetraActual"></block>
        <block type="hayLetra"></block>
        <block type="hayLetraNoOculta"></block>
        <block type="hayLetraOculta"></block>
      </category>
      <category name="Acceso">
        <block type="esMenorLetra__"></block>
        <block type="esMayorLetra__"></block>
        <block type="letraSiguiente_"></block>
        <block type="letraPrevia_"></block>
      </category>
    </category>
    <category name="Operaciones de Palos">
      <category name="Creación">
        <block type="palo_"></block>
        <block type="minPalo"></block>
        <block type="maxPalo"></block>
      </category>
      <category name="Acceso">
        <block type="esMenorPalo__"></block>
        <block type="esMayorPalo__"></block>
        <block type="paloSiguiente_"></block>
        <block type="paloPrevio_"></block>
      </category>
    </category>
    <category name="Operaciones de Valores">
      <category name="Creación">
        <block type="valorDeCartaEspañolaDe40_"></block>
        <block type="minValor"></block>
        <block type="maxValor"></block>
      </category>
      <category name="Acceso">
        <block type="esMenorValor__"></block>
        <block type="esMayorValor__"></block>
        <block type="valorSiguiente_"></block>
        <block type="valorPrevio_"></block>
      </category>
    </category>
    <category name="Operaciones de Cartas">
      <category name="Creación">
        <block type="dameCarta__"></block>
        <block type="minCarta"></block>
        <block type="maxCarta"></block>
        <block type="cartaActual"></block>
        <block type="cartaTapada"></block>
      </category>
      <category name="Manipulación">
        <block type="PonerCarta_"></block>
        <block type="SacarCartaActual"></block>
        <block type="DarVueltaLaCartaActual"></block>
        <block type="hayCarta"></block>
        <block type="hayCartaTapada"></block>
      </category>
      <category name="Acceso">
        <block type="dameElPalo_"></block>
        <block type="dameElValor_"></block>
        <block type="esMenorCarta__"></block>
        <block type="esMayorCarta__"></block>
        <block type="cartaSiguiente_"></block>
        <block type="cartaPrevia_"></block>
      </category>
      <category name="Iluminación">
        <block type="IluminarLaCartaActual"></block>
        <block type="laCartaEstáIluminada"></block>
        <block type="hayCartaDestapadaSinIluminar"></block>
        <block type="hayOtraCartaDestapadaSinIluminar"></block>
      </category>
    </category>
    <category name="Operaciones de Mazos">
      <category name="Creación">
        <block type="mazoVacío"></block>
        <block type="agregarAlFinalDelMazo__"></block>
        <block type="agregarAlPrincipioDelMazo__"></block>
        <block type="juntarMazos__"></block>
        <block type="mazoEspañol"></block>
        <block type="mazoActual"></block>
        <block type="mazoTapado"></block>
      </category>
      <category name="Manipulación">
        <block type="PonerMazo_"></block>
        <block type="SacarMazo"></block>
        <block type="DarVueltaElMazoActual"></block>
      </category>
      <category name="Acceso">
        <block type="quedanCartas_"></block>
        <block type="cantidadDeCartasDelMazo_"></block>
        <block type="dameLaPrimeraCartaDe_"></block>
        <block type="sacarLaPrimeraCartaDe_"></block>
        <block type="dameLaÚltimaCartaDe_"></block>
        <block type="sacarLaÚltimaCartaDe_"></block>
        <block type="dameLaCartaMásGrandeDe_"></block>
        <block type="dameLaCartaMásChicaDe_"></block>
      </category>
    </category>
    <category name="Mis procedimientos" custom="PROCEDURE_CALLS">  </category>
    <category name="Mis funciones" custom="FUNCTION_CALLS">  </category>
    <category name="Definiciones">
        <block type="procedures_defnoreturn"></block>
        <block type="procedures_defreturnsimplewithparams"></block>
        <block type="procedures_defreturn"></block>
    </category>

Otra caja posible, sin las subcategorías:
    
    <category name="Comandos básicos">
        <block type="Poner__Veces"></block>
        <block type="Sacar__Veces"></block>
        <block type="Mover__Veces"></block>
        <block type="SacarTodas"></block>
        <block type="SacarTodas_"></block>
        <block type="IrAlBorde"></block>
        <block type="IrAlOrigen"></block>
        <block type="PasarASiguientePosición"></block>
        <block type="BOOM"></block>
        <block type="RepeticionSimple"></block>
        <block type="AlternativaCompleta"></block>
        <block type="RepeticionCondicional"></block>
        <block type="Asignacion"></block>
    </category>
    <category name="Expresiones básicas">
        <block type="math_number"></block>
        <block type="ColorSelector"></block>
        <block type="DireccionSelector"></block>
        <block type="nroBolitas"></block>
        <block type="puedeMover"></block>
        <block type="OperadorNumerico"></block>
        <block type="OperadorDeComparacion"></block>
        <block type="OperadorLogico"></block>
        <block type="not"></block>
    </category>
    <category name="Operaciones de Números por Dígitos">
        <block type="númeroPorDígitosActual"></block>
        <block type="númeroPorDígitosOculto"></block>
        <block type="PonerNúmeroPorDígitos_"></block>
        <block type="SacarNúmeroPorDígitosActual"></block>
        <block type="OcultarNúmeroPorDígitosActual"></block>
        <block type="RevelarNúmeroPorDígitosActual"></block>
        <block type="hayNúmeroPorDígitos"></block>
        <block type="hayNúmeroPorDígitosNoOculto"></block>
        <block type="hayNúmeroPorDígitosOculto"></block>
    </category>
    <category name="Operaciones de Números">
        <block type="númeroActual"></block>
        <block type="númeroOculto"></block>
        <block type="PonerNúmero_"></block>
        <block type="SacarNúmeroActual"></block>
        <block type="OcultarNúmeroActual"></block>
        <block type="RevelarNúmeroActual"></block>
        <block type="hayNúmero"></block>
        <block type="hayNúmeroNoOculto"></block>
        <block type="hayNúmeroOculto"></block>
    </category>
    <category name="Operaciones de Letras">
        <block type="letra_"></block>
        <block type="minLetra"></block>
        <block type="maxLetra"></block>
        <block type="letraActual"></block>
        <block type="letraOculta"></block>
        <block type="PonerLetra_"></block>
        <block type="SacarLetraActual"></block>
        <block type="OcultarLetraActual"></block>
        <block type="RevelarLetraActual"></block>
        <block type="hayLetra"></block>
        <block type="hayLetraNoOculta"></block>
        <block type="hayLetraOculta"></block>
        <block type="laLetraEstáOculta"></block>
        <block type="esMenorLetra__"></block>
        <block type="esMayorLetra__"></block>
        <block type="letraSiguiente_"></block>
        <block type="letraPrevia_"></block>
    </category>
    <category name="Operaciones de Palos">
        <block type="palo_"></block>
        <block type="minPalo"></block>
        <block type="maxPalo"></block>
        <block type="esMenorPalo__"></block>
        <block type="esMayorPalo__"></block>
        <block type="paloSiguiente_"></block>
        <block type="paloPrevio_"></block>
    </category>
    <category name="Operaciones de Valores">
        <block type="valorDeCartaEspañolaDe40_"></block>
        <block type="minValor"></block>
        <block type="maxValor"></block>
        <block type="esMenorValor__"></block>
        <block type="esMayorValor__"></block>
        <block type="valorSiguiente_"></block>
        <block type="valorPrevio_"></block>
    </category>
    <category name="Operaciones de Cartas">
        <block type="dameCarta__"></block>
        <block type="minCarta"></block>
        <block type="maxCarta"></block>
        <block type="cartaActual"></block>
        <block type="cartaTapada"></block>
        <block type="PonerCarta_"></block>
        <block type="SacarCartaActual"></block>
        <block type="DarVueltaLaCartaActual"></block>
        <block type="hayCarta"></block>
        <block type="hayCartaTapada"></block>
        <block type="dameElPalo_"></block>
        <block type="dameElValor_"></block>
        <block type="esMenorCarta__"></block>
        <block type="esMayorCarta__"></block>
        <block type="cartaSiguiente_"></block>
        <block type="cartaPrevia_"></block>
        <block type="IluminarLaCartaActual"></block>
        <block type="laCartaEstáIluminada"></block>
        <block type="hayCartaDestapadaSinIluminar"></block>
        <block type="hayOtraCartaDestapadaSinIluminar"></block>
    </category>
    <category name="Operaciones de Mazos">
        <block type="mazoVacío"></block>
        <block type="agregarAlFinalDelMazo__"></block>
        <block type="agregarAlPrincipioDelMazo__"></block>
        <block type="juntarMazos__"></block>
        <block type="mazoEspañol"></block>
        <block type="mazoActual"></block>
        <block type="mazoTapado"></block>
        <block type="PonerMazo_"></block>
        <block type="SacarMazoActual"></block>
        <block type="DarVueltaElMazoActual"></block>
        <block type="quedanCartas_"></block>
        <block type="cantidadDeCartasDelMazo_"></block>
        <block type="dameLaPrimeraCartaDe_"></block>
        <block type="sacarLaPrimeraCartaDe_"></block>
        <block type="dameLaÚltimaCartaDe_"></block>
        <block type="sacarLaÚltimaCartaDe_"></block>
        <block type="dameLaCartaMásGrandeDe_"></block>
        <block type="dameLaCartaMásChicaDe_"></block>
    </category>
    <category name="Mis procedimientos" custom="PROCEDURE_CALLS">  </category>
    <category name="Mis funciones" custom="FUNCTION_CALLS">  </category>
    <category name="Definiciones">
        <block type="procedures_defnoreturn"></block>
        <block type="procedures_defreturnsimplewithparams"></block>
        <block type="procedures_defreturn"></block>
    </category>
