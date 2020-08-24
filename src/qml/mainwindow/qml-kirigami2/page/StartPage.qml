import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 2.4
import org.kde.kirigami 2.4 as Kirigami

Kirigami.Page
{
    title: "Start journey"

    actions.main: Kirigami.Action {
        icon.name: "search"
        text: "Search"
        onTriggered: pageStack.push(Qt.resolvedUrl("ConnectionsPage.qml"))
    }

    ColumnLayout {

        width: parent.width

        Label {
            text: "From:"
        }
        TextField {
            Layout.fillWidth: true
            placeholderText: "Würzburg..."
        }
        Label {
            text: "To:"
        }
        TextField {
            id: dest
            Layout.fillWidth: true
            placeholderText: "Berlin..."
        }

        RowLayout {
            width: parent.width
            Button {
                text: "Pick date"
                Layout.fillWidth: true
            }
            Button {
                text: "Pick time"
                Layout.fillWidth: true
            }
        }
    }
}


