(function(){
  document.documentElement.classList.add('js');

  // меню (три полоски)
  var menu=document.querySelector('.menu'),open=document.querySelector('.burger'),close=document.querySelector('.menu-close');
  function setMenu(on){menu.hidden=!on;document.body.style.overflow=on?'hidden':'';open.setAttribute('aria-expanded',on)}
  open.addEventListener('click',function(){setMenu(true)});
  close.addEventListener('click',function(){setMenu(false)});
  menu.addEventListener('click',function(e){if(e.target===menu)setMenu(false)});
  addEventListener('keydown',function(e){if(e.key==='Escape'&&!menu.hidden)setMenu(false)});
  menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setMenu(false)})});

  // появление блоков при прокрутке
  var els=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){io.observe(el)});
  }else{els.forEach(function(el){el.classList.add('in')})}

  // форма (прототип: никуда не отправляет)
  document.querySelectorAll('form.lead').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var c=f.querySelector('[name=contact]').value.trim(),err=f.querySelector('.form-error');
      if(!c){err.textContent='Оставьте контакт, чтобы мы могли ответить.';err.hidden=false;return}
      if(!f.querySelector('[name=consent]').checked){err.textContent='Отметьте согласие на обработку данных.';err.hidden=false;return}
      err.hidden=true;f.hidden=true;f.nextElementSibling.hidden=false;
    });
  });
})();
