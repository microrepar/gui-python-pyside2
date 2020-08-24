import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

Window {
    id: window
    visible: true
    width: Screen.desktopAvailableWidth / 2
    height: Screen.desktopAvailableHeight / 2
    minimumWidth: Screen.desktopAvailableWidth / 3
    minimumHeight: Screen.desktopAvailableHeight / 3
    title: qsTr("PySide2 QQmlApplicationEngine e slot")

    ColumnLayout {
        anchors.margins: 12
        spacing: 12
        anchors.fill: parent

        Label {
            id: label
            objectName: "label"
            text: qsTr("Este texto será alterado quando o botão for clicado!")
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            rightPadding: 10
            leftPadding: 10
            padding: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        }

        TextField {
            id: textfield
            objectName: "text_field"
            text: qsTr("")
            placeholderText: qsTr("Digite algo")
            Layout.fillHeight: false
            Layout.fillWidth: true
            leftPadding: 5
        }

        Button {
            id: button_python_slot
            objectName: "button_python_slot"
            text: qsTr("Método Python é chamado no QML")
            Layout.fillWidth: true
            onClicked: {
                python.on_button_clicked(textfield.text)
            }
        }
    }
}
