$(document).ready(function(){
  console.log('hello');

  var npos = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    limit: 10,
    prefetch: {
      // url points to a json file that contains an array of country names
      url: '/data/npos',
      // the json file contains an array of strings, but the Bloodhound
      // suggestion engine expects JavaScript objects so this converts all of
      // those strings
      filter: function(list) {
        return $.map(list, function(npo) { return { name: npo }; });
      }
    }
  });
   
  // kicks off the loading/processing of `local` and `prefetch`
  npos.initialize();
  console.log(npos);

  $('.tt-hint').addClass('form-control');
   
  // passing in `null` for the `options` arguments will result in the default
  // options being used
  $('#prefetch .typeahead').typeahead(null, {
    name: 'npos',
    displayKey: 'name',
    // `ttAdapter` wraps the suggestion engine in an adapter that
    // is compatible with the typeahead jQuery plugin
    source: npos.ttAdapter()
  });

});

