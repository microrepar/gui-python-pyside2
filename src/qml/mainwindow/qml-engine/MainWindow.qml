import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

Window {
    id: mainwindow
    visible: true
    width: Screen.desktopAvailableWidth / 2
    height: Screen.desktopAvailableHeight / 2
    minimumWidth: Screen.desktopAvailableWidth / 3
    minimumHeight: Screen.desktopAvailableHeight / 3
    title: qsTr("PySide2 lendo arquivo QML com QQmlApplicationEngine()")
}
