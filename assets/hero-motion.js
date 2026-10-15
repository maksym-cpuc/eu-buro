/* Scroll-linked perspective on a portrait; no continuous background render loop. */
(function () {
  var hero = document.querySelector('.hero-portrait');
  if (!hero) return;
  var person = hero.querySelector('.hero-person');
  var halo = hero.querySelector('.hero-halo');
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  var mobile = matchMedia('(max-width: 759px)');
  var frame = 0, current = 0, target = 0, lastTime = 0;
  var visible = true, start = 0, distance = 1;

  function paint(progress) {
    var amount = mobile.matches ? 0.35 : 1;
    person.style.transform = 'translate3d(' + (-12 * progress * amount) + 'px,' +
      (46 * progress * amount) + 'px,0) rotateY(' + (-9 * progress * amount) +
      'deg) rotateZ(' + (-1.2 * progress * amount) + 'deg)';
    halo.style.transform = 'translate3d(' + (18 * progress * amount) + 'px,' +
      (-24 * progress * amount) + 'px,0)';
  }
  function stop() {
    cancelAnimationFrame(frame);
    frame = 0;
    lastTime = 0;
    person.style.willChange = '';
  }
  function tick(time) {
    frame = 0;
    var delta = lastTime ? Math.min(time - lastTime, 64) : 16;
    lastTime = time;
    current += (target - current) * (1 - Math.exp(-delta / 95));
    if (Math.abs(target - current) < 0.0005) current = target;
    paint(current);
    if (current !== target) frame = requestAnimationFrame(tick);
    else stop();
  }
  function update() {
    if (reduced.matches || document.hidden || !visible) return;
    target = Math.max(0, Math.min(1, (scrollY - start) / distance));
    if (!frame && target !== current) {
      person.style.willChange = 'transform';
      frame = requestAnimationFrame(tick);
    }
  }
  function measure() {
    var bounds = hero.getBoundingClientRect();
    start = bounds.top + scrollY;
    distance = Math.max(1, bounds.height * 0.75);
    update();
  }
  function preference() {
    stop();
    if (reduced.matches) {
      current = target = 0;
      person.style.transform = '';
      halo.style.transform = '';
    } else measure();
  }
  addEventListener('scroll', update, { passive: true });
  addEventListener('resize', measure, { passive: true });
  addEventListener('pageshow', measure);
  reduced.addEventListener('change', preference);
  mobile.addEventListener('change', measure);
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) stop();
    else measure();
  });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) measure();
      else stop();
    }).observe(hero);
  }
  if ('ResizeObserver' in window) new ResizeObserver(measure).observe(hero);
  measure();
})();
