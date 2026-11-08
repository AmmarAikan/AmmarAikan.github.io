/* Progressive navigation enhancement; every section works without JavaScript. */
(() => {
  const links = [...document.querySelectorAll('.section-nav a')];
  const sections = links.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
  const activate = id => links.forEach(link => {
    if (link.getAttribute('href') === `#${id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
  activate(location.hash.slice(1) || 'profile');
  links.forEach(link => link.addEventListener('click', () => activate(link.hash.slice(1))));
  if (!('IntersectionObserver' in window)) return;
  const observer = new IntersectionObserver(entries => {
    const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio);
    if (visible.length) activate(visible[0].target.id);
  }, { rootMargin: '-8% 0px -65% 0px', threshold: [0, 0.2, 0.6] });
  sections.forEach(section => observer.observe(section));
})();
