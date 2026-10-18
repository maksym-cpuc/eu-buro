(function(){
  document.documentElement.classList.add('js');

  // Each language has its own URLs, so navigation and reloads keep the selection.
  document.querySelectorAll('[data-language]').forEach(function(link){
    function preserveSection(){
      var url=new URL(link.href);
      url.hash=location.hash;
      link.href=url.href;
    }
    preserveSection();
    addEventListener('hashchange',preserveSection);
  });

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

  // Заявка открывается в WhatsApp; посетитель сам отправляет сообщение в чате.
  document.querySelectorAll('form.lead').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var name=f.elements.name.value.trim();
      var situation=f.elements.situation.value.trim();
      var english=document.documentElement.lang==='en';
      var lines=[english ? 'Hello! I would like a free assessment from Nexora.' : 'Здравствуйте! Хочу получить бесплатный разбор в Nexora.'];
      if(name) lines.push((english ? 'My name is ' : 'Меня зовут ')+name+'.');
      if(situation) lines.push((english ? 'My situation: ' : 'Моя ситуация: ')+situation);
      var link=document.createElement('a');
      link.href=f.action+'?text='+encodeURIComponent(lines.join('\n\n'));
      link.target='_blank';
      link.rel='noopener noreferrer';
      document.body.appendChild(link);
      link.click();
      link.remove();
    });
  });
})();
