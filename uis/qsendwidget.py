# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qsendwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 462)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.senderAddress = QtWidgets.QLineEdit(Form)
        self.senderAddress.setObjectName("senderAddress")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.senderAddress)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password)
        self.receiverAddress = QtWidgets.QLineEdit(Form)
        self.receiverAddress.setObjectName("receiverAddress")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.receiverAddress)
        self.subject = QtWidgets.QLineEdit(Form)
        self.subject.setObjectName("subject")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.subject)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.send = QtWidgets.QPushButton(Form)
        self.send.setObjectName("send")
        self.horizontalLayout.addWidget(self.send)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textEdit, self.send)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Адрес отправителя"))
        self.label_2.setText(_translate("Form", "Пароль"))
        self.label_3.setText(_translate("Form", "Адрес получателя"))
        self.label_4.setText(_translate("Form", "Тема"))
        self.textEdit.setPlaceholderText(_translate("Form", "Введите текст сообщения..."))
        self.send.setText(_translate("Form", "Отправить сообщение"))
