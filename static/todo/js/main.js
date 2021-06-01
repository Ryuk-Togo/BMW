$(function() {
    // 追加ボタン押下
    $('.btn_insert').click(function() {
        var totalManageElement = $('input#id_form-TOTAL_FORMS');
        var row = parseInt(totalManageElement.val());
    
        var todoLabelElement = $('<label>', {
            for: 'id_form-' + row + '-todo',
            value: 'TODO内容:'
        });

        var todoElement = $('<input>', {
            type: 'text',
            name: 'form-' + row + '-todo',
            id: 'id_form-' + row + '-todo',
            // class: 'item_name_class',
            maxlength: "100",
        });

        var todoRowElement = $('<input>', {
            type: 'hidden',
            name: 'form-' + row + '-row',
            id: 'id_form-' + row + '-row',
        });

        var todoIdElement = $('<input>', {
            type: 'hidden',
            name: 'form-' + row + '-id',
            id: 'id_form-' + row + '-id',
        });

        var newElement = $('div#todo_input');
        newElement.append('<p>');
        // newElement.append(todoLabelElement);
        newElement.append(todoRowElement);
        newElement.append(todoIdElement);
        newElement.append(todoElement);
        newElement.append('</p>');
        
        row += 1;
        totalManageElement.attr('value', row);

    });

});