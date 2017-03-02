var gulp = require('gulp');
    coffee = require('gulp-coffee'),
    plumber = require('gulp-plumber'),
    uglify = require('gulp-uglify'),
    minifyCSS = require('gulp-minify-css'),
    browserSync = require('browser-sync').create(),

    static_path = '/home/tonghs/Develop/xueyuan/static/',
    coffee_path = static_path.concat('coffee/'),
    js_path = static_path.concat('js/'),
    css_path = static_path.concat('css/'),
    dist_path = static_path.concat('dist/')


// 编译coffee
gulp.task('coffee', function() {
    gulp.src(coffee_path.concat('**/*.coffee'))
        .pipe(plumber())
        .pipe(coffee())
        .pipe(gulp.dest(js_path));
});


// 自动刷新
gulp.task('browser-sync', function() {
    browserSync.init({
        notify: false,
        proxy: 'http://test.xueyuan.yikuaitouba.com',
        files: "static/**/*.css, static/**/*.js, template/**/*.html"
    });
});


//压缩 css
gulp.task('minicss', function() {
    gulp.src(css_path.concat('**/*.css'))
    .pipe(minifyCSS())
    .pipe(gulp.dest(dist_path.concat('css')))
});

// gulp.task('fonts', function() {
//     gulp.src(css_path.concat('fonts/*.*'))
//     .pipe(gulp.dest(dist_path.concat('css/fonts')))
// });

//压缩 js
gulp.task('minijs', function() {
    gulp.src(js_path.concat('**/*.js'))
    .pipe(uglify())
    .pipe(gulp.dest(dist_path.concat('/js')))
});


// 默认任务
gulp.task('default', ['dev']);

gulp.task('dev', ['coffee', 'watch', 'browser-sync']);

gulp.task('online', ['coffee', 'minicss', 'minijs']);

// 监听 coffee
gulp.task('watch', function() {
    // 编译 coffee
    gulp.watch(coffee_path.concat('/**/*.coffee'), ['coffee']);
});
