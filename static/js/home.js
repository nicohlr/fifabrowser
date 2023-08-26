$(document).ready(function(){
    $('input[class="form_player"]').autoComplete({
        minChars: 2,
        delay: 100,  // This delay is for the built-in delay of the autoComplete plugin itself
        source: function(term, suggest){
            term = term.toLowerCase();
            $.ajax({
                url: "/autocomplete",  // endpoint to fetch the autocomplete suggestions
                data: { query: term },
                success: function(response) {
                    suggest(response);
                }
            });
        },
        renderItem: function(item, search) {
            search = search.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
            var re = new RegExp("(" + search.split(' ').join('|') + ")", "gi");
            return '<div class="autocomplete-suggestion" data-langname="' + item[0] + '" data-lang="' + item[1] + '" data-val="' + search + '">' + item[0].replace(re, "<b>$1</b>") + '</div>';
        },
        onSelect: function(e, term, item) {
            e.preventDefault();
            $('input[class="form_player"]').val(item.data('langname'));
        },
    });
});