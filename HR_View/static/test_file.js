downloadDoc=function(page)
    {
        var link=document.createElement('a');
        link.setAttribute("downloaded","");
        link.href=page;
        document.body.appendChild(link);
        link.click();
        link.remove();
    } 

    function fe(){
        $('#foo').html('hiee');
    }
    
    goHome=function(page)
    {
        var link=document.createElement('a');
        link.setAttribute("downloaded","");
        link.href=page;
        document.body.appendChild(link);
        link.click();
        link.remove();
    } 




