import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
class Example(QMainWindow):
    def __init__(self):
        super().__init__()            
        self.combo = QComboBox(self)
        self.combo_vnic = QComboBox(self)
        self.combo_pod = QComboBox(self)
        self.text_vlans = QTextEdit(self)
        self.btn_script = QPushButton(self)
        self.qlabel = QLabel(self)
        self.qlabel1 = QLabel(self)
        self.qlabel2 = QLabel(self)
        self.qlabel3 = QLabel(self)
        self.qlabel4 = QLabel(self)
        self.qlabel5= QLabel(self)
        self.qlabel6= QLabel(self)
        self.btn_a_type = QRadioButton(self)
        self.btn_b_type = QRadioButton(self)
        self.btn_both_type = QRadioButton(self)
        self.btn_a_type.setGeometry(100, 140, 95, 20)
        self.btn_b_type.setGeometry(100, 140, 95, 20)
        self.btn_both_type.setGeometry(100, 140, 95, 20)
        self.combo_vnic.setGeometry(100,180,170,20)
        self.combo_pod.setGeometry(100,180,170,20)
        self.btn_script.setGeometry(100,140,170,20)
        self.text_vlans.setGeometry(100,140,270,80)
        self.setWindowTitle("Comunicaciones SENHA")
        self.btn_script.setText("Genera el script")
        self.qlabel.move(50,16)
        self.qlabel1.move(50,40)
        self.qlabel6.move(50,90)
        self.combo_pod.move(50,120)
        self.qlabel3.move(50,150)
        self.combo_vnic.move(50,170)
        self.qlabel2.move(50,200 )
        self.text_vlans.move(50,220)
        self.qlabel4.move(50,320)
        self.btn_a_type.move(50,340)
        self.btn_b_type.move(100,340)
        self.btn_both_type.move(150,340)
        self.qlabel5.move(50,360)
        self.btn_script.move(50,390)
        self.combo.setGeometry(100,140,170,20)
        
        self.combo.addItem("Crear")
        self.combo.addItem("Borrar")
        self.combo.move(50, 60)

        self.qlabel.setText("Este programa te ayudara a escribir scripts mas facil para borrar o crear VLANs")
        self.qlabel.setFont(QFont("Arial",9))     
        self.qlabel2.setFont(QFont("Arial",9))      
        self.qlabel3.setFont(QFont("Arial",9))
        self.qlabel4.setFont(QFont("Arial",9))
        self.qlabel5.setFont(QFont("Arial",9))
        self.qlabel6.setFont(QFont("Arial",9))    
        self.combo.setFont(QFont("Arial",9))
        self.text_vlans.setFont(QFont("Arial",9))
        self.combo_vnic.setFont(QFont("Arial",9))
        self.btn_script.setFont(QFont("Arial",9))        
        self.qlabel1.setFont(QFont("Arial",9))    
        self.qlabel1.setText("Elige la acción que deseas realizar")
        self.qlabel2.setText("Inserte las VLANs separadas por comas")
        self.qlabel3.setText("Selecciona el vnic template que requieres trabajar")
        self.qlabel4.setText("Selecciona el Fabric que requieres trabajar")
        self.qlabel5.setText("A                B            A y B")
        self.qlabel6.setText("Elige el POD donde quieres trabajar")
        self.qlabel.adjustSize()
        self.qlabel1.adjustSize()
        self.qlabel2.adjustSize()
        self.qlabel3.adjustSize()
        self.qlabel4.adjustSize()
        self.qlabel5.adjustSize()
        self.qlabel6.adjustSize()
        self.combo.activated[str].connect(self.onChanged_create_delete)      
        self.combo_pod.activated[str].connect(self.onChanged_vnics)
        self.setGeometry(400,350,570,500)
    
        self.btn_script.clicked.connect(self.script_generate)

    def onChanged_create_delete(self):
            self.combo_create_or_delete()
    def onChanged_vnics(self): #Metodo del Combo_vnics que de acuerdo a  la selecion crear/borrar rellena los items
        if self.combo.currentIndex() == 0: #El usuario selecciono crear  VLANS  en cualquier POD que seleccione se rellenara de ITEMs
            self.vnics_to_create()
        elif self.combo.currentIndex() == 1:  #El usuario seleccion borrar VLANs y en cualquier POD que seleccione se rellenara de ITEMs
            self.vnics_to_delete()
    
    def script_generate(self):
        self.vlans_str = self.text_vlans.toPlainText()
        self.vlans_array = self.vlans_str.split(",")
        self.content_combo_vnic = self.combo_vnic.currentText()
        self.POD1_port_channels_gestion =["a 60","b 61"]
        self.POD1_port_channels_storage =["a 41","b 41"]
        self.POD1_port_channels_produccion  = ["a 40","b 40"]
        self.POD2_port_channels_gestion = ["a 62","b 63"]
        self.POD2_port_channels_storage =["a 43","b 43"]
        self.POD2_port_channels_produccion = ["a 42","b 42"]
        self.POD3_port_channels_gestion =["a 64","b 65"]
        self.POD3_port_channels_storage= ["a 45","b 45"]
        self.POD3_port_channels_produccion = ["a 44","b 44"]
        self.POD4_port_channels_gestion = ["a 66","b 67"]
        self.POD4_port_channels_storage = ["a 41","b 41"]
        self.POD4_port_channels_produccion = ["a 40","b 40"]
        self.Fabric_type_A = ["-A"]
        self.Fabric_type_B = ["-B"]
        self.Fabric_type_A_and_B = ["-A","-B"]
        self.Puertos_Fabric_interconnect =["13","14"]
        self.Member_port_channel =["a","b"]
        if self.combo.currentIndex() == 0: #El usuario selecciono la opcion de crear VLANs

            if self.combo_pod.currentIndex()==0: #El usuario selecciono el POD1
                if self.combo_vnic.currentText()=="gestion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD1_port_channels_gestion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD1_port_channels_gestion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD1_port_channels_gestion)
                elif self.combo_vnic.currentText()=="ip-storage":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD1_port_channels_storage)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD1_port_channels_storage)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD1_port_channels_storage)
                elif self.combo_vnic.currentText()=="produccion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD1_port_channels_produccion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD1_port_channels_produccion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD1_port_channels_produccion)

            elif self.combo_pod.currentIndex()==1:
                if self.combo_vnic.currentText()=="gestion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD2_port_channels_gestion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD2_port_channels_gestion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD2_port_channels_gestion)
                elif self.combo_vnic.currentText()=="ip-storage":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD2_port_channels_storage)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD2_port_channels_storage)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD2_port_channels_storage)
                elif self.combo_vnic.currentText()=="produccion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD2_port_channels_produccion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD2_port_channels_produccion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD2_port_channels_produccion)

            elif self.combo_pod.currentIndex()==2:
                if self.combo_vnic.currentText()=="gestion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD3_port_channels_gestion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD3_port_channels_gestion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD3_port_channels_gestion)
                elif self.combo_vnic.currentText()=="ip-storage":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD3_port_channels_storage)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD3_port_channels_storage)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD3_port_channels_storage)
                elif self.combo_vnic.currentText()=="produccion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD3_port_channels_produccion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD3_port_channels_produccion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD3_port_channels_produccion)

            elif self.combo_pod.currentIndex()==3:
                if self.combo_vnic.currentText()=="gestion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD4_port_channels_gestion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD4_port_channels_gestion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD4_port_channels_gestion)
                elif self.combo_vnic.currentText()=="ip-storage":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD4_port_channels_storage)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD4_port_channels_storage)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD4_port_channels_storage)
                elif self.combo_vnic.currentText()=="produccion":
                    if self.btn_a_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,self.POD4_port_channels_produccion)
                    elif self.btn_b_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,self.POD4_port_channels_produccion)
                    elif self.btn_both_type.isChecked():
                        self.create_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,self.POD4_port_channels_produccion)

        elif self.combo.currentIndex() == 1: #El usuario selecciono la opcion de borrar VLANs
            if self.combo_pod.currentIndex()==0:#El usuario seleccion el POD1
                if self.btn_a_type.isChecked() :
                    self.delete_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,["a"],self.Puertos_Fabric_interconnect,True)
                elif self.btn_b_type.isChecked():
                    self.delete_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,["b"],self.Puertos_Fabric_interconnect,True)
                elif self.btn_both_type.isChecked():
                    self.delete_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,["a","b"],self.Puertos_Fabric_interconnect,True)
                else:
                    print("Ocurrio un Error!")
            else:
                if self.btn_a_type.isChecked() :
                    self.delete_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A,["a"],self.Puertos_Fabric_interconnect,False)
                elif self.btn_b_type.isChecked():
                    self.delete_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_B,["b"],self.Puertos_Fabric_interconnect,False)
                elif self.btn_both_type.isChecked():
                    self.delete_vlans(self.vlans_array,self.content_combo_vnic,self.Fabric_type_A_and_B,["a","b"],self.Puertos_Fabric_interconnect,False)
                else:
                    print("Ocurrio un Error!")
            

    def vnics_to_delete(self): #Metodo que llena el combo_vnic de los vnics que se pueden borrar
        self.combo_vnic.clear()
        combo_domain_vnics=["cisco-avs","vmkernel","vmotion-senha","vmotion-spac","gestion","ip-storage","produccion"]
        self.combo_vnic.addItems(combo_domain_vnics)
        
    def vnics_to_create(self):#Metodo que llena el combo_vnic de los vnics que se pueden crear
        self.combo_vnic.clear()
        combo_domain_vnics=["gestion","ip-storage","produccion"]
        self.combo_vnic.addItems(combo_domain_vnics)    
     
    def combo_create_or_delete(self): #Metodo que llena el combo_pod de los POD existentes
        self.combo_pod.clear()
        self.combo_vnic.clear()
        combo_pod_array=["POD 1","POD 2","POD 3","POD 4"]
        self.combo_pod.addItems(combo_pod_array)

    #Metodo que borra VLANs, recibe el array de VLANs, el Vnic para trabajar y el tipo  o los tipos de Fabrica
    def delete_vlans(self,vlans_array,content_combo_vnic,fabric_type_vnic,fabric_type_member_port,fabric_port_channels,dominio_1_boolean):
        digitos = ["0","1","2","3","4","5","6","7","8","9"]
        vlan_number=""
        f= open("Delete VLANs in "+ content_combo_vnic +" at "+self.combo_pod.currentText()+".txt","w")
        for j in fabric_type_vnic:
            f.write("scope org\n")
            f.write("enter vnic-templ " + content_combo_vnic + j +" target adapter\n")
            for i in vlans_array :
                f.write("\tdelete eth-if "+ i +"\n")
            f.write("exit\n")
        if dominio_1_boolean == True:
            f.write("scope eth-uplink\n")
            for i in vlans_array:
            #Este metodo separa el numero de vlan y lo utiliza para escribirlo dentro del script
                for k in i:
                    if k in digitos:
                        vlan_number+=k    
                f.write("\tenter vlan " + i + " "+ vlan_number+"\n")
                # Este for recibe el tipo de fabrica y lo escribe dentro del script
                for j in fabric_type_member_port:
                    #Al haber recibido que estamos trabajando en el POD1 entramos a este metodo que omite el Fabric B y el Port Channel 13
                    for m in fabric_port_channels:
                        if j =="b" and m =="13":
                            f.write(" ")    
                        else:
                            f.write("\t\tdelete member-port "+ j +" 1 " + m +"\n")
                    
                f.write("\texit\n")
                vlan_number=""
            f.write("exit\n")
        else:
            f.write("scope eth-uplink\n")
            for i in vlans_array:
            #Este metodo separa el numero de vlan y lo utiliza para escribirlo dentro del script
                for k in i:
                    if k in digitos:
                        vlan_number+=k    
                f.write("\tenter vlan " + i + " "+ vlan_number+"\n")
                # Este for recibe el tipo de fabrica y lo escribe dentro del script
                for j in fabric_type_member_port:
                    for m in fabric_port_channels:
                            f.write("\t\tdelete member-port "+ j +" 1 " + m +"\n")
                    
                f.write("\texit\n")
                vlan_number=""
            f.write("exit\n")
        f.close()

    def create_vlans(self,vlans_array,content_combo_vnic,fabric_type,POD_port_channels):
        digitos = ["0","1","2","3","4","5","6","7","8","9"]
        vlan_number = ""
        f= open("Create VLANs in "+ content_combo_vnic +" at " + self.combo_pod.currentText() + ".txt","w")
        
        f.write ("scope eth-uplink\n")
        for i in vlans_array:
            for k in i:
                if k in digitos:
                    vlan_number+=k 
            f.write("\tenter "+ i+ " "+  vlan_number + "\n")
            for  j in POD_port_channels:
                f.write("\t\tcreate member port-channel "+ j +"\n")
                f.write ("\t\t\tset isnative no\n")
                f.write("\t\texit\n")
            vlan_number=""
                        
        for j in fabric_type:
            f.write("scope org\n")
            f.write("enter vnic-templ " +content_combo_vnic + j +" target adapter\n")
            for i in vlans_array :
                f.write("\t create eth-if "+ i +"\n")
                f.write("\t\tset default-net no\n\texit\n")
            f.write("exit\n")

        f.close() 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())   