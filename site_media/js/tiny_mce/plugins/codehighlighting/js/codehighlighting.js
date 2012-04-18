    function  Save_Button_onclick() {
	 var lang = document.getElementById("ProgrammingLanguages").value;
	 var syntax = document.getElementById("Syntax").value;
	 
	 var code;
	 if(syntax=="highlighter"){
		 code =  WrapCode(lang);
	 }else{
		 code =  WrapCodePrettify(lang);	 
	 }
	 
	 code = code + document.getElementById("CodeArea").value;
	 code = code + "</pre> "
	     if (document.getElementById("CodeArea").value == ''){
			tinyMCEPopup.close();
			return false;
		}
	tinyMCEPopup.execCommand('mceInsertContent', false, code);
	tinyMCEPopup.close();
    }
    
    function  WrapCode(lang)
    {
       var options = "";
       if (document.getElementById("nogutter").checked == true)
       options = ":nogutter";
       
       if (document.getElementById("collapse").checked == true)
       options = options + ":collapse";
              
       if (document.getElementById("nocontrols").checked == true)
       options = options + ":nocontrols";
              
       if (document.getElementById("showcolumns").checked == true)
       options = options + ":showcolumns";
       
       return "<pre class='brush: "+lang+"'>";

    }
    
    function WrapCodePrettify(lang){
    	
	var langPrettify = "";
    	switch(lang){
	    	case 'c++':
	    		langPrettify = "cpp";
	    	break
	    	case 'java':
	    		langPrettify = "java";
	    	break
	    	case 'javascript':
	    		langPrettify = "js"
	    	break
	    	case 'ruby':
	    		langPrettify = "rb";
	    	break
	    	case 'xhtml':
	    		langPrettify = "html";
	    	break
	    	case 'sql':
	    		langPrettify = "sql";
	    	break
	    	case 'python':
	    		langPrettify = "py";
	    	break
    	}
    	
    	
    	return "<pre class='prettyprint lang-"+langPrettify+" prettyprinted'>";
    	
    }

    function Cancel_Button_onclick()
    {
    	    tinyMCEPopup.close();
    	    return false;
    }