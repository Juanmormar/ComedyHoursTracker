"""Comedy Hours user guide: builds shot.html (app with demo data) and one HTML guide per language.
Usage: python3 mkguide.py <app index.html> <out dir>
The Trainings tab (Google Drive + generator) is personal and deliberately left out."""
import sys, json

APP, G = sys.argv[1], sys.argv[2]
app = open(APP, encoding='utf-8').read()

# ── Demo app for screenshots ──────────────────────────────────────────────────
stub = r"""<style>#debugPanel,#syncActions,.sync-status{display:none!important}</style><script>
const Q=new URLSearchParams(location.search);const L=Q.get('lang');
localStorage.clear();localStorage.setItem('comedy-tracker-username','kike');localStorage.setItem('comedy-tracker-tab','calendar');localStorage.setItem('comedy-tracker-lang',L);
const D={
 es:['El dentista','Mi casero','Los gatos','Boda de mi primo','Clases de yoga','Sin batería','El gimnasio','Mi suegra'],
 en:['The dentist','My landlord','Cats','My cousin’s wedding','Yoga class','Dead battery','The gym','My mother-in-law'],
 pt:['O dentista','Meu senhorio','Os gatos','O casamento do meu primo','Aula de ioga','Sem bateria','A academia','Minha sogra'],
 fr:['Le dentiste','Mon proprio','Les chats','Le mariage de mon cousin','Cours de yoga','Plus de batterie','La salle de sport','Ma belle-mère']}[L];
const C={es:['Probar el final en directo','Buen remate','El remate llegó tarde: acortar la premisa.'],
 en:['Try the ending live','Great punchline','The punchline came late: shorten the premise.'],
 pt:['Testar o final ao vivo','Ótimo desfecho','O desfecho demorou: encurtar a premissa.'],
 fr:['Tester la fin en live','Super chute','La chute arrivait tard : raccourcir la prémisse.']}[L];
const P={es:['Terraza','Micro abierto','Bar Central','Teatro'],en:['Terrace','Open mic','Central Bar','Theatre'],pt:['Terraço','Open mic','Bar Central','Teatro'],fr:['Terrasse','Open mic','Bar Central','Théâtre']}[L];
const seed={
 videos:[{id:'v1',title:'1. '+D[0],status:'green',comment:C[1]},{id:'v2',title:'2. '+D[1],status:'purple'},{id:'v3',title:'3. '+D[2],status:'red'},
  {id:'v4',title:'4. '+D[3],status:'green'},{id:'v5',title:'5. '+D[4],status:'green',gigs:['g2','g1'],gigRates:{g2:'green',g1:'green'}},
  {id:'v6',title:'6. '+D[5]},{id:'v7',title:'7. '+D[6]}],
 'plan-2026-11':[{id:'p0',w:0,vid:'v1'},{id:'p1',w:1,vid:'v2'},{id:'p2',w:1,vid:'v3'},{id:'p3',w:2,vid:'v4'},{id:'p4',w:3,vid:'v5'},{id:'p5',w:4,vid:'v6'},{id:'p6',w:0,vid:null}],
 develop:[{id:'d1',title:D[7],comment:C[0],gigs:['g1','g2','g3'],gigRates:{g1:'green',g2:'orange'}},{id:'d2',title:D[5]}],
 toEdit:[{id:'e1',title:D[2]}],
 gigs:[{id:'g1',date:'2026-11-17',title:P[0],notes:C[2],jokes:['d1','v5']},{id:'g2',date:'2026-11-10',title:P[1],jokes:['d1']},
  {id:'g3',date:'2026-11-03',title:P[2]},{id:'g4',date:'2026-11-27',title:P[3]}],
 jokes:[{id:'a',dk:'2026-11-05',title:D[0],comment:C[1]},{id:'b',dk:'2026-11-05',title:D[1],comment:'',sentToDevelop:true},{id:'c',dk:'2026-11-03',title:D[5],comment:''}],
 '2026-11-03':{hours:2,note:'',videos:1},'2026-11-04':{hours:1,note:'',videos:0},'2026-11-05':{hours:3,note:D[3],videos:1},
 '2026-11-10':{hours:2,note:'',videos:2},'2026-11-12':{hours:1,note:'',videos:0},'2026-11-17':{hours:2,note:'',videos:1}};
window.fetch=async(u,o)=>new Response(o&&o.method==='POST'?'[]':JSON.stringify([{data:seed}]),{status:200,headers:{'Content-Type':'application/json'}});
addEventListener('load',()=>setTimeout(()=>{const q=s=>document.querySelector(s),m=Q.get('m');let sel=[];
 if(m==='cal'){}
 if(m==='stats'){sel=['.plan-head','#planStats'];}
 if(m==='combo'){q('#planBody .plan-item[data-id=p6] .combo-input').focus();sel=['#planBody .plan-item[data-id=p6]','body > .combo-list'];}
 if(m==='rec'){q('.tab-btn[data-tab=videos]').click();q('.subtab-btn[data-sub=develop]').click();sel=['#developList'];}
 if(m==='gigs'){q('.tab-btn[data-tab=notes]').click();q('.subtab-btn[data-nsub=gigs]').click();sel=['#nsub-gigs'];}
 setTimeout(()=>{if(!sel.length)return;let x1=1e9,y1=1e9,x2=0,y2=0;
  sel.forEach(s=>{const e=q(s);if(!e)return;const r=e.getBoundingClientRect();x1=Math.min(x1,r.left);y1=Math.min(y1,r.top);x2=Math.max(x2,r.right);y2=Math.max(y2,r.bottom);});
  const p=12;document.title='RECT:'+[x1-p,y1-p,x2-x1+2*p,y2-y1+2*p].map(Math.round).join(',');},150);
},400));
</script>"""
open(G + '/shot.html', 'w', encoding='utf-8').write(app.replace('<head>', '<head>' + stub, 1))

# ── Guide text ────────────────────────────────────────────────────────────────
# Each section: (title, [bullets], image or None, caption or None)
T = {
'es': dict(file='comedy-hours-guia-es', title='Comedy Hours', sub='Guía de uso',
 intro='Comedy Hours sirve para registrar lo que escribes, planificar tus vídeos y apuntar cómo va cada chiste en tus actuaciones. Todo se guarda solo, y lo ves igual en cualquier dispositivo.',
 secs=[
 ('Antes de empezar', ['<b>Elige tu perfil</b> y escribe su contraseña, que te dará quien gestiona la app. Cada perfil tiene sus propios datos.',
   '<b>El navegador recuerda tu perfil,</b> así que no tendrás que escribirla cada vez. Solo te la pide en un navegador nuevo o si cambias de perfil, arriba a la izquierda.',
   '<b>Cambia el idioma</b> arriba a la derecha: español, inglés, portugués o francés.',
   '<b>Descarga esta guía</b> con el botón junto al perfil.']),
 ('Calendario', ['<b>Horas:</b> haz clic en un día para añadir una ✕ por hora. Para quitarla, usa clic derecho o pulsación larga.',
   '<b>Vídeos editados 🎬:</b> clic para sumar uno; clic derecho o pulsación larga para restar.',
   '<b>Chistes 🤣:</b> clic para abrir la lista de chistes de ese día.',
   '<b>Nota del día:</b> pasa el ratón por el día y pulsa «+ nota» (en el móvil, ✎).',
   'Arriba ves el total del mes de horas, vídeos y chistes.'], 'cal', 'En cada día: 🤣 chistes, 🎬 vídeos editados y una ✕ por hora. A la derecha, el plan de subidas.'),
 ('Chistes', ['Pulsa 🤣 en un día, escribe el chiste y pulsa <b>Añadir</b>. Si lo dejas en blanco, cuenta igualmente y puedes ponerle título después.',
   'La flecha <b>→</b> lo envía a <b>Vídeos por desarrollar</b>. El chiste sigue en tu lista, marcado como <b>✓ Enviado</b>.',
   'En <b>Calendario › Chistes escritos</b> ves todos los del mes. Se abre en el mes del calendario y las flechas cambian de mes.']),
 ('Plan de subidas', ['Pulsa <b>+ Añadir vídeo</b> en una semana y escribe para filtrar tu backlog, o elige de la lista.',
   'Si eliges un vídeo que ya está en otra semana, <b>se mueve</b> a esta. La lista te indica dónde está.',
   'Si escribes un título nuevo, puedes crearlo con <b>＋ Crear</b>.',
   '<b>El punto de color</b> marca el resultado, con un clic por cada cambio: pendiente, funcionó, regular o fracasó.',
   'Arrastra <b>⋮⋮</b> para mover un vídeo. La pista «puedes subir N» sale de los vídeos que editaste la semana anterior.'], 'combo', 'Selector de vídeo con todo el backlog.'),
 ('Resultados de lo publicado', ['Encima del plan de subidas, y también en <b>Vídeos › Publicados</b>, ves cuántos vídeos publicaste entre dos fechas y cuántos <b>funcionaron</b>, fueron <b>regular</b> o <b>no funcionaron</b>, con su porcentaje.',
   'Por defecto cuenta <b>del primer al último día del mes</b> que estás viendo en el calendario.',
   'Cambia las fechas <b>Del</b> y <b>al</b> para ver otro periodo. Con <b>↺</b>, o al cambiar de mes, vuelve al mes completo.',
   'Cada vídeo cuenta en la semana del calendario en la que está.'], 'stats', 'Resultados del mes: barra de colores y porcentajes.'),
 ('Vídeos', ['<b>Backlog:</b> tus vídeos pendientes. Puedes pegar una lista para añadir varios a la vez.',
   '<b>Publicados:</b> un vídeo pasa aquí cuando su semana ha empezado y tiene un resultado de color.',
   '<b>Vídeos virales a prueba:</b> lista con casillas para marcar.',
   '<b>Vídeos por desarrollar:</b> la flecha <b>→ Por editar</b> lo pasa a la siguiente lista.',
   '<b>Vídeos por editar:</b> la flecha <b>→ Backlog</b> lo pasa al backlog cuando esté editado.']),
 ('Grabaciones', ['En las listas de Vídeos, el icono de <b>cámara</b> abre las grabaciones: las actuaciones donde grabaste ese chiste. La cámara se pone azul cuando el vídeo tiene alguna.',
   'En <b>+ Añadir grabación…</b> elige la actuación: aparece como una etiqueta con su código, por ejemplo <b>261117_Terraza</b>.',
   '<b>Haz clic en la etiqueta</b> para apuntar cómo fue el chiste en esa grabación: <b>azul</b> sin valorar, <b>verde</b> fue bien y <b>naranja</b> regular. Cada clic pasa al siguiente color.',
   'La <b>×</b> de la etiqueta quita la grabación.'], 'rec', 'Un chiste con tres grabaciones: una fue bien, otra regular y otra sin valorar.'),
 ('Actuaciones', ['En <b>Notas › Actuaciones</b> añade cada actuación con su <b>fecha</b> y el <b>sitio</b>. Se ordenan en <b>Próximas</b> y <b>Pasadas</b>.',
   'Cada una tiene un <b>código</b>: la fecha (AAMMDD) y el sitio, por ejemplo 261117_Terraza. Haz clic en él para copiarlo.',
   '<b>🎬 N</b> indica cuántos vídeos se grabaron ahí. Pasa el ratón por encima para ver cuáles.',
   'Con <b>🤣</b> apuntas los chistes que hiciste esa noche, elegidos de tus listas de Vídeos (por defecto, Por desarrollar).',
   'En el comentario escribe <b>qué aprendiste</b>: qué funcionó y qué no. En las actuaciones pasadas aparece abierto.'], 'gigs', 'Actuaciones próximas y pasadas, con su código, vídeos grabados y chistes.'),
 ('Comentarios', ['El icono de bocadillo está en todas las filas: en <b>gris</b> no hay comentario y en <b>naranja</b> sí. Haz clic para abrirlo o cerrarlo.',
   'El cuadro crece mientras escribes. Pon texto en <b>negrita</b> con Cmd+B (Ctrl+B en Windows) o con el botón <b>B</b>.']),
 ('Notas', ['<b>Por hacer:</b> tu lista de tareas. Debajo tienes <b>Cosas pendientes</b>, una segunda lista para lo que está a la espera.',
   '<b>Libreta:</b> un espacio libre para ideas, premisas o recordatorios.']),
 ('Guardado', ['Cada cambio se guarda automáticamente. Arriba a la derecha aparece <b>Guardado ✓</b>.',
   'Antes de borrar algo, la app te pide confirmación.',
   'Si ves <b>Sin conexión</b>, los cambios quedan en ese dispositivo. Abajo, <b>Sincronizar ahora</b> vuelve a cargar lo que hay en la nube y sustituye lo que tengas en pantalla.'])]),

'en': dict(file='comedy-hours-guide-en', title='Comedy Hours', sub='User guide',
 intro='Comedy Hours lets you log what you write, plan your videos and note how each joke goes at your gigs. Everything saves on its own, and you see the same data on any device.',
 secs=[
 ('Before you start', ['<b>Choose your profile</b> and enter its password, which the person running the app will give you. Each profile has its own data.',
   '<b>Your browser remembers your profile,</b> so you won’t type it every time. It only asks on a new browser or if you change profile, at the top left.',
   '<b>Change the language</b> at the top right: Spanish, English, Portuguese or French.',
   '<b>Download this guide</b> with the button next to the profile.']),
 ('Calendar', ['<b>Hours:</b> click a day to add one ✕ per hour. To remove one, right-click or long-press.',
   '<b>Videos edited 🎬:</b> click to add one; right-click or long-press to subtract.',
   '<b>Jokes 🤣:</b> click to open that day’s joke list.',
   '<b>Day note:</b> hover over the day and press “+ note” (✎ on a phone).',
   'The top shows the month’s total hours, videos and jokes.'], 'cal', 'On each day: 🤣 jokes, 🎬 videos edited and one ✕ per hour. On the right, the upload plan.'),
 ('Jokes', ['Press 🤣 on a day, type the joke and press <b>Add</b>. If you leave it blank it still counts, and you can title it later.',
   'The <b>→</b> arrow sends it to <b>Videos to Develop</b>. The joke stays on your list, marked <b>✓ Sent</b>.',
   '<b>Calendar › Written jokes</b> lists the whole month. It opens on the calendar’s month, and the arrows change month.']),
 ('Upload plan', ['Press <b>+ Add video</b> in a week and type to filter your backlog, or choose from the list.',
   'If you choose a video that’s already in another week, <b>it moves</b> to this one. The list shows you where it is.',
   'If you type a new title, you can create it with <b>＋ Create</b>.',
   '<b>The coloured dot</b> marks the result, one click per change: pending, worked, so-so or flopped.',
   'Drag <b>⋮⋮</b> to move a video. The “can upload N” hint comes from the videos you edited the week before.'], 'combo', 'Video picker with the whole backlog.'),
 ('Published results', ['Above the upload plan, and also in <b>Videos › Published</b>, you see how many videos you published between two dates and how many <b>worked</b>, were <b>so-so</b> or <b>flopped</b>, with percentages.',
   'By default it counts <b>from the first to the last day of the month</b> shown in the calendar.',
   'Change the <b>From</b> and <b>to</b> dates to see another period. <b>↺</b>, or changing month, goes back to the whole month.',
   'Each video counts in the calendar week it sits in.'], 'stats', 'The month’s results: colour bar and percentages.'),
 ('Videos', ['<b>Backlog:</b> your pending videos. You can paste a list to add several at once.',
   '<b>Published:</b> a video moves here once its week has started and it has a coloured result.',
   '<b>Viral Videos on Trial:</b> a list with tick boxes.',
   '<b>Videos to Develop:</b> the <b>→ To Edit</b> arrow moves it to the next list.',
   '<b>Videos to Edit:</b> the <b>→ Backlog</b> arrow moves it to the backlog once edited.']),
 ('Recordings', ['In the Videos lists, the <b>camera</b> icon opens the recordings: the gigs where you recorded that joke. The camera turns blue when the video has any.',
   'In <b>+ Add recording…</b> pick the gig: it shows as a tag with its code, for example <b>261117_Terrace</b>.',
   '<b>Click the tag</b> to note how the joke went in that recording: <b>blue</b> not rated, <b>green</b> went well and <b>orange</b> so-so. Each click moves to the next colour.',
   'The tag’s <b>×</b> removes the recording.'], 'rec', 'A joke with three recordings: one went well, one so-so and one not rated.'),
 ('Gigs', ['In <b>Notes › Gigs</b>, add each gig with its <b>date</b> and <b>venue</b>. They’re sorted into <b>Upcoming</b> and <b>Past</b>.',
   'Each one has a <b>code</b>: the date (YYMMDD) and the venue, for example 261117_Terrace. Click it to copy it.',
   '<b>🎬 N</b> shows how many videos were recorded there. Hover over it to see which.',
   'With <b>🤣</b> you note the jokes you did that night, picked from your Videos lists (Videos to Develop by default).',
   'In the comment, write <b>what you learned</b>: what worked and what didn’t. It’s open on past gigs.'], 'gigs', 'Upcoming and past gigs, with their code, recorded videos and jokes.'),
 ('Comments', ['The speech-bubble icon is on every row: <b>grey</b> means no comment and <b>orange</b> means there is one. Click to open or close it.',
   'The box grows as you type. Make text <b>bold</b> with Cmd+B (Ctrl+B on Windows) or the <b>B</b> button.']),
 ('Notes', ['<b>To-do:</b> your task list. Below it is <b>Pending things</b>, a second list for what’s waiting on something.',
   '<b>Notebook:</b> free space for ideas, premises or reminders.']),
 ('Saving', ['Every change saves automatically, and <b>Saved ✓</b> appears at the top right.',
   'Before deleting anything, the app asks you to confirm.',
   'If you see <b>Offline</b>, changes stay on that device. At the bottom, <b>Sync now</b> reloads what’s in the cloud and replaces what’s on screen.'])]),

'pt': dict(file='comedy-hours-guia-pt', title='Comedy Hours', sub='Guia de uso',
 intro='O Comedy Hours serve para registrar o que você escreve, planejar os seus vídeos e anotar como cada piada vai nas suas apresentações. Tudo é salvo sozinho, e você vê os mesmos dados em qualquer dispositivo.',
 secs=[
 ('Antes de começar', ['<b>Escolha o seu perfil</b> e digite a senha, que a pessoa que gerencia o app vai passar para você. Cada perfil tem os seus próprios dados.',
   '<b>O navegador lembra do seu perfil,</b> então você não precisa digitá-la toda vez. Ela só é pedida em um navegador novo ou ao trocar de perfil, no canto superior esquerdo.',
   '<b>Mude o idioma</b> no canto superior direito: espanhol, inglês, português ou francês.',
   '<b>Baixe este guia</b> com o botão ao lado do perfil.']),
 ('Calendário', ['<b>Horas:</b> clique em um dia para adicionar um ✕ por hora. Para remover, use o clique direito ou o toque longo.',
   '<b>Vídeos editados 🎬:</b> clique para somar um; clique direito ou toque longo para subtrair.',
   '<b>Piadas 🤣:</b> clique para abrir a lista de piadas daquele dia.',
   '<b>Nota do dia:</b> passe o mouse sobre o dia e clique em “+ nota” (no celular, ✎).',
   'No topo aparece o total do mês de horas, vídeos e piadas.'], 'cal', 'Em cada dia: 🤣 piadas, 🎬 vídeos editados e um ✕ por hora. À direita, o plano de publicação.'),
 ('Piadas', ['Clique em 🤣 em um dia, escreva a piada e clique em <b>Adicionar</b>. Se deixar em branco, ela conta mesmo assim e você pode dar um título depois.',
   'A seta <b>→</b> envia para <b>Vídeos para desenvolver</b>. A piada continua na sua lista, marcada como <b>✓ Enviado</b>.',
   'Em <b>Calendário › Piadas escritas</b> você vê todas as do mês. Abre no mês do calendário, e as setas mudam o mês.']),
 ('Plano de publicação', ['Clique em <b>+ Adicionar vídeo</b> em uma semana e digite para filtrar o seu backlog, ou escolha na lista.',
   'Se escolher um vídeo que já está em outra semana, <b>ele é movido</b> para esta. A lista mostra onde ele está.',
   'Se digitar um título novo, você pode criá-lo com <b>＋ Criar</b>.',
   '<b>O ponto colorido</b> marca o resultado, um clique por mudança: pendente, funcionou, mais ou menos ou fracassou.',
   'Arraste <b>⋮⋮</b> para mover um vídeo. A dica “pode publicar N” vem dos vídeos que você editou na semana anterior.'], 'combo', 'Seletor de vídeo com todo o backlog.'),
 ('Resultados do que foi publicado', ['Acima do plano de publicação, e também em <b>Vídeos › Publicados</b>, você vê quantos vídeos publicou entre duas datas e quantos <b>funcionaram</b>, foram <b>mais ou menos</b> ou <b>não funcionaram</b>, com a porcentagem.',
   'Por padrão, conta <b>do primeiro ao último dia do mês</b> que você está vendo no calendário.',
   'Mude as datas <b>De</b> e <b>a</b> para ver outro período. Com <b>↺</b>, ou ao mudar de mês, volta ao mês inteiro.',
   'Cada vídeo conta na semana do calendário em que está.'], 'stats', 'Resultados do mês: barra colorida e porcentagens.'),
 ('Vídeos', ['<b>Backlog:</b> os seus vídeos pendentes. Você pode colar uma lista para adicionar vários de uma vez.',
   '<b>Publicados:</b> um vídeo vem para cá quando a semana dele começou e ele tem um resultado colorido.',
   '<b>Vídeos virais em teste:</b> lista com caixas para marcar.',
   '<b>Vídeos para desenvolver:</b> a seta <b>→ Para editar</b> passa para a próxima lista.',
   '<b>Vídeos para editar:</b> a seta <b>→ Backlog</b> passa para o backlog depois de editado.']),
 ('Gravações', ['Nas listas de Vídeos, o ícone de <b>câmera</b> abre as gravações: as apresentações onde você gravou essa piada. A câmera fica azul quando o vídeo tem alguma.',
   'Em <b>+ Adicionar gravação…</b> escolha a apresentação: ela aparece como uma etiqueta com o código, por exemplo <b>261117_Terraco</b>.',
   '<b>Clique na etiqueta</b> para anotar como a piada foi naquela gravação: <b>azul</b> sem avaliação, <b>verde</b> foi bem e <b>laranja</b> mais ou menos. Cada clique passa para a próxima cor.',
   'O <b>×</b> da etiqueta remove a gravação.'], 'rec', 'Uma piada com três gravações: uma foi bem, outra mais ou menos e outra sem avaliação.'),
 ('Apresentações', ['Em <b>Notas › Apresentações</b>, adicione cada apresentação com a <b>data</b> e o <b>lugar</b>. Elas ficam em <b>Próximas</b> e <b>Passadas</b>.',
   'Cada uma tem um <b>código</b>: a data (AAMMDD) e o lugar, por exemplo 261117_Terraco. Clique nele para copiá-lo.',
   '<b>🎬 N</b> mostra quantos vídeos foram gravados ali. Passe o mouse por cima para ver quais.',
   'Com <b>🤣</b> você anota as piadas que fez naquela noite, escolhidas das suas listas de Vídeos (por padrão, Para desenvolver).',
   'No comentário, escreva <b>o que você aprendeu</b>: o que funcionou e o que não. Nas apresentações passadas ele aparece aberto.'], 'gigs', 'Apresentações próximas e passadas, com código, vídeos gravados e piadas.'),
 ('Comentários', ['O ícone de balão está em todas as linhas: em <b>cinza</b> não há comentário e em <b>laranja</b> há. Clique para abrir ou fechar.',
   'A caixa cresce enquanto você escreve. Deixe o texto em <b>negrito</b> com Cmd+B (Ctrl+B no Windows) ou com o botão <b>B</b>.']),
 ('Notas', ['<b>A fazer:</b> a sua lista de tarefas. Embaixo fica <b>Coisas pendentes</b>, uma segunda lista para o que está esperando algo.',
   '<b>Caderno:</b> um espaço livre para ideias, premissas ou lembretes.']),
 ('Salvamento', ['Cada mudança é salva automaticamente, e <b>Salvo ✓</b> aparece no canto superior direito.',
   'Antes de apagar algo, o app pede confirmação.',
   'Se aparecer <b>Sem conexão</b>, as mudanças ficam naquele dispositivo. Embaixo, <b>Sincronizar agora</b> recarrega o que está na nuvem e substitui o que está na tela.'])]),

'fr': dict(file='comedy-hours-guide-fr', title='Comedy Hours', sub='Guide d’utilisation',
 intro='Comedy Hours sert à noter ce que tu écris, à planifier tes vidéos et à suivre comment chaque blague passe sur scène. Tout s’enregistre tout seul, et tu retrouves les mêmes données sur n’importe quel appareil.',
 secs=[
 ('Avant de commencer', ['<b>Choisis ton profil</b> et tape son mot de passe, que te donnera la personne qui gère l’app. Chaque profil a ses propres données.',
   '<b>Le navigateur se souvient de ton profil,</b> tu n’as donc pas à le retaper à chaque fois. Il n’est demandé que sur un nouveau navigateur ou si tu changes de profil, en haut à gauche.',
   '<b>Change la langue</b> en haut à droite : espagnol, anglais, portugais ou français.',
   '<b>Télécharge ce guide</b> avec le bouton à côté du profil.']),
 ('Calendrier', ['<b>Heures :</b> clique sur un jour pour ajouter une ✕ par heure. Pour en retirer une, fais un clic droit ou un appui long.',
   '<b>Vidéos montées 🎬 :</b> clic pour en ajouter une ; clic droit ou appui long pour en retirer une.',
   '<b>Blagues 🤣 :</b> clic pour ouvrir la liste des blagues de ce jour-là.',
   '<b>Note du jour :</b> survole le jour et clique sur « + note » (✎ sur mobile).',
   'En haut, tu vois le total du mois en heures, vidéos et blagues.'], 'cal', 'Sur chaque jour : 🤣 blagues, 🎬 vidéos montées et une ✕ par heure. À droite, le plan de publication.'),
 ('Blagues', ['Clique sur 🤣 sur un jour, écris la blague et clique sur <b>Ajouter</b>. Si tu la laisses vide, elle compte quand même et tu peux lui donner un titre plus tard.',
   'La flèche <b>→</b> l’envoie vers <b>Vidéos à développer</b>. La blague reste dans ta liste, marquée <b>✓ Envoyé</b>.',
   '<b>Calendrier › Blagues écrites</b> montre toutes celles du mois. Elle s’ouvre sur le mois du calendrier, et les flèches changent de mois.']),
 ('Plan de publication', ['Clique sur <b>+ Ajouter une vidéo</b> dans une semaine et tape pour filtrer ton backlog, ou choisis dans la liste.',
   'Si tu choisis une vidéo déjà placée dans une autre semaine, <b>elle est déplacée</b> ici. La liste t’indique où elle est.',
   'Si tu tapes un nouveau titre, tu peux la créer avec <b>＋ Créer</b>.',
   '<b>La pastille de couleur</b> indique le résultat, un clic par changement : en attente, a marché, moyen ou raté.',
   'Fais glisser <b>⋮⋮</b> pour déplacer une vidéo. L’indication « tu peux en publier N » vient des vidéos montées la semaine précédente.'], 'combo', 'Sélecteur de vidéo avec tout le backlog.'),
 ('Résultats des publications', ['Au-dessus du plan de publication, et aussi dans <b>Vidéos › Publiées</b>, tu vois combien de vidéos tu as publiées entre deux dates et combien <b>ont marché</b>, ont été <b>moyennes</b> ou <b>ratées</b>, avec leur pourcentage.',
   'Par défaut, le compte va <b>du premier au dernier jour du mois</b> affiché dans le calendrier.',
   'Change les dates <b>Du</b> et <b>au</b> pour voir une autre période. Avec <b>↺</b>, ou en changeant de mois, on revient au mois entier.',
   'Chaque vidéo compte dans la semaine du calendrier où elle se trouve.'], 'stats', 'Résultats du mois : barre de couleurs et pourcentages.'),
 ('Vidéos', ['<b>Backlog :</b> tes vidéos en attente. Tu peux coller une liste pour en ajouter plusieurs d’un coup.',
   '<b>Publiées :</b> une vidéo arrive ici quand sa semaine a commencé et qu’elle a un résultat en couleur.',
   '<b>Vidéos virales à l’essai :</b> une liste avec des cases à cocher.',
   '<b>Vidéos à développer :</b> la flèche <b>→ À monter</b> la passe à la liste suivante.',
   '<b>Vidéos à monter :</b> la flèche <b>→ Backlog</b> la passe au backlog une fois montée.']),
 ('Enregistrements', ['Dans les listes de Vidéos, l’icône <b>caméra</b> ouvre les enregistrements : les scènes où tu as filmé cette blague. La caméra devient bleue quand la vidéo en a.',
   'Dans <b>+ Ajouter un enregistrement…</b>, choisis la scène : elle apparaît comme une étiquette avec son code, par exemple <b>261117_Terrasse</b>.',
   '<b>Clique sur l’étiquette</b> pour noter comment la blague est passée sur cet enregistrement : <b>bleu</b> pas évalué, <b>vert</b> a bien marché et <b>orange</b> moyen. Chaque clic passe à la couleur suivante.',
   'La <b>×</b> de l’étiquette retire l’enregistrement.'], 'rec', 'Une blague avec trois enregistrements : un a bien marché, un moyen et un pas évalué.'),
 ('Scènes', ['Dans <b>Notes › Scènes</b>, ajoute chaque scène avec sa <b>date</b> et le <b>lieu</b>. Elles sont classées en <b>À venir</b> et <b>Passées</b>.',
   'Chacune a un <b>code</b> : la date (AAMMJJ) et le lieu, par exemple 261117_Terrasse. Clique dessus pour le copier.',
   '<b>🎬 N</b> indique combien de vidéos ont été filmées là. Survole-le pour voir lesquelles.',
   'Avec <b>🤣</b>, tu notes les blagues jouées ce soir-là, choisies dans tes listes de Vidéos (par défaut, À développer).',
   'Dans le commentaire, écris <b>ce que tu as appris</b> : ce qui a marché et ce qui n’a pas marché. Il est ouvert sur les scènes passées.'], 'gigs', 'Scènes à venir et passées, avec leur code, les vidéos filmées et les blagues.'),
 ('Commentaires', ['L’icône de bulle est sur chaque ligne : <b>grise</b>, il n’y a pas de commentaire ; <b>orange</b>, il y en a un. Clique pour l’ouvrir ou le fermer.',
   'La zone s’agrandit pendant que tu écris. Mets du texte en <b>gras</b> avec Cmd+B (Ctrl+B sous Windows) ou le bouton <b>B</b>.']),
 ('Notes', ['<b>À faire :</b> ta liste de tâches. En dessous, <b>Choses en attente</b> est une deuxième liste pour ce qui attend quelque chose.',
   '<b>Carnet :</b> un espace libre pour tes idées, prémisses ou rappels.']),
 ('Enregistrement', ['Chaque changement s’enregistre automatiquement, et <b>Enregistré ✓</b> apparaît en haut à droite.',
   'Avant de supprimer quoi que ce soit, l’app te demande de confirmer.',
   'Si tu vois <b>Hors ligne</b>, les changements restent sur cet appareil. En bas, <b>Synchroniser</b> recharge ce qui est dans le cloud et remplace ce qui est à l’écran.'])]),
}

CSS = """@page{size:A4;margin:16mm 16mm 14mm}*{box-sizing:border-box}body{margin:0;font:10.5pt/1.5 -apple-system,"Helvetica Neue",Arial,sans-serif;color:#1d1d1f;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.hero{background:#7d0f1b;color:#fff;border-radius:10px;padding:18px 22px;margin-bottom:14px}.hero h1{margin:0;font-size:26pt;line-height:1.1;letter-spacing:-.01em}.hero p{margin:3px 0 0;font-size:12pt;opacity:.9}
.intro{font-size:11pt;margin:0 0 6px}section{margin-top:14px}section.noimg,li{break-inside:avoid}h2{font-size:13.5pt;margin:0 0 5px;color:#7d0f1b;break-after:avoid}ul{margin:0;padding-left:17px}li{margin:3px 0}
figure{margin:8px 0 0;break-inside:avoid}figure img{display:block;max-width:100%;border-radius:6px;border:1px solid #d2d2d7}figure.narrow img{max-width:60%}figure.mid img{max-width:78%}figcaption{font-size:9pt;color:#6e6e73;margin-top:3px}"""
WIDTH = {'combo': 'narrow', 'stats': 'narrow', 'rec': 'mid', 'gigs': 'mid'}
for l, c in T.items():
    h = [f'<!doctype html><html lang="{l}"><meta charset="utf-8"><title>{c["title"]} · {c["sub"]}</title><style>{CSS}</style><body>'
         f'<div class="hero"><h1>{c["title"]}</h1><p>{c["sub"]}</p></div><p class="intro">{c["intro"]}</p>']
    for s in c['secs']:
        name, items = s[0], s[1]
        img = s[2] if len(s) > 2 else None
        cap = s[3] if len(s) > 3 else None
        h.append(f'<section class="{"" if img else "noimg"}"><h2>{name}</h2><ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>')
        if img:
            h.append(f'<figure class="{WIDTH.get(img, "")}"><img src="{l}-{img}.jpg" alt="{cap}"><figcaption>{cap}</figcaption></figure>')
        h.append('</section>')
    open(f'{G}/{c["file"]}.html', 'w', encoding='utf-8').write(''.join(h))
json.dump({l: c['file'] for l, c in T.items()}, open(G + '/files.json', 'w'))
