window.gdo ||= {};

window.gdo.tags = {
    init: function() {
        const input = document.querySelector('input[name=tags]');
        const tagify = new Tagify(input, {
          whitelist: ['foo', 'bar', 'baz', 'lawking'],
          dropdown: {
            enabled: 1,
            fuzzySearch: true,
          },
        });
    },
};

window.gdo.tags.init();