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
    <category name="Operaciones de Valores">
      <category name="Creación">
        <block type="armarValorAs"></block>
        <block type="armarValor_"></block>
        <block type="armarValorSota"></block>
        <block type="armarValorCaballo"></block>
        <block type="armarValorRey"></block>
      </category>
      <category name="Acceso">
        <block type="esMenorValor__"></block>
        <block type="esMayorValor__"></block>
        <block type="valorSiguiente_"></block>
        <block type="valorPrevio_"></block>
        <block type="minValor"></block>
        <block type="maxValor"></block>
      </category>
    </category>
    <category name="Operaciones de Palos">
      <category name="Creación">
        <block type="bastos"></block>
        <block type="copas"></block>
        <block type="espadas"></block>
        <block type="oros"></block>
      </category>
      <category name="Acceso">
        <block type="esMenorPalo__"></block>
        <block type="esMayorPalo__"></block>
        <block type="paloSiguiente_"></block>
        <block type="paloPrevio_"></block>
        <block type="minPalo"></block>
        <block type="maxPalo"></block>
      </category>
    </category>
    <category name="Operaciones de Cartas">
      <category name="Creación">
        <block type="dameCarta__"></block>
        <block type="leerCarta"></block>
      </category>
      <category name="Manipulación">
        <block type="hayCarta"></block>
        <block type="hayCartaTapada"></block>
        <block type="PonerCarta_"></block>
        <block type="SacarCartaActual"></block>
        <block type="DarVueltaLaCartaActual"></block>
      </category>
      <category name="Acceso">
        <block type="dameElPalo_"></block>
        <block type="dameElValor_"></block>
        <block type="esMenorCarta__"></block>
        <block type="esMayorCarta__"></block>
        <block type="cartaSiguiente_"></block>
        <block type="cartaPrevia_"></block>
        <block type="minCarta"></block>
        <block type="maxCarta"></block>
      </category>
    </category>
    <category name="Operaciones de Letras">
      <category name="Creación">
        <block type="letra_"></block>
        <block type="leerLetra"></block>
      </category>
      <category name="Manipulación">
        <block type="PonerLetra_"></block>
        <block type="SacarLetraActual"></block>
        <block type="hayLetra"></block>
      </category>
      <category name="Acceso">
        <block type="esMenorLetra__"></block>
        <block type="esMayorLetra__"></block>
        <block type="letraSiguiente_"></block>
        <block type="letraPrevia_"></block>
        <block type="minLetra"></block>
        <block type="maxLetra"></block>
      </category>
    </category>
    <category name="Mis procedimientos" custom="PROCEDURE_CALLS">  </category>
    <category name="Mis funciones" custom="FUNCTION_CALLS">  </category>
    <category name="Definiciones">
        <block type="procedures_defnoreturn"></block>
        <block type="procedures_defreturnsimplewithparams"></block>
        <block type="procedures_defreturn"></block>
    </category>

