/* Герой: портрет поворачивается при прокрутке, документы выходят из папки один за другим.
   Скролл читается в passive-слушателе, рисуется только в requestAnimationFrame с плавным догоном. */
(function () {
  var hero = document.querySelector('.hero-portrait');
  if (!hero) return;
  var visual = hero.querySelector('.hero-visual');
  var person = hero.querySelector('.hero-person');
  var halo = hero.querySelector('.hero-halo');
  var docs = [].slice.call(hero.querySelectorAll('.doc'));
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  var mobile = matchMedia('(max-width: 759px)');
  var frame = 0, current = 0, target = 0, lastTime = 0;
  var visible = true, start = 0, distance = 1, W = 1, H = 1;

  /* Позиции в долях блока .hero-visual: откуда выходит документ (папка), через какую точку идёт (обход лица) и где останавливается. */
  var DESK = {
    from: { x: 0.44, y: 0.5, r: -14 },
    rest: [
      { x: -0.03, y: 0.14, r: -9, via: { x: 0.0, y: 0.5 } },
      { x: 0.02, y: 0.44, r: 6, via: { x: 0.14, y: 0.5 } },
      { x: 0.62, y: 0.6, r: 4, via: { x: 0.54, y: 0.72 } }
    ]
  };
  var MOB = {
    from: { x: 0.46, y: 0.5, r: -14 },
    rest: [
      { x: 0.0, y: 0.1, r: -8, via: { x: 0.03, y: 0.48 } },
      { x: 0.02, y: 0.4, r: 5, via: { x: 0.16, y: 0.5 } },
      { x: 0.62, y: 0.54, r: 4, via: { x: 0.56, y: 0.7 } }
    ]
  };
  var PHASE = [-0.1, 0.2, 0.5], LEN = 0.4;

  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function bez(a, c, b, t) { var u = 1 - t; return u * u * a + 2 * u * t * c + t * t * b; }

  function paint(p) {
    var m = mobile.matches, amount = m ? 0.45 : 1, set = m ? MOB : DESK;
    person.style.transform = 'translate3d(' + (-12 * p * amount) + 'px,' + (36 * p * amount) + 'px,0) rotateY(' +
      (-14 * p * amount) + 'deg) rotateZ(' + (-1.2 * p * amount) + 'deg) scale(' + (1 - 0.03 * p * amount) + ')';
    halo.style.transform = 'translate3d(' + (18 * p * amount) + 'px,' + (-24 * p * amount) + 'px,0)';
    var ts = docs.map(function (_, i) { return clamp((p - PHASE[i]) / LEN); });
    docs.forEach(function (doc, i) {
      var t = ts[i], e = easeOut(t), rest = set.rest[i], from = set.from;
      var next = i + 1 < docs.length ? easeOut(ts[i + 1]) : 0; /* следующий документ отодвигает предыдущий */
      var x = bez(from.x, rest.via.x, rest.x, e) * W - 0.02 * next * W;
      var y = bez(from.y, rest.via.y, rest.y, e) * H - 0.05 * next * H;
      var rz = lerp(from.r, rest.r, e), rx = 55 * (1 - e), s = lerp(0.72, 1, e) - 0.04 * next;
      doc.style.transform = 'translate3d(' + x + 'px,' + y + 'px,0) rotateX(' + rx + 'deg) rotateZ(' + rz + 'deg) scale(' + s + ')';
      doc.style.opacity = clamp(t / 0.12) * (1 - 0.2 * next);
    });
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
    target = clamp((scrollY - start) / distance);
    if (!frame && target !== current) {
      person.style.willChange = 'transform';
      frame = requestAnimationFrame(tick);
    }
  }
  function measure() {
    var bounds = hero.getBoundingClientRect(), box = visual.getBoundingClientRect();
    W = box.width || 1;
    H = box.height || 1;
    start = bounds.top + scrollY;
    distance = Math.max(1, bounds.height * 0.6);
    if (reduced.matches) { paintStatic(); return; }
    paint(current);
    update();
  }
  /* Без движения: портрет на месте, документы сразу разложены. */
  function paintStatic() {
    var set = mobile.matches ? MOB : DESK;
    person.style.transform = '';
    halo.style.transform = '';
    docs.forEach(function (doc, i) {
      var r = set.rest[i];
      doc.style.transform = 'translate3d(' + (r.x * W) + 'px,' + (r.y * H) + 'px,0) rotateZ(' + r.r + 'deg)';
      doc.style.opacity = 1;
    });
  }
  function preference() {
    stop();
    current = target = 0;
    measure();
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
  if ('ResizeObserver' in window) new ResizeObserver(measure).observe(visual);
  measure();
})();
