TOKEN = '1291432348:AAH1HOhiVlSFn6xWJzjyzlNr-qRCAAWKKg8'

# Сообщения
hello_text = '\U0001F680 *Привет!*\n\nЭтот поможет определить тебе, входит ли дом или точка на карте ' \
             'в 9-й избирательный округ Екатеринбурга. Чтобы проверить адрес, воспользуйся одним из вариантов:\n\n' \
             '' \
             '1. Отправь адрес дома в свободном формате. Например: _«Московская 77»_ или _«проспект Ленина, 24А»_ ' \
             '(без кавычек).\n\n' \
             '' \
             '2. Если хочешь проверить адрес, где ты сейчас находишься, просто нажми на кнопку ниже и отправь ' \
             'свою геолокацию \u2B07\uFE0F\n\n' \
             'У бота есть и другие функции. Узнать о них можно по команде /help'
help_text = '\U0001F64B\U0001F3FB\u200D\u2642\uFE0F *Помощь в работе с ботом*\n\n' \
            'Просто отправь адрес дома в свободном формате. Например: _«Московская 77»_ или ' \
            '_«проспект Ленина, 24А»_ (без кавычек). или нажми на кнопку ниже.\n\n' \
            'Другие полезные команды:\n' \
            '/abbreviations — допустимые сокращения\n' \
            '/memo — памятка сборщика подписей\n' \
            '/program — программа кандидата\n' \
            '/help — вызвать эту команду'
memo_text = '\U0001F4BC Памятка сборщика'
abbreviations = '\u270D\U0001F3FB *Допустимые сокращения*\n\n' \
                '• улица — ул.\n' \
                '• корпус — корп. (нежелательно сокращать)\n' \
                '• дом — д.\n' \
                '• квартира — кв.\n' \
                '• микрорайон — мкр-н. (нежелательно сокращать)\n' \
                '• бульвар — бул. (нежелательно сокращать)\n' \
                '• шоссе — ш.\n' \
                '• проспект — просп. (нежелательно сокращать)\n' \
                '• строение — стр.\n' \
                '• комната — комн. (нежелательно сокращать)\n' \
                '• проезд — проезд. (нельзя сокращать)\n'
program = '\U0001F4E2 *Почему Константин Плашиннов?*\n\n' \
          '\u2757\uFE0F Ежегодные смерти на улицах города в ДТП по-прежнему измеряются десятками, и близятся к сотне ' \
          '(72 в прошлом году).\n\n' \
          '\u2757\uFE0F Богатый на историю и архитектуру город теряет свое лицо: памятники разрушаются и даже ' \
          'целенаправленно сносятся (например, аэропорт Уктус).\n\n' \
          '\u2757\uFE0F Жителей города игнорируют — администрация предпочитает решать вопросы, не спрашивая мнения ' \
          'людей (например, сквер на драме или парк 22 партсъезда).\n\n' \
          '\u2757\uFE0F Город должен развиваться и быть удобным для всех жителей города: безбарьерная среда и ' \
          'велоинфраструктура.\n\n' \
          '\u2757\uFE0F В городе должны соблюдаться цели устойчивого развития: раздельный сбор отходов и ' \
          'озеленение улиц.'


# Файлы
memo_photo = 'AgACAgIAAxkBAAN3X3OrQ5tjhJxppOHKcSV3DTxNsa0AApSvMRt1LqBL6-MXbcVwa0ZCTxKVLgADAQADAgADeQAD3aoEAAEbBA'

# Границы избирательных округов
constituency_3 = [(60.56336063046075, 56.82522182924867), [60.56166788675167, 56.825307500635624],
                  [60.56165715791557, 56.82444863159775], [60.561013427752044, 56.82450745889027],
                  [60.560916868227416, 56.82444054283886], [60.56004783250663, 56.82443245407825],
                  [60.55910369493338, 56.824380980110014], [60.55903932191706, 56.82434862500536],
                  [60.55898852380653, 56.824287686025755], [60.5588948103518, 56.82412085697585],
                  [60.55812802629517, 56.82345775632827], [60.55772000280331, 56.82307076523431],
                  [60.557172504442704, 56.82260434940495], [60.55615445778778, 56.82176427566877],
                  [60.555330681372986, 56.82104991681604], [60.55464355148794, 56.82048602162862],
                  [60.5542417289327, 56.82021719190235], [60.55352161692191, 56.81973836132556],
                  [60.55285137366668, 56.81931314609405], [60.55252664173478, 56.81910773198935],
                  [60.551979194401625, 56.81877925417149], [60.55145292804636, 56.81839882414239],
                  [60.55108300982983, 56.818147010589534], [60.55068626952322, 56.817862834619376],
                  [60.55059552767187, 56.81775929826585], [60.5500420861045, 56.8173279778555],
                  [60.54950296209251, 56.81751478979615], [60.54919141856998, 56.81739643693825],
                  [60.5488235486581, 56.81725013536751], [60.54897643457193, 56.817089064142834],
                  [60.54912932048581, 56.81694858593843], [60.549349261625046, 56.81684414630355],
                  [60.54995812307137, 56.81661761425044], [60.55089019070398, 56.81629178812192],
                  [60.550993455751076, 56.81637048678336], [60.55136360059505, 56.81625133544813],
                  [60.55042918602957, 56.815479416979066], [60.55003389547596, 56.81561364883959],
                  [60.54960273037693, 56.81528928503809], [60.54934322665475, 56.81508995801732],
                  [60.54913736711283, 56.8149553565244], [60.549901796682015, 56.814787655609166],
                  [60.54973013530502, 56.81445813583354], [60.55037686177741, 56.814287528855175],
                  [60.55140446192977, 56.814028655563924], [60.55090307258563, 56.81363831112597],
                  [60.55043168925541, 56.813246007193136], [60.54996030592518, 56.81284340116183],
                  [60.54654966361283, 56.80996527323245], [60.54507298182151, 56.810488242868956],
                  [60.544702103560866, 56.810180357272735], [60.54418638601355, 56.80976065339587],
                  [60.54348754483667, 56.809168408253775], [60.5430032803809, 56.808732112123316],
                  [60.54170215755161, 56.80891885213248], [60.54033666170591, 56.80913501697554],
                  [60.53648400373213, 56.810470461637564], [60.5367931283211, 56.810740248211694],
                  [60.53575377232781, 56.811126810170194], [60.535289750168296, 56.81076709803058],
                  [60.53406129843944, 56.809735756891634], [60.53298633594988, 56.808921615579614],
                  [60.53261782943339, 56.80862489388151], [60.5341042137837, 56.808152644301344],
                  [60.535584793159956, 56.80764650493151], [60.53431626155937, 56.806663683432795],
                  [60.5349360051054, 56.806484224306786], [60.53680339274909, 56.80591732554611],
                  [60.537703751911266, 56.805667986477204], [60.53858706174392, 56.80561862738352],
                  [60.53930187044643, 56.80562819165832], [60.5397860091737, 56.80560538458399],
                  [60.54040291724715, 56.805508270355226], [60.54084279952562, 56.805343469874316],
                  [60.54132559714835, 56.8050020951241], [60.541926411967665, 56.80443116831785],
                  [60.542629150729525, 56.80391688527115], [60.543647719872034, 56.80349170205866],
                  [60.54473634114843, 56.80307100807997], [60.54645312257333, 56.80241449491126],
                  [60.54823444466993, 56.80175353345491], [60.550750564927135, 56.80078681032748],
                  [60.55396557081062, 56.79960302103507], [60.55683553445662, 56.7985110315845],
                  [60.55701792466962, 56.79846982381021], [60.5572271369728, 56.79846688040341],
                  [60.55743634927593, 56.798484540874], [60.55758118856275, 56.79851103158453],
                  [60.557717981222495, 56.79855959782046], [60.55838585126722, 56.79909382238048],
                  [60.559769627747684, 56.80020053239591], [60.5606654855586, 56.80091574201497],
                  [60.56156670778765, 56.80162799477807], [60.56245586007604, 56.80235274215565],
                  [60.563377198872594, 56.80307747547371], [60.562697259369706, 56.803327701548326],
                  [60.56182838704516, 56.803641575148745], [60.56056039074231, 56.804114035940444],
                  [60.55981447405371, 56.80438865519232], [60.55939209378401, 56.804544854070954],
                  [60.559334493940355, 56.804550962932446], [60.559262250391264, 56.804527815181025],
                  [60.558750124563744, 56.804122083469416], [60.55859490862955, 56.804049300675935],
                  [60.55801322146198, 56.80427670048665], [60.55869376937322, 56.80482119397872],
                  [60.55919106340823, 56.80521039749751], [60.55938022679389, 56.8053974930691],
                  [60.55880422240795, 56.80563292176021], [60.558963143292075, 56.80577712111162],
                  [60.55922063535755, 56.80581390658837], [60.559864888078216, 56.8063456453098],
                  [60.560456116179935, 56.80681728327928], [60.56101771539756, 56.80724409711369],
                  [60.56165215181537, 56.80775963072788], [60.56219502230531, 56.808197410399735],
                  [60.562822842064534, 56.80870365892948], [60.56309707395813, 56.80892524424238],
                  [60.56336325922471, 56.8091468282474], [60.56387953650374, 56.809584107235985],
                  [60.56427391714167, 56.809902752204465], [60.567445629301744, 56.81241630922342],
                  [60.56766620019381, 56.81251984419144], [60.568124146583735, 56.81276828679673],
                  [60.568508154056246, 56.812991168643094], [60.56889327528675, 56.81321391926178],
                  [60.56896778291772, 56.81327692637071], [60.56914553777684, 56.81342704803206],
                  [60.56935547914417, 56.81359408687688], [60.57024549762773, 56.81430327118672],
                  [60.570464921041975, 56.81446410221348], [60.570785215694045, 56.814717223764006],
                  [60.571058571688425, 56.814935773771275], [60.57152403522988, 56.8152252610999],
                  [60.57192404274607, 56.81542617395507], [60.5727825208452, 56.81575634207994],
                  [60.57335366015099, 56.81594471151162], [60.573962443142754, 56.81612053255487],
                  [60.574522603943585, 56.81623996933285], [60.5747765720334, 56.81628230868674],
                  [60.575069942220715, 56.81632933340468], [60.575347219153954, 56.81636532555942],
                  [60.576238047823054, 56.81647347771774], [60.57710924278862, 56.81654937394898],
                  [60.578005623564, 56.816573982054706], [60.57898671530508, 56.81655488100153],
                  [60.57941460143691, 56.81653025100852], [60.5797830891496, 56.81649306124361],
                  [60.5801059793092, 56.816447045459036], [60.580581586943666, 56.81638108530217],
                  [60.581276651251606, 56.81626921229796], [60.58167838584552, 56.81618530104026],
                  [60.58184436677771, 56.8161358562338], [60.582391221390026, 56.81599594397705],
                  [60.583080064641095, 56.81579446982486], [60.58373489581381, 56.815613970743385],
                  [60.583973015657755, 56.8155579105022], [60.584180011769206, 56.815565131896456],
                  [60.584541234898936, 56.815588534656044], [60.58521540139621, 56.81563828219214],
                  [60.58598653648803, 56.81569887337969], [60.58676981531425, 56.81576371279549],
                  [60.58746122848169, 56.8158197535714], [60.58761813770906, 56.815814604986016],
                  [60.58776968251839, 56.815799159240434], [60.588021810165785, 56.815724136946045],
                  [60.58808350097316, 56.81576238362851], [60.58887743484153, 56.81578886207062],
                  [60.58871540307911, 56.81629914924876], [60.58858775626795, 56.816695002140186],
                  [60.58846016051966, 56.817127315509985], [60.588383908382745, 56.81753934012302],
                  [60.588276620022114, 56.818114479266484], [60.58820285927429, 56.81840131006459],
                  [60.58806740771908, 56.818808753097215], [60.58785163782485, 56.81945137844067],
                  [60.587683851829965, 56.81995751254652], [60.58755876646672, 56.82033117692473],
                  [60.58740685901339, 56.820759258263884], [60.587252902426485, 56.82122006984613],
                  [60.58710449468276, 56.82162984305366], [60.58687558248376, 56.82233624347369],
                  [60.586673347311276, 56.822892612044], [60.58660839887801, 56.82306334655056],
                  [60.586528609661094, 56.82323243505823], [60.58646534724348, 56.82337265981508],
                  [60.58640769055339, 56.82350493296414], [60.58633390741528, 56.82366809065574],
                  [60.58628152743497, 56.823787677893094], [60.58621217578364, 56.8239476171859],
                  [60.586138211887224, 56.8241163937719], [60.586089019663135, 56.824244541766205],
                  [60.586044369297284, 56.824358547764525], [60.58599984618319, 56.824469924514815],
                  [60.58592529382717, 56.82465552414749], [60.58587314342005, 56.82479114771357],
                  [60.58574540571287, 56.825115704699115], [60.58564337904944, 56.82525492051107],
                  [60.58307792957245, 56.824997297697266], [60.58101673539024, 56.82481614795822],
                  [60.58045768907888, 56.824799007365854], [60.57765864927548, 56.824881912022036],
                  [60.575912605357125, 56.82491209483917], [60.575991767598424, 56.826158111916456],
                  [60.576124574019886, 56.82645997167633], [60.57536833937878, 56.826276214155214],
                  [60.57418295129525, 56.82599833603154], [60.57343208107206, 56.82582928252621],
                  [60.57297133432567, 56.825700140609314], [60.57284578731642, 56.82559646029652],
                  [60.572816799831784, 56.82545748427971], [60.57276955369847, 56.82500893440527],
                  [60.57160217782595, 56.8250471696491], [60.569970982599784, 56.82508393584815],
                  [60.570002756963014, 56.825556013864585], [60.56920799880459, 56.82557660233693],
                  [60.56917416371637, 56.82510599404151], [60.568806086130245, 56.825117757370485],
                  [60.56746260096234, 56.825133925029384], [60.56634204069119, 56.825144325921215],
                  [60.56336063046075, 56.82522182924867]]
constituency_9 = [(60.609149768554644, 56.838911051002235), [60.59521819468121, 56.83739757720716],
                  [60.59462341483215, 56.837394378844685], [60.59430758472066, 56.837373538418184],
                  [60.58885599489793, 56.836815650811985], [60.585111631113115, 56.836441427204775],
                  [60.5819996119612, 56.83612652454279], [60.5821917406296, 56.83554419849253],
                  [60.582389233716015, 56.83505301989372], [60.58271446840471, 56.83420473584903],
                  [60.582793499452706, 56.83409607067464], [60.58324625063383, 56.83314513495876],
                  [60.5836292643805, 56.832094189189284], [60.5839818009205, 56.83109761942595],
                  [60.58422735574987, 56.83029849169405], [60.58456232180305, 56.82928913894029],
                  [60.58484569871076, 56.828362701655266], [60.585129075618475, 56.82743035910655],
                  [60.58546076989668, 56.826384812964164], [60.585783000170366, 56.825299570618625],
                  [60.58599448193513, 56.82470313622345], [60.58624887904422, 56.824071395573206],
                  [60.58674701254262, 56.822897232528085], [60.58698056980819, 56.8221749519048],
                  [60.587230220327896, 56.821435007688045], [60.58756360157256, 56.8204737576214],
                  [60.58790870429177, 56.81943613438286], [60.58825264523847, 56.81840808272238],
                  [60.58833285150254, 56.818111730364386], [60.5883780457725, 56.81778484111811],
                  [60.5884822486408, 56.817219652951486], [60.58855117950861, 56.81692477674921],
                  [60.58872471652797, 56.8164077778656], [60.58892366890565, 56.8157717622934],
                  [60.58809510077536, 56.815745014781584], [60.58802828000533, 56.815706499030824],
                  [60.587755163596434, 56.81578539632007], [60.58746058951543, 56.81580545255177],
                  [60.58417554709601, 56.815529600382554], [60.58394287239242, 56.8155141886956],
                  [60.58275733600782, 56.815830459940535], [60.581642878162114, 56.816126134354704],
                  [60.58124591122791, 56.81621586592194], [60.58054585467503, 56.816335017350966],
                  [60.57974119197056, 56.81644092941503], [60.57905454646273, 56.81650271130774],
                  [60.578314256774625, 56.81652918923574], [60.5777268530003, 56.81652624723025],
                  [60.57712872038998, 56.81650565330397], [60.57627846013226, 56.81644092940024],
                  [60.57544429312862, 56.81634090135854], [60.574559164153754, 56.81621733694253],
                  [60.573971760379486, 56.816082003986445], [60.57338435660521, 56.81591136610015],
                  [60.5725206853024, 56.81561127689033], [60.571981561290414, 56.8153906215146],
                  [60.57166237841762, 56.81524645930334], [60.57135660658991, 56.81507581760041],
                  [60.571109843360595, 56.81490811723202], [60.570712876426434, 56.81458154066044],
                  [60.570525121795306, 56.814437375322065], [60.569023084747, 56.81323989885328],
                  [60.56749422560851, 56.812357213455655], [60.56608338366665, 56.811227345703195],
                  [60.565069508659, 56.810418174590254], [60.5643989564053, 56.80985689378376],
                  [60.565172773706045, 56.80953799718167], [60.56595731984291, 56.80922792556942],
                  [60.56857783805045, 56.808240681586575], [60.572831821548036, 56.80663102065627],
                  [60.57646889697227, 56.8052832073001], [60.57627577792322, 56.80513017738029],
                  [60.579709005462306, 56.80383528371991], [60.58488633941325, 56.80186821017443],
                  [60.585050289439295, 56.80200304280968], [60.58570776592407, 56.8018082435221],
                  [60.586583758832, 56.80248131756874], [60.58763275422147, 56.80331109630651],
                  [60.58887545477062, 56.80431425245336], [60.588905964898174, 56.8043379800022],
                  [60.58899146031054, 56.80430652719613], [60.58915976892622, 56.80424803594274],
                  [60.589446765290866, 56.80414797521499], [60.589626808570934, 56.804086540732705],
                  [60.58979209970147, 56.804040556778645], [60.59010390649948, 56.80395447466466],
                  [60.5902702034584, 56.80391915885555], [60.590427783237985, 56.80388310727543],
                  [60.590531718837354, 56.803866185106976], [60.59087772380023, 56.803810268279165],
                  [60.591131863104394, 56.80378746006979], [60.59150938402326, 56.803769066348735],
                  [60.59194792519724, 56.80375876586364], [60.59236366759456, 56.80376465185017],
                  [60.59277404557381, 56.80378525282908], [60.5931871057621, 56.803811739771994],
                  [60.593474102126684, 56.80384411268493], [60.59525775726594, 56.80404997760086],
                  [60.59680272351418, 56.804207570239555], [60.59960026751665, 56.804485679089],
                  [60.59926761965691, 56.80552071489559], [60.59894366228503, 56.806438673140775],
                  [60.59862126122614, 56.8074270316276], [60.601939153777636, 56.80776691287945],
                  [60.605254364119986, 56.808105319694896], [60.60779373857721, 56.808357065269405],
                  [60.61014134894524, 56.80859379715367], [60.610819023218816, 56.80864458048723],
                  [60.61176491839387, 56.80873067503938], [60.61384446337499, 56.808947002390305],
                  [60.61619173500296, 56.80918437830313], [60.617882204162164, 56.80937358227201],
                  [60.620553006861215, 56.80964000020452], [60.622978401290446, 56.809888525778526],
                  [60.62542021385862, 56.810123226705386], [60.62793712827921, 56.8103844084478],
                  [60.63035447608137, 56.81065357157829], [60.63492227803368, 56.81112877480713],
                  [60.634876680480474, 56.81126853931789], [60.635147583590985, 56.81131856018831],
                  [60.63552577506208, 56.81154806678419], [60.63594755242965, 56.811808098985296],
                  [60.63640151630543, 56.81208284109047], [60.636692535983556, 56.81223804926944],
                  [60.6361923040023, 56.81219464989044], [60.63580740700864, 56.8122056836384],
                  [60.63547749529979, 56.81229689579941], [60.63519854556231, 56.81242782900318],
                  [60.63472647677568, 56.81276913585028], [60.63434023867753, 56.81315751570747],
                  [60.633769177455015, 56.81388579070479], [60.63335834716949, 56.814465730330156],
                  [60.633087647067526, 56.814915472453066], [60.63241405332622, 56.81557931872151],
                  [60.63216228495734, 56.81575249556854], [60.63161243210935, 56.815958438624364],
                  [60.63043494235182, 56.8163114812264], [60.62910456668041, 56.81671159212959],
                  [60.628396463500515, 56.816946949480574], [60.62792707692282, 56.81725291181039],
                  [60.627562296496826, 56.81750003340536], [60.62702317248484, 56.8175941745423],
                  [60.62580008517406, 56.817735385783884], [60.624941778289326, 56.81799427168594],
                  [60.62428463708066, 56.81826492320127], [60.62386353026531, 56.81857087473283],
                  [60.62319297801155, 56.8192224842978], [60.622785282241296, 56.819618151370705],
                  [60.62237758647108, 56.819782888840614], [60.62195916186477, 56.819924091814805],
                  [60.6214964808097, 56.8200814736474], [60.62096942673821, 56.820221204638294],
                  [60.620544296609324, 56.82031828059133], [60.6200842977633, 56.82034769750175],
                  [60.61944324980876, 56.82031828059502], [60.61877269755505, 56.8202756260391],
                  [60.617973399268564, 56.82019472933354], [60.61740745316649, 56.820132953549354],
                  [60.617061448203565, 56.82014986835385], [60.6167449475398, 56.82025503416704],
                  [60.616482091056355, 56.820399177032726], [60.61627287875317, 56.82054773185989],
                  [60.61588932286406, 56.8209007310319], [60.61540384303234, 56.82139492427275],
                  [60.61501267588534, 56.82180180153604], [60.61461614432042, 56.82222926516381],
                  [60.61420757781169, 56.82272597766216], [60.613813293086416, 56.82303924630429],
                  [60.61318297396799, 56.82352458691991], [60.61297979663505, 56.8237003374765],
                  [60.61270688186777, 56.823993743488224], [60.6122576118578, 56.824477600994314],
                  [60.61187673817767, 56.8248864483389], [60.611487817870575, 56.82528940861111],
                  [60.61119277487887, 56.825524711854946], [60.61080117236274, 56.825724718459064],
                  [60.610377383338346, 56.825867369560335], [60.60992140780585, 56.82599531391258],
                  [60.60939569483891, 56.82611296349011], [60.60876269351144, 56.82623061271151],
                  [60.60743231784007, 56.82644238035424], [60.60653109561103, 56.82660708769548],
                  [60.606217277156254, 56.82671591177497], [60.60593028079172, 56.82686591204818],
                  [60.60576163689987, 56.827027676340045], [60.60562517951618, 56.827315909185835],
                  [60.60563121448643, 56.82743943686367], [60.60637081976898, 56.827520095064415],
                  [60.607340941242065, 56.827625326178705], [60.60807435776962, 56.827703244358084],
                  [60.608751280269786, 56.82777847758402], [60.60961763378158, 56.82787089273823],
                  [60.610486758913915, 56.82796801764913], [60.61226520877595, 56.828159222934325],
                  [60.61403024759295, 56.82833204561881], [60.614121152129066, 56.82841138414782],
                  [60.61420276047884, 56.82856481986929], [60.614024846896804, 56.82910541685394],
                  [60.6139092576168, 56.82945985503107], [60.61379160299581, 56.829855364103466],
                  [60.61372033967845, 56.83007078735311], [60.61365981217834, 56.83025023264266],
                  [60.61350169125033, 56.830735430038175], [60.61330369462144, 56.83125007884632],
                  [60.613236972619084, 56.83145320405752], [60.61316226240612, 56.83166551814744],
                  [60.61297801074266, 56.83216687134803], [60.6128711491483, 56.8324374200875],
                  [60.612801152266485, 56.832644741430734], [60.61271577531172, 56.83285500233248],
                  [60.612653983797856, 56.83302708239208], [60.6124715935847, 56.833581398301625],
                  [60.61232138987986, 56.83395779910087], [60.61219438442557, 56.83432374415232],
                  [60.612067921127924, 56.83470544333502], [60.611870778765336, 56.83526929097554],
                  [60.611870778765336, 56.835430283714025], [60.61194319840872, 56.83558980552104],
                  [60.61217655059305, 56.835705954590786], [60.61245684143507, 56.8358132819056],
                  [60.612517191137904, 56.835910317309015], [60.61243672486756, 56.83618818999475],
                  [60.61223019477346, 56.836801266823684], [60.612037925950595, 56.8374266218154],
                  [60.61186273213833, 56.83797446487146], [60.61167631861179, 56.83852870724774],
                  [60.6115596425196, 56.83893740059844], [60.61145235415908, 56.83919172908408],
                  [60.609149768554644, 56.838911051002235]]
