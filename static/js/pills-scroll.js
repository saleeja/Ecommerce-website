/**
 * Keep the horizontal category pills scrolled to the active item after navigation.
 */
function scrollActivePillIntoView() {
  document.querySelectorAll('.pills-container').forEach((container) => {
    const active = container.querySelector('.pill.active');
    if (!active) return;

    active.scrollIntoView({
      behavior: 'auto',
      block: 'nearest',
      inline: 'center',
    });
  });
}

document.addEventListener('DOMContentLoaded', scrollActivePillIntoView);
window.addEventListener('load', scrollActivePillIntoView);
