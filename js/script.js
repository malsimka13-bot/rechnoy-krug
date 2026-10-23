// 1. Мобильное меню
const btn = document.querySelector('.menu-btn');
const nav = document.getElementById('nav');
if (btn && nav) {
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
  });
}

// 2. Фильтр расписания по линиям
document.querySelectorAll('input[name="line"]').forEach(radio => {
  radio.addEventListener('change', () => {
    document.querySelectorAll('#timetable tbody tr').forEach(row => {
      row.hidden = radio.value !== 'all' && row.dataset.line !== radio.value;
    });
  });
});

// 3. Калькулятор стоимости поездки
const calc = document.getElementById('calc');
if (calc) {
  const update = () => {
    const prices = calc.cat.value.split('|').map(Number); // [проезд, экскурсия]
    const qty = Math.max(1, Math.min(50, Number(calc.qty.value) || 1));
    document.getElementById('total').textContent = prices[Number(calc.route.value)] * qty + ' ₽';
  };
  calc.addEventListener('input', update);
  calc.addEventListener('submit', e => e.preventDefault());
}
