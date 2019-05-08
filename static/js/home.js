console.log('coucou');

$('input[class="search_input"]').autoComplete({
    minChars: 1,
    source: function(term, suggest){
        term = term.toLowerCase();
        var choices = [['Australia', 'au'], ['Austria', 'at'], ['Brasil', 'br']];
        var suggestions = [];
        for (i=0;i<choices.length;i++)
            if (~(choices[i][0]+' '+choices[i][1]).toLowerCase().indexOf(term)) suggestions.push(choices[i]);
        suggest(suggestions);
    },
    renderItem: function (item, search){
        search = search.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
        var re = new RegExp("(" + search.split(' ').join('|') + ")", "gi");
        return '<div class="autocomplete-suggestion" data-langname="'+item[0]+'" data-lang="'+item[1]+'" data-val="'+search+'"><img src="img/'+item[1]+'.png"> '+item[0].replace(re, "<b>$1</b>")+'</div>';
    },
    onSelect: function(e, term, item){
        event.preventDefault();
        $('input[class="search_input"]').val(item.data('langname'));
    }
});