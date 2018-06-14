var statusList = document.getElementsByName('XID')[0].options;

packets = [['Patient ID','Packet type','Visit Num','Status']];

for(i=6; i < statusList.length; i++){

    label = statusList[i].label.split(" ");

    csv = [label[3], label[6], label[10], label[19]];

    packets.push(csv);}

var csvContent;

csvContent = packets.map(packet => packet.join(",")).join("\n");

console.log(csvContent);

var encodedUri = encodeURI(csvContent);

var link = document.createElement("a");

link.href = 'data:text/csv,' + encodedUri;

link.download = "subject_status.csv";

link.click();
