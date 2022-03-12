document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
    var adobeDCView = new AdobeDC.View({clientId: "ebad89bcc9ed40b1b1bb30cf65507969", divId: "adobe-dc-view"});
    adobeDCView.previewFile({
        content:{location: {url: "static/APB.pdf"}},
        metaData:{fileName: "APB.pdf"}
    }, {embedMode: "IN_LINE"});
});