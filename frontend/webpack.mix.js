let mix = require('laravel-mix');

mix.js('src/main.js', '../src/assets/js').setPublicPath('../src/assets/js')
.vue();