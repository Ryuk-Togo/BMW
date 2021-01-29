$(function(){
    // 左ペインのフォルダリストを描画
    let data = $('input#folder_data').val();
    generateMailFolder(convertStringToJSon(data),'div#folder_list ul#root');
    
    // リフレッシュボタン押下
    $('button#reflesh').on('click',function(){
        window.location.href = '/mailbk/';
    });

    // メールファイルをタブで開く
    $('a#link_mail').on('click',function(e){
        e.preventDefault(); 
        var url = $(this).attr('href'); 
        window.open(url, '_blank');
    });

});

//フォルダの形成
function generateMailFolder(folders,folderElement) {
    return factoryJSonForMailFolder(folders,folderElement);
}

// フォルダ構成の描画
function factoryJSonForMailFolder(data,ulTag) {

    // 取得したulタグの名称を取得
    for (var i=0; i<data.length; i++) {
        
        // データの項目を取得
        var folder = data[i].folder;
        var path = data[i].path.replaceAll('/','%5c');

        // さらに繰り返しデータがあるなら、当メソッドを再読み込み
        $(ulTag).append($('<li><a class="folder_link" href="' + path + '" >' + folder + ' </a></li>'));
        if (data[i].next.length!=0) {
            $(ulTag).append($('<ul id="' + folder + '">'));
            let ulNextTag = ulTag + ' ul#' + folder;
            factoryJSonForMailFolder(data[i].next,ulNextTag);
        }
    }
}

function convertStringToJSon(text) {
    return (new Function("return " + text))();
}