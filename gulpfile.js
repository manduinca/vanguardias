var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('styles', function() {
  gulp
    .src('vanguardias/frontdev/scss/app.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('static/css/'));
});

gulp.task('copy-images', function() {
  gulp.src('./vanguardias/frontdev/img/**/*.*').pipe(gulp.dest('static/img/'));
});

gulp.task('copy-fonts', function() {
  gulp
    .src('./vanguardias/frontdev/fonts/**/*.*')
    .pipe(gulp.dest('static/fonts/'));
});

//Watch task
gulp.task('watch-styles', function() {
  gulp.watch('vanguardias/frontdev/scss/**/*.scss', ['styles']);
});

gulp.task('default', ['styles', 'copy-images', 'copy-fonts']);
