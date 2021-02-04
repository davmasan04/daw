# coding=utf8
from flask import Flask,render_template,jsonify, Response
from flask_cors import CORS, cross_origin
import dicttoxml

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/anuncios/json')
@cross_origin()
def json():
	anuncios = [{
	    'tipo': "Asistencia",
	    'titulo': "Niñera",
	    'texto': "Saldremos por el fin de semana y necesitamos una niñera para que cuide los 3 niños (6,7 y 8 años)",
	    'fecha': '03-June-2019',
	    'barrio': "Sauces 8"
	  },
	  {
	    'tipo': "Servicio",
	    'titulo': "Mecánico",
	    'texto': "Electromecánico a su casa",
	    'fecha': '02-June-2019',
	    'barrio': "La Saiba"
	  },
	  {
	    'tipo': "Eventos",
	    'titulo': "Fiesta",
	    'texto': "Este sábado 15 de Junio celebraré mis quinceaños. Todos son bienvenidos. Regalo en sobre cerrado.",
	    'fecha': '01-June-2019',
	    'barrio': "Primavera 2"
	  },
	  {
	    'tipo': "Servicio",
	    'titulo': "Limpieza",
	    'texto': "Servicio bueno, confiable y barato.",
	    'fecha': '25-March-2019',
	    'barrio': "La Saiba"
	  }]

	return jsonify({'anuncios': [anuncio for anuncio in anuncios]}) 

@app.route('/escritores', defaults={'type': 'json'})
@app.route('/escritores/<type>')
@cross_origin()
def escritores(type):

	lstEscritores =[{'id': 42, 'nombre': 'Miguel de Cervantes.'}, {'id': 157, 'nombre': 'Mark Twain.'}, {'id': 86, 'nombre': 'Goethe.'}, {'id': 21, 'nombre': 'Baltasar Gracián.'}, {'id': 149, 'nombre': 'Victor Hugo.'}, {'id': 20, 'nombre': 'José Ortega y Gasset.'}, {'id': 142, 'nombre': 'Friedrich Nietzsche.'}, {'id': 11, 'nombre': 'Francisco de Quevedo.'}, {'id': 13, 'nombre': 'William Shakespeare.'}, {'id': 14, 'nombre': 'Voltaire.'}, {'id': 16, 'nombre': 'Dante Alighieri.'}, {'id': 19, 'nombre': 'Gustavo Adolfo Bécquer.'}, {'id': 44, 'nombre': 'Cicerón.'}, {'id': 24, 'nombre': 'Mario Benedetti.'}, {'id': 26, 'nombre': 'Jorge Bucay.'}, {'id': 28, 'nombre': 'Richard Bach.'}, {'id': 30, 'nombre': 'Pedro Calderón de la Barca.'}, {'id': 139, 'nombre': 'Albert Camus.'}, {'id': 34, 'nombre': 'Truman Capote.'}, {'id': 36, 'nombre': 'Dale Carnegie.'}, {'id': 38, 'nombre': 'Lewis Carroll.'}, {'id': 40, 'nombre': 'Camilo José Cela.'}, {'id': 43, 'nombre': 'Noam Chomsky.'}, {'id': 45, 'nombre': 'René Descartes.'}, {'id': 151, 'nombre': 'Charles Dickens.'}, {'id': 47, 'nombre': 'Fiodor Dostoievski.'}, {'id': 48, 'nombre': 'Wayne W. Dyer.'}, {'id': 49, 'nombre': 'Umberto Eco.'}, {'id': 50, 'nombre': 'Emerson.'}, {'id': 174, 'nombre': 'Gustave Flaubert.'}, {'id': 52, 'nombre': 'Anatole France.'}, {'id': 53, 'nombre': 'Viktor Frankl.'}, {'id': 54, 'nombre': 'Sigmund Freud.'}, {'id': 55, 'nombre': 'Eduardo Galeano.'}, {'id': 56, 'nombre': 'Gabriel García Márquez.'}, {'id': 57, 'nombre': 'Friedrich Hegel.'}, {'id': 58, 'nombre': 'Aldous Huxley.'}, {'id': 59, 'nombre': 'John Irving.'}, {'id': 60, 'nombre': 'Franz Kafka.'}, {'id': 61, 'nombre': 'Antonio Machado.'}, {'id': 62, 'nombre': 'Marco Aurelio.'}, {'id': 63, 'nombre': 'Karl Marx.'}, {'id': 64, 'nombre': 'George Orwell.'}, {'id': 112, 'nombre': 'Henry David Thoreau.'}, {'id': 66, 'nombre': 'J. R. R. Tolkien.'}, {'id': 67, 'nombre': 'Leon Tolstoi.'}, {'id': 68, 'nombre': 'Miguel de Unamuno.'}, {'id': 106, 'nombre': 'Mario Vargas Llosa.'}, {'id': 70, 'nombre': 'Lope de Vega.'}, {'id': 160, 'nombre': 'Oscar Wilde.'}, {'id': 72, 'nombre': 'María Zambrano.'}, {'id': 73, 'nombre': 'Arturo Pérez Reverte.'}, {'id': 74, 'nombre': 'Platón.'}, {'id': 75, 'nombre': 'Karl Popper.'}, {'id': 76, 'nombre': 'Alexander Pope.'}, {'id': 77, 'nombre': 'Mario Puzo.'}, {'id': 78, 'nombre': 'Fernando de Rojas.'}, {'id': 79, 'nombre': 'Jean Jacques Rousseau.'}, {'id': 80, 'nombre': 'Marqués de Sade.'}, {'id': 81, 'nombre': 'Antoine de Saint'}, {'id': 82, 'nombre': 'José Luis Sampedro.'}, {'id': 83, 'nombre': 'Santa Teresa de Jesús.'}, {'id': 84, 'nombre': 'Fernando Savater.'}, {'id': 85, 'nombre': 'Jean Paul Sartre.'}, {'id': 105, 'nombre': 'Federico García Lorca.'}, {'id': 88, 'nombre': 'Carlos Ruiz Zafón.'}, {'id': 90, 'nombre': 'Alejandro Dumas.'}, {'id': 91, 'nombre': 'Eduardo Mendoza.'}, {'id': 92, 'nombre': 'Ana Frank.'}, {'id': 121, 'nombre': 'Isaac Asimov.'}, {'id': 134, 'nombre': 'Robert L. Stevenson.'}, {'id': 96, 'nombre': 'Azorín.'}, {'id': 97, 'nombre': 'Cesare Pavese.'}, {'id': 99, 'nombre': 'Julio Cortázar'}, {'id': 147, 'nombre': 'Fyodor Dostoyevsky.'}, {'id': 102, 'nombre': 'Fyodor Dostoyevsky'}, {'id': 152, 'nombre': 'Ernest Hemingway.'}, {'id': 109, 'nombre': 'Somerset Maugham.'}, {'id': 110, 'nombre': 'Herman Melville.'}, {'id': 111, 'nombre': 'C. J. Cherryh.'}, {'id': 164, 'nombre': 'Ray Bradbury.'}, {'id': 114, 'nombre': 'Willa Cather.'}, {'id': 115, 'nombre': 'Ayn Rand.'}, {'id': 116, 'nombre': 'Joseph Conrad.'}, {'id': 117, 'nombre': 'Philip K. Dick.'}, {'id': 118, 'nombre': 'E. L. Doctorow.'}, {'id': 122, 'nombre': 'William Faulkner.'}, {'id': 120, 'nombre': 'Robert Graves.'}, {'id': 123, 'nombre': 'Henry Miller.'}, {'id': 124, 'nombre': 'Ursula K. Le Guin.'}, {'id': 125, 'nombre': 'Nancy Kress.'}, {'id': 126, 'nombre': 'Henry Wadsworth Longfellow.'}, {'id': 127, 'nombre': 'Elmore Leonard.'}, {'id': 128, 'nombre': 'Madeleine L’Engle.'}, {'id': 129, 'nombre': 'Anais Nin.'}, {'id': 170, 'nombre': 'Stephen King.'}, {'id': 131, 'nombre': 'Toni Morrison.'}, {'id': 132, 'nombre': 'Saul Bellow.'}, {'id': 135, 'nombre': 'C. S. Lewis.'}, {'id': 136, 'nombre': 'Margaret Atwood.'}, {'id': 137, 'nombre': 'Virginia Woolf.'}, {'id': 138, 'nombre': 'Charles Baudelaire.'}, {'id': 140, 'nombre': 'John Steinbeck.'}, {'id': 143, 'nombre': 'Natalie Goldberg.'}, {'id': 144, 'nombre': 'Ralph Waldo Emerson.'}, {'id': 145, 'nombre': 'Napoleón Hill.'}, {'id': 146, 'nombre': 'Maya Angelou.'}, {'id': 148, 'nombre': 'Emily Dickinson.'}, {'id': 150, 'nombre': 'William Wordsworth.'}, {'id': 153, 'nombre': 'George R. R. Martin.'}, {'id': 154, 'nombre': 'J. K. Rowling.'}, {'id': 155, 'nombre': 'Jack London.'}, {'id': 156, 'nombre': 'Khaled Hosseini.'}, {'id': 161, 'nombre': 'Thomas Mann.'}, {'id': 162, 'nombre': 'E. B. White.'}, {'id': 163, 'nombre': 'Jorge Luis Borges.'}, {'id': 165, 'nombre': 'Cornelia Funke.'}, {'id': 166, 'nombre': 'Muriel Rukeyser.'}, {'id': 167, 'nombre': 'Lisa See.'}, {'id': 169, 'nombre': 'Tom Bissell.'}, {'id': 171, 'nombre': 'Natsuki Takaya.'}, {'id': 172, 'nombre': 'William Saroyan.'}, {'id': 173, 'nombre': 'Epictetus.'}, {'id': 175, 'nombre': 'Friedrich Nietzche.'}, {'id': 176, 'nombre': 'Stephen Chbosky.'}, {'id': 177, 'nombre': 'Bil Keane.'}]
	
	obj = {
        'escritores': lstEscritores
    }

	if type == "xml":
		xml = dicttoxml.dicttoxml(lstEscritores,item_func=lambda x: 'escritor',custom_root='escritores',attr_type=False)
		return Response(xml, mimetype='text/xml')

	return jsonify(obj)

@app.route('/escritores/frases', defaults={'type': 'json'})
@app.route('/escritores/frases/<type>')
@cross_origin()
def frases(type):

	lstFrases = [{'id_autor': 42, 'texto': 'El que lee mucho y anda mucho, ve mucho y sabe mucho.'}, {'id_autor': 42, 'texto': 'Más vale la pena en el rostro que la mancha en el corazón.'}, {'id_autor': 42, 'texto': 'Confía en el tiempo, que suele dar dulces salidas a muchas amargas dificultades.'}, {'id_autor': 42, 'texto': 'La senda de la virtud es muy estrecha y el camino del vicio, ancho y espacioso.'}, {'id_autor': 157, 'texto': 'Escribir es fácil. Lo único que tienes que hacer es cruzar las palabras erróneas.'}, {'id_autor': 157, 'texto': 'Un libro no es exitoso por lo que hay dentro de él, sino por lo que deja afuera.'}, {'id_autor': 86, 'texto': 'Cierto que en el mundo de los hombres nada hay necesario, excepto el amor.'}, {'id_autor': 86, 'texto': 'No basta con saber, se debe también aplicar. No es suficiente querer, se debe también hacer.'}, {'id_autor': 86, 'texto': 'Ambición y amor son las alas de las grandes acciones.'}, {'id_autor': 21, 'texto': 'El primer paso de la ignorancia es presumir de saber.'}, {'id_autor': 21, 'texto': 'Todo lo que realmente nos pertenece es el tiempo; incluso el que no tiene nada más, lo posee.'}, {'id_autor': 149, 'texto': 'El futuro tiene muchos nombres. Para los débiles es lo inalcanzable. Para los temerosos, lo desconocido. Para los valientes es la oportunidad.'}, {'id_autor': 149, 'texto': 'Atreveos: el progreso solamente se logra así.'}, {'id_autor': 149, 'texto': 'Un escritor es un mundo atrapado en una persona.'}, {'id_autor': 20, 'texto': 'La vida es una serie de colisiones con el futuro; no es una suma de lo que hemos sido, sino de lo que anhelamos ser.'}, {'id_autor': 20, 'texto': 'Nuestras convicciones más arraigadas, más indubitables, son las más sospechosas. Ellas constituyen nuestro límite, nuestros confines, nuestra prisión.'}, {'id_autor': 142, 'texto': 'Los monos son demasiado buenos para que el hombre pueda descender de ellos.'}, {'id_autor': 142, 'texto': 'Aquel que tiene un porqué para vivir se puede enfrentar a todos los «cómos».'}, {'id_autor': 142, 'texto': 'Un buen escritor no posee solo su propio espíritu, sino también el espíritu de sus amigos.'}, {'id_autor': 11, 'texto': 'El que quiere de esta vida todas las cosas a su gusto, tendrá muchos disgustos.'}, {'id_autor': 11, 'texto': 'El valiente tiene miedo del contrario; el cobarde, de su propio temor.'}, {'id_autor': 13, 'texto': 'Es mejor ser rey de tu silencio que esclavo de tus palabras.'}, {'id_autor': 13, 'texto': 'El sabio no se sienta para lamentarse, sino que se pone alegremente a su tarea de reparar el daño hecho.'}, {'id_autor': 14, 'texto': 'Buscamos la felicidad, pero sin saber dónde, como los borrachos buscan su casa, sabiendo que tienen una.'}, {'id_autor': 16, 'texto': 'La raza humana se encuentra en la mejor situación cuando posee el más alto grado de libertad.'}, {'id_autor': 16, 'texto': 'Quien sabe de dolor, todo lo sabe.'}, {'id_autor': 19, 'texto': 'El alma que hablar puede con los ojos, también puede besar con la mirada.'}, {'id_autor': 19, 'texto': 'El que tiene imaginación, con qué facilidad saca de la nada un mundo.'}, {'id_autor': 44, 'texto': 'Si hacemos el bien por interés, seremos astutos, pero nunca buenos.'}, {'id_autor': 44, 'texto': 'Los hombres son como los vinos: la edad agria los malos y mejora los buenos.'}, {'id_autor': 24, 'texto': 'Acá hay tres clases de gente: las que se matan trabajando, las que deberían trabajar y las que tendrían que matarse.'}, {'id_autor': 24, 'texto': 'Cuando creíamos que teníamos todas las respuestas, de pronto, cambiaron todas las preguntas.'}, {'id_autor': 26, 'texto': 'El verdadero amor no es otra cosa que el deseo inevitable de ayudar al otro para que sea quien es.'}, {'id_autor': 26, 'texto': 'El verdadero buscador crece y aprende, y descubre que siempre es el principal responsable de lo que sucede.'}, {'id_autor': 28, 'texto': 'El vínculo que une a tu auténtica familia no es de sangre, sino de respeto y alegría mutua.'}, {'id_autor': 28, 'texto': 'Si tu felicidad depende de lo que hagan los demás, supongo que estarás en aprietos.'}, {'id_autor': 30, 'texto': 'Afortunado es el hombre que tiene tiempo para esperar.'}, {'id_autor': 30, 'texto': 'Vencerse a sí mismo es tan gran hazaña, que sólo el que es grande puede atreverse a ejecutarla.'}, {'id_autor': 139, 'texto': 'Puede que lo que hacemos no traiga siempre la felicidad, pero si no hacemos nada, no habrá felicidad.'}, {'id_autor': 139, 'texto': 'No camines delante de mí, puede que no te siga. No camines detrás de mí, puede que no te guíe. Camina junto a mí y sé mi amigo.'}, {'id_autor': 139, 'texto': 'No ser amado es una simple desventura. La verdadera desgracia es no saber amar.'}, {'id_autor': 139, 'texto': 'El propósito de un escritor es evitar que la civilización se destruya así misma.'}, {'id_autor': 34, 'texto': 'La disciplina es la parte más importante del éxito.'}, {'id_autor': 34, 'texto': 'Todo fracaso es el condimento que da sabor al éxito.'}, {'id_autor': 36, 'texto': 'Acepta los riesgos, toda la vida no es sino una oportunidad. El hombre que llega más lejos es, generalmente, el que quiere y se atreve a serlo.'}, {'id_autor': 36, 'texto': 'Encuéntrate y sé tú mismo; recuerda que no hay nadie como tú.'}, {'id_autor': 38, 'texto': 'Uno de los secretos profundos de la vida es que lo único que merece la pena hacer es lo que hacemos por los demás.'}, {'id_autor': 38, 'texto': 'Puedes llegar a cualquier parte, siempre que andes lo suficiente.'}, {'id_autor': 40, 'texto': 'Lo malo de los que se creen en posesión de la verdad es que cuando tienen que demostrarlo no aciertan ni una.'}, {'id_autor': 40, 'texto': 'La más noble función de un escritor es dar testimonio, como acta notarial y como fiel cronista, del tiempo que le ha tocado vivir.'}, {'id_autor': 43, 'texto': 'El verdadero problema del mundo es cómo impedir que salte por los aires.'}, {'id_autor': 45, 'texto': 'Daría todo lo que sé, por la mitad de lo que ignoro.'}, {'id_autor': 151, 'texto': 'El corazón humano es un instrumento de muchas cuerdas; el perfecto conocedor de los hombres las sabe hacer vibrar todas, como un buen músico.'}, {'id_autor': 151, 'texto': 'Una idea, como un fantasma, debe ser expuesta un poco antes de ser explicada.'}, {'id_autor': 47, 'texto': 'El secreto de la existencia no consiste solamente en vivir, sino en saber para qué se vive.'}, {'id_autor': 48, 'texto': 'Si crees totalmente en ti mismo, no habrá nada que esté fuera de tus posibilidades.'}, {'id_autor': 49, 'texto': 'Nada es más nocivo para la creatividad que el furor de la inspiración.'}, {'id_autor': 50, 'texto': 'El éxito consiste en obtener lo que se desea. La felicidad, en disfrutar lo que se obtiene.'}, {'id_autor': 174, 'texto': 'Un corazón es una riqueza que no se vende ni se compra, pero que se regala.'}, {'id_autor': 174, 'texto': 'El futuro nos tortura y el pasado nos encadena. He aquí por qué se nos escapa el presente.'}, {'id_autor': 174, 'texto': 'No haces arte solo con buenas intenciones.'}, {'id_autor': 52, 'texto': 'Si exagerásemos nuestras alegrías, como hacemos con nuestras penas, nuestros problemas perderían importancia.'}, {'id_autor': 53, 'texto': 'La muerte como final del tiempo que se vive sólo puede causar pavor a quien no sabe llenar el tiempo que le es dado para vivir.'}, {'id_autor': 54, 'texto': 'La ciencia moderna aún no ha producido un medicamento tranquilizador tan eficaz como lo son unas pocas palabras bondadosas.'}, {'id_autor': 55, 'texto': 'Al fin y al cabo, somos lo que hacemos para cambiar lo que somos.'}, {'id_autor': 56, 'texto': 'Los seres humanos no nacen para siempre el día en que sus madres los alumbran, sino que la vida los obliga a parirse a sí mismos una y otra vez.'}, {'id_autor': 57, 'texto': 'Ser independiente de la opinión pública es la primera condición formal para lograr algo grande.'}, {'id_autor': 58, 'texto': 'Saber es relativamente fácil. Querer y obrar de acuerdo a lo que uno quisiera, es siempre más duro.'}, {'id_autor': 59, 'texto': 'Donde funciona un televisor, seguro que hay alguien que no está leyendo.'}, {'id_autor': 60, 'texto': 'La juventud es feliz porque tiene la capacidad de ver la belleza. Cualquiera que conserve la capacidad de ver la belleza jamás envejece.'}, {'id_autor': 61, 'texto': 'Si es bueno vivir, todavía es mejor soñar, y lo mejor de todo, despertar.'}, {'id_autor': 62, 'texto': 'De las cosas que tienes, escoge las mejores y después medita cuán afanosamente las hubieras buscado si no las tuvieras.'}, {'id_autor': 63, 'texto': 'La desvalorización del mundo humano crece en razón directa de la valorización del mundo de las cosas.'}, {'id_autor': 64, 'texto': 'Si el pensamiento corrompe el lenguaje, el lenguaje también puede corromper el pensamiento.'}, {'id_autor': 112, 'texto': 'Las cosas no cambian; cambiamos nosotros.'}, {'id_autor': 112, 'texto': 'No es que el cuento necesite ser largo, sino el largo tiempo que tomará hacerlo corto.'}, {'id_autor': 66, 'texto': 'Quien no es capaz de desprenderse de un tesoro en un momento de necesidad es como un esclavo encadenado.'}, {'id_autor': 67, 'texto': 'El secreto de la felicidad no es hacer siempre lo que se quiere sino querer siempre lo que se hace.'}, {'id_autor': 68, 'texto': 'Se viaja no para buscar el destino sino para huir de donde se parte.'}, {'id_autor': 106, 'texto': 'La incertidumbre es una margarita cuyos pétalos no se terminan jamás de deshojar.'}, {'id_autor': 106, 'texto': 'Uno no puede pelear consigo mismo, porque esta batalla tendría un solo perdedor.'}, {'id_autor': 70, 'texto': 'No hay cosa más fácil que dar consejo ni más difícil que saberlo tomar.'}, {'id_autor': 160, 'texto': 'A veces podemos pasarnos años sin vivir en absoluto, y de pronto toda nuestra vida se concentra en un solo instante.'}, {'id_autor': 160, 'texto': 'Una idea que no es peligrosa no vale la pena llamarla idea.'}, {'id_autor': 72, 'texto': 'Sólo en soledad se siente la sed de la verdad.'}, {'id_autor': 73, 'texto': 'La vida es muy traicionera, y cada uno se las ingenia como puede para mantener a raya el horror, la tristeza y la soledad. Yo lo hago con mis libros.'}, {'id_autor': 74, 'texto': 'La pobreza no viene por la disminución de las riquezas, sino por la multiplicación de los deseos.'}, {'id_autor': 75, 'texto': 'Quien sea incapaz de hablar claro debe callar hasta poder hacerlo.'}, {'id_autor': 76, 'texto': 'El que dice una mentira no sabe qué tarea ha asumido, porque estará obligado a inventar veinte más para sostener la certeza de esta primera.'}, {'id_autor': 77, 'texto': 'El tiempo hace estragos en la gratitud, aún más que en la belleza.'}, {'id_autor': 78, 'texto': 'Saludable es al enfermo la alegre cara del que le visita.'}, {'id_autor': 79, 'texto': 'Todas las pasiones son buenas mientras uno es dueño de ellas, y todas son malas cuando nos esclavizan.'}, {'id_autor': 80, 'texto': 'Todo es bueno cuando es excesivo.'}, {'id_autor': 81, 'texto': 'El mundo entero se aparta cuando ve pasar a un hombre que sabe adónde va.'}, {'id_autor': 82, 'texto': 'Deberíamos vivir tantas veces como los árboles, que pasado un año malo echan nuevas hojas y vuelven a empezar.'}, {'id_autor': 83, 'texto': 'Si en medio de las adversidades persevera el corazón con serenidad, con gozo y con paz, esto es amor.'}, {'id_autor': 84, 'texto': 'Es mejor saber después de haber pensado y discutido que aceptar los saberes que nadie discute para no tener que pensar.'}, {'id_autor': 85, 'texto': 'Como todos los soñadores, confundí el desencanto con la verdad.'}, {'id_autor': 105, 'texto': 'Como no me he preocupado de nacer, no me preocupo de morir.'}, {'id_autor': 105, 'texto': 'A menudo me he perdido a mi mismo, solo para encontrar el fuego que lo mantiene todo vivo.'}, {'id_autor': 105, 'texto': 'Solo el misterio nos permite vivir. Solo el misterio.'}, {'id_autor': 105, 'texto': 'En el corazón de todo arte grandioso hay una melancolía esencial.'}, {'id_autor': 88, 'texto': 'En el momento en que te paras a pensar si quieres a alguien, ya has dejado de quererle para siempre.'}, {'id_autor': 90, 'texto': 'La vida es tan incierta, que la felicidad debe aprovecharse en el momento en que se presenta.'}, {'id_autor': 91, 'texto': 'Un problema deja de serlo si no tiene solución.'}, {'id_autor': 92, 'texto': 'Las personas libres jamás podrán concebir lo que los libros significan para quienes vivimos encerrados.'}, {'id_autor': 121, 'texto': 'La violencia es el último recurso del incompetente.'}, {'id_autor': 121, 'texto': 'Es el escritor quien atrapa la imaginación de los jóvenes, y planta la semilla que florecerá y se convertirá en cosecha.'}, {'id_autor': 134, 'texto': 'Vale más vivir y morir de una vez, que no languidecer cada día en nuestra habitación bajo el pretexto de preservarnos.'}, {'id_autor': 134, 'texto': 'Siempre cargo dos libros en mi bolsillo, uno para leer, y otro para escribir.'}, {'id_autor': 96, 'texto': 'La sensibilidad levanta una barrera que no puede salvar la inteligencia.'}, {'id_autor': 97, 'texto': 'No hay venganza más bella que aquella que infringen los otros a tu enemigo. Tiene hasta la virtud de dejarte la parte del generoso.'}, {'id_autor': 99, 'texto': 'La memoria es un espejo que miente escandalosamente.'}, {'id_autor': 99, 'texto': 'Toda distracción profunda abre una puerta. Debes permitirte estar distraído cuando eres incapaz de concentrarte.'}, {'id_autor': 147, 'texto': 'Errar en el camino propio es mejor que acertar en el camino de alguien más.'}, {'id_autor': 147, 'texto': '¿Qué es el infierno? Yo sostengo que es el sufrimiento de ser incapaz de amar.'}, {'id_autor': 147, 'texto': 'Sin ninguna meta y esfuerzo para alcanzarlo, ningún hombre puede vivir.'}, {'id_autor': 102, 'texto': 'Al hombre solo le gusta enumerar sus problemas, no suele calcular su felicidad.'}, {'id_autor': 152, 'texto': 'La prosa es arquitectura, no una decoración interna.'}, {'id_autor': 152, 'texto': 'No es su problema que hayas aprendido a escribir. Déjalos que pinsen que así naciste.'}, {'id_autor': 152, 'texto': 'Como escritor, no debes juzgar, debes entender.'}, {'id_autor': 152, 'texto': 'Cuando se escribe una novela, el escritor debería crear a personas vivientes; personas, no personajes. Un personaje es una caricatura.'}, {'id_autor': 109, 'texto': 'Si puedes contar cuentos, crear personajes, idear incidentes, y tener sinceridad y pasión, no importa cómo rayos escribas.'}, {'id_autor': 110, 'texto': 'Para producir un gran libro, debes escoger un gran tema.'}, {'id_autor': 111, 'texto': 'Está perfectamente bien si escribes basura, siempre y cuando la edites brillantemente.'}, {'id_autor': 164, 'texto': 'Primero, descubre qué quieren tus héroes, y luego solo síguelos.'}, {'id_autor': 164, 'texto': 'Debes mantenerte borracho cuando escribes para que así la realidad no te destruya.'}, {'id_autor': 164, 'texto': 'No necesito un reloj con alarma. Mis ideas me despiertan.'}, {'id_autor': 164, 'texto': 'Con frecuencia los buenos escritores tocan vidas. Los mediocres pasan una mano rápida sobre ellas. Y los malos solo las violan y las dejan por las moscas.'}, {'id_autor': 114, 'texto': 'La mayoría del material básico con el que un escritor trabaja es adquirido antes de cumplir los quince.'}, {'id_autor': 115, 'texto': 'Las palabras son lentes que enfocan nuestra mente.'}, {'id_autor': 116, 'texto': 'Un escritor sin interés o simpatía por las debilidades de sus compañeros no puede considerarse un escritor.'}, {'id_autor': 117, 'texto': 'Escritores de ciencia ficción, lamento decirlo, pero realmente no saben nada.'}, {'id_autor': 118, 'texto': 'Escribir una novela es como conducir un auto por la noche. Solo puedes ver tan lejos como las luces lo permitan, pero puedes hacer todo un viaje en ese camino.'}, {'id_autor': 122, 'texto': 'Arriésgate, aprovecha las oportunidades. Puede que sea malo, pero es la única forma de hacer algo realmente bueno.'}, {'id_autor': 122, 'texto': 'El trabajo nunca va unido al sueño de la perfección con el que el artista tiene que comenzar.'}, {'id_autor': 120, 'texto': 'No hay dinero en la poesía, entonces tampoco hay poesía en el dinero.'}, {'id_autor': 123, 'texto': 'Escribir es nuestra recompensa.'}, {'id_autor': 124, 'texto': 'Una historia sin leer no es una historia; son pequeñas marcas negras sobre la pulpa de madera. El lector, leyendo, lo hace vivo: una cosa con vida, una historia.'}, {'id_autor': 125, 'texto': 'La ficción se trata de cosas que están perdidas.'}, {'id_autor': 126, 'texto': 'Comenzar es un arte maravilloso, pero terminar es un arte más grande.'}, {'id_autor': 127, 'texto': 'Toda la información que necesitas puede ser dada en un diálogo.'}, {'id_autor': 128, 'texto': 'Tienes que escribir un libro que quieres que sea escrito. Y si el libro resulta difícil para los adultos, entonces escríbelo para los niños.'}, {'id_autor': 129, 'texto': 'Escribimos para saborear la vida dos veces, en el momento y en retrospectiva.'}, {'id_autor': 170, 'texto': 'Si no tienes tiempo para leer, no tienes el tiempo (ni las herramientas) para escribir. Tan simple como eso.'}, {'id_autor': 170, 'texto': 'La descripción comienza con la imaginación del escritor, pero debe ser terminada por los lectores.'}, {'id_autor': 170, 'texto': 'Escribir es un trabajo solitario. Y tener a alguien que cree en ti hace mucha diferencia. Solo con creer es más que suficiente.'}, {'id_autor': 170, 'texto': 'Las personas silenciosas son las que tienen las mentes más ruidosas.'}, {'id_autor': 131, 'texto': 'Si hay un libro que quieras leer, pero no ha sido escrito todavía, entonces debes escribirlo.'}, {'id_autor': 132, 'texto': 'No debes cambiar nada de lo que escribiste cuando te levantas en medio de la noche.'}, {'id_autor': 135, 'texto': 'Puedes crear lo que sea escribiendo.'}, {'id_autor': 136, 'texto': 'Una palabra tras otra palabra tras otra es poder.'}, {'id_autor': 137, 'texto': 'Escribir es como el sexo. Primero lo haces por amor, luego lo haces por tus amigos, y luego lo haces por dinero.'}, {'id_autor': 138, 'texto': 'Siempre sé un poeta, incluso en la prosa.'}, {'id_autor': 140, 'texto': 'Las ideas son como los conejos. Tienes un par y aprendes cómo manejarlos, y muy pronto tienes una docena.'}, {'id_autor': 143, 'texto': 'Los escritores viven dos veces.'}, {'id_autor': 144, 'texto': 'La única persona en la que estas destinado a convertirte es en la persona que decidas ser.'}, {'id_autor': 145, 'texto': 'Una meta es un sueño con fecha limite.'}, {'id_autor': 146, 'texto': 'El éxito es que te gustes a ti mismo, que te guste lo que haces, y cómo lo haces.'}, {'id_autor': 148, 'texto': 'No conozco nada en este mundo tan poderoso como una palabra. Algunas veces escribo una, y solo la miro cuando empieza a brillar.'}, {'id_autor': 150, 'texto': 'Llena tu papel con el aliento de tu corazón.'}, {'id_autor': 153, 'texto': 'Un lector vive miles de vidas antes de morir. El hombre que nunca lee solo vive una vez.'}, {'id_autor': 154, 'texto': 'Soy escritora, y escribiré lo que quiera escribir.'}, {'id_autor': 155, 'texto': 'No puedes esperar por la inspiración. Tienes que ir tras ella.'}, {'id_autor': 156, 'texto': 'Escribir ficción es el acto de tejer una serie de mentiras para llegar a una gran verdad.'}, {'id_autor': 161, 'texto': 'Un escritor es alguien al que se le hace más difícil la escritura de lo que es para otras personas.'}, {'id_autor': 162, 'texto': 'No es usual que alguien pueda ser un verdadero amigo y un buen escritor.'}, {'id_autor': 163, 'texto': 'Dejemos que los demás se enorgullezcan de ellos mismos por todas las páginas que han escrito; prefiero presumir por las que he leído.'}, {'id_autor': 165, 'texto': '¿Quién de nosotros no ha sentido que el personaje que estamos leyendo en la página impresa es más real que la persona que está junto a nosotros?'}, {'id_autor': 166, 'texto': 'El universo esta hecho de historias, no de átomos.'}, {'id_autor': 167, 'texto': 'Lee un millón de libros, y todas tus palabras fluirán como un río.'}, {'id_autor': 169, 'texto': 'Un gran escritor revela la verdad, incluso cuando él o ella no desean hacerlo.'}, {'id_autor': 171, 'texto': 'Un novelista no puede estar sin un kimono y una pluma.'}, {'id_autor': 172, 'texto': 'No sé lo que te hace ser un escritor, pero probablemente no es la felicidad.'}, {'id_autor': 173, 'texto': 'Si deseas ser un escritor, escribe.'}, {'id_autor': 175, 'texto': 'Sin música, la vida sería un error.'}, {'id_autor': 176, 'texto': 'Aceptamos el amor que pensamos merecer.'}, {'id_autor': 177, 'texto': 'El pasado es historia, el mañana un misterio, el hoy es un regalo de Dios, y es por eso que lo llamamos presente.'}]

	obj = {
        'frases': lstFrases
    }

	if type == "xml":
		xml = dicttoxml.dicttoxml(lstFrases,item_func=lambda x: 'frase',custom_root='frases', attr_type=False)
		return Response(xml, mimetype='text/xml')

	return jsonify(obj)

if __name__ == '__main__':
    app.run(debug=True, port=5000)