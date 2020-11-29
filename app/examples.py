# -*- coding: utf-8 -*-
# # Copyright (c) 2016-2020 educorvi GmbH & Co. KG
# # lars.walther@educorvi.de

from .models import Welcome, ServiceDescription, ServiceButton, FormDescription

songtext = u"""\
<h2>Strophe 1</h2>
<p>Es ist wie eine Art Fröhlichkeit, wie ein Lächeln<br/>
Irgendwas liegt in dieser Stimme,<br/>
Das uns zu sagen scheint: "Komm!"<br/>
Das uns ein seltsames Wohlgefühl verschafft<br/>
Es ist wie die ganze Geschichte der Schwarzen,<br/>
Die immer zwischen Liebe und Verzweiflung schwankt.<br/>
Wie etwas, das in dir drin tanzt<br/>
Wenn du es hast, dann hast du’s.<br/>
</p>
<h2>Strophe 2</h2>
<p>Ella hat es.<br/>
Dieses gewisse Etwas,<br/>
Das andere nicht haben<br/>
Das uns in diesen seltsamen Zustand versetzt.<br/>
Ella hat es.<br/>
Ella hat es.<br/>
Dieses seltsame Etwas in ihrer Stimme<br/>
Diese Wonne darin<br/>
Diese Himmelsgabe,<br/>
Die sie so schön macht.<br/>
Ella hat es.<br/>
Ella hat es.<br/>
</p>
"""

steckbrief = """\
<p>France Gall war eine französische Pop- und Schlagersängerin. Nach einem erfolgreichen
Karrierestart in Frankreich gewann sie 1965 für Luxemburg den Grand Prix Eurovision
mit dem Titel Poupée de cire, poupée de son.</p>
<ul>
<li><strong>Geboren:</strong> 9. Oktober 1947, Paris, Frankreich</li>
<li><strong>Gestorben:</strong> 7. Januar 2018, Amerikanisches Krankenhaus Paris,
                                Neuilly-sur-Seine, Frankreich</li>
<li><strong>Ehepartner:</strong> Michel Berger (verh. 1976–1992)</li>
<li><strong>Kinder:</strong> Raphaël Hamburger, Pauline Hamburger</li>
<li><strong>Musikgruppe:</strong> Les Enfoirés (1993 – 1994)</li>
</ul>
"""

formfields = {u'vorname':{u'description':u'Dein Vorname', u'type':u'string'},
              u'name':{u'description':u'Dein Name', u'type':'string'},
              u'age':{u'description':u'Dein Alter', u'type':'number', u'minimum':18, u'maximum':67},
              u'geschmack':{u'description':u'Dein Musikgeschmack',u'type':u'array',
                           u'enum':['Pop','Rock','Klassik','Jazz'], u'uniqueItems':True}
             }

reqfields = ['name', 'age', 'geschmack']

example_services = {'ella_simple_page': ServiceDescription(name = u"ella_simple_page",
                        title = u"Steckbrief France Gall",
                        description = u"Wichtige biografische Stationen der Sängerin France Gall",
                        type = u"page",
                        text = steckbrief),
                    'ella_simple_service': ServiceDescription(name = u"ella_simple_service",
                        title = u"Fragebogen Musikinteresse",
                        description = u"Mit diesem Fragebogen teilst Du Dein Musikinteresse mit uns.",
                        type = u"service",
                        form = FormDescription(name = u"ella_simple_service",
                            title = u"Fragebogen Musikinteresse",
                            description =u"Mit diesem Fragebogen teilst Du Dein Musikinteresse mit uns.",
                            type = u"object",
                            properties = formfields,
                            required = reqfields),
                            formactions = [ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"btn btn-primary",
                                                         method=u"POST")]),
                    'ella_simple_group': ServiceDescription(name = u"ella_simple_group",
                        title = u"VIP Services",
                        description = u"Gruppe mit VIP-Services",
                        type = u"group",
                        services = [u"ella_simple_page", "ella_simple_group"])
                  }

example_apps = {'ella_example_simple': Welcome(name = u"ella_example_simple",
                    title = u"Ella, elle l'a",
                    description = u"(France Gall) ELLA, ELLE L'A LYRICS ÜBERSETZUNG",
                    bodytext = songtext,
                    services=[example_services['ella_simple_page'],
                             example_services['ella_simple_service'],
                             example_services['ella_simple_group']
                            ],
                    impressum=u"Impressum",
                    privacy=u"Datenschutzerklärung",
                    contact=u"Kontaktinformationen")
               }
