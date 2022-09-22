document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
    var adobeDCView = new AdobeDC.View({clientId: "16afbd9ba10346489c311b3f7d6dad72", divId: "adobe-dc-view"});
    adobeDCView.previewFile({
        content:{location: {url: "static/APB.pdf"}},
        metaData:{fileName: "APB.pdf"}
    }, {embedMode: "IN_LINE"});
});