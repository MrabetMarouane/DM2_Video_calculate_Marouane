from PySide6 import QtWidgets
from PySide6 import QtGui

# Définition de la classe MaFenetre qui hérite de QDialog
class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Video_calculate") # Définit le titre de la fenêtre de dialogue
        self.create_layouts() # Crée les mises en page
        self.create_widgets() # Crée les widgets
        self.addWigets_to_layouts() # Ajoute les widgets aux mises en page
        self.setup_connections() # Configure les connexions

        #Créez un QLabel pour afficher l'image 
        self.image_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(".jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.layoutH6.addWidget(self.image_label)

    def create_layouts(self):         # Crée différentes mises en page (Layout)
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()
        self.layoutH7 = QtWidgets.QHBoxLayout()
        self.layoutH8 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.radioBt_Durée = QtWidgets.QRadioButton("Durée")
        self.radioBt_HDD = QtWidgets.QRadioButton("HDD")

        self.lbl_taille = QtWidgets.QLabel("Taille\t")
        self.LEdit_taille = QtWidgets.QLineEdit()
        self.LEdit_taille.setPlaceholderText("Saisir votre Taille")
        

        self.lbl_ips = QtWidgets.QLabel("ips\t")
        self.LEdit_ips= QtWidgets.QLineEdit()
        self.LEdit_ips.setPlaceholderText("Saisir votre ips")

        self.lbl_HDD = QtWidgets.QLabel("HDD\t")
        self.LEdit_HDD = QtWidgets.QLineEdit()
        self.LEdit_HDD.setPlaceholderText("Saisir votre HDD")

        
        
        self.lbl_Jour = QtWidgets.QLabel("\tJour")
        self.LEdit_Jour = QtWidgets.QLineEdit()

        self.lbl_Heure = QtWidgets.QLabel("\tHeures")
        self.LEdit_Heure = QtWidgets.QLineEdit()

        self.lbl_minute = QtWidgets.QLabel("\tMinutes")
        self.LEdit_minute = QtWidgets.QLineEdit()

        self.lbl_seconde = QtWidgets.QLabel("\tSecondes")
        self.LEdit_seconde = QtWidgets.QLineEdit()
        
        self.lbl_duree = QtWidgets.QLabel("Durée")
        #self.LEdit_duree = QtWidgets.QLineEdit()

        self.btn_Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Exit = QtWidgets.QPushButton("Exit")
        self.btn_Effacer = QtWidgets.QPushButton("Recommencer")

        self.radioBt_HDD.setChecked(True)
        self.LEdit_taille.setDisabled(True)
        self.LEdit_ips.setDisabled(True)
        self.LEdit_HDD.setDisabled(True)

    def addWigets_to_layouts(self):

        self.layoutH0.addWidget(self.radioBt_Durée)
        self.layoutH0.addWidget(self.radioBt_HDD)

        self.layoutH1.addWidget(self.lbl_taille)
        self.layoutH1.addWidget(self.LEdit_taille)

        self.layoutH2.addWidget(self.lbl_ips)
        self.layoutH2.addWidget(self.LEdit_ips)

        self.layoutH3.addWidget(self.lbl_HDD)
        self.layoutH3.addWidget(self.LEdit_HDD)

        self.layoutH5.addWidget(self.lbl_duree)

        self.layoutH4.addWidget(self.lbl_Jour)
        self.layoutH5.addWidget(self.LEdit_Jour)

        self.layoutH4.addWidget(self.lbl_Heure)
        self.layoutH5.addWidget(self.LEdit_Heure)

        self.layoutH4.addWidget(self.lbl_minute)
        self.layoutH5.addWidget(self.LEdit_minute)

        self.layoutH4.addWidget(self.lbl_seconde)
        self.layoutH5.addWidget(self.LEdit_seconde)

        self.layoutH7.addWidget(self.btn_Calculer)
        self.layoutH7.addWidget(self.btn_Exit)

        self.layoutH8.addWidget(self.btn_Effacer)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)
        self.layoutV.addLayout(self.layoutH7)
        self.layoutV.addLayout(self.layoutH8)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_Exit.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.radioBt_Durée.clicked.connect(self.Duree)#Durée
        self.radioBt_HDD.clicked.connect(self.HDD)#HDD
        self.btn_Calculer.clicked.connect(self.calculerDuree)
        self.btn_Calculer.clicked.connect(self.calculerHDD)
        self.btn_Effacer.clicked.connect(self.recommencer)

    def Duree(self):
        if self.radioBt_Durée.isChecked():
             self.LEdit_taille.setDisabled(False)
             self.LEdit_ips.setDisabled(False)
             self.LEdit_HDD.setDisabled(False)

             self.LEdit_Jour.setDisabled(True)
             self.LEdit_Heure.setDisabled(True)
             self.LEdit_minute.setDisabled(True)
             self.LEdit_seconde.setDisabled(True)

    def HDD(self):
         if self.radioBt_HDD.isChecked():
             self.LEdit_taille.setDisabled(False)
             self.LEdit_ips.setDisabled(False)
             self.LEdit_HDD.setDisabled(True)

             self.LEdit_Jour.setDisabled(False)
             self.LEdit_Heure.setDisabled(False)
             self.LEdit_minute.setDisabled(False)
             self.LEdit_seconde.setDisabled(False)
    
    
    def recommencer(self):
        # Réinitialise les zones de texte et l'affichage du résultat
        self.LEdit_HDD.setText("")
        self.LEdit_taille.setText("")
        self.LEdit_ips.setText("")
        self.LEdit_Jour.setText("")
        self.LEdit_Heure.setText("")         
        self.LEdit_minute.setText("")         
        self.LEdit_seconde.setText("")         
         


    #def HDD(self):
                #try:
                    #taille = float(self.LEdit_taille.text())
                   # ips = float(self.LEdit_ips.text())
                    #duree = float(self.LEdit_duree.text())
                
                    #print(taille,"***",ips,"***",duree)
                
                #except:
                    #pass

                #else:
                    #calcul_temps = (taille*ips*duree/(1024*1024))
                    #self.LEdit_duree.setText(str(calcul_temps))
                    #print(calcul_temps)
    def calculerDuree(self):

        taille_img = float(self.LEdit_taille.text())
        ips = float(self.LEdit_ips.text())
        stockage = float(self.LEdit_HDD.text())
        duree = (1024*1024*stockage)/(taille_img*ips)
        self.LEdit_Jour.setText(str(int(duree % 86400)))
        self.LEdit_Heure.setText(str(int((duree % 86400)//3600)))
        self.LEdit_minute.setText(str(int((duree % 3600)//60)))
        self.LEdit_seconde.setText(str(int(duree % 60)))

    def calculerHDD(self):

        taille_img = float(self.LEdit_taille.text()) 
        ips = float(self.LEdit_ips.text())
        duree_jour =int(self.LEdit_Jour.text()) 
        duree_heure =int(self.LEdit_Heure.text())      
        duree_minute =int(self.LEdit_minute.text())       
        duree_seconde =int(self.LEdit_seconde.text())

        duree_totale = (duree_jour *86400)+ (duree_heure*3600)+(duree_minute*60)+(duree_seconde)
        stockage = (taille_img*ips*duree_totale)/(1024*1024)

        self.LEdit_HDD.setText(str(stockage))     


app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()