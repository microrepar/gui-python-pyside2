import QtQuick 2.2
import QtQuick.Controls 2.4
import org.kde.kirigami 2.3 as Kirigami

Kirigami.ApplicationWindow
{
    width: 480
    height: 720

    Label {
        text: "Hello world!"
        anchors.centerIn: parent
    }
}