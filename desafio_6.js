function toJadenCase(string){
    let i=0
    let ini=0
    let string_final=''
    while  (i<string.length){
    if (i==0){
        ini=0
        string_final+=string.toUpperCase()[ini]
    }else if(string[i]===' '){
        ini=i+1
        string_final+=' '
        string_final+=string.toUpperCase()[ini]
        i=i+1
    }else{
        string_final+=string[i]
    }
    i++
    }
    return string_final 
} ;

