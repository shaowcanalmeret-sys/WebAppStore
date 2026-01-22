// site.js - validation & small interactions
document.addEventListener('DOMContentLoaded', function(){
  // nav toggle for mobile
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  if(btn && nav){
    btn.addEventListener('click', ()=> nav.classList.toggle('open'));
  }

  // Simple form validation hooks for login/signup forms
  const forms = document.querySelectorAll('form.needs-validation');
  forms.forEach(form=>{
    form.addEventListener('submit', function(e){
      // run validations defined on data-validate attributes
      const email = form.querySelector('input[type="email"]');
      const pwd = form.querySelector('input[name="password"]');
      const pwdConfirm = form.querySelector('input[name="password_confirm"]');
      let valid = true;
      const errors = [];

      if(email){
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!re.test(email.value.trim())){ valid=false; errors.push('البريد الإلكتروني غير صالح'); }
      }
      if(pwd){
        if(pwd.value.length < 8) { valid=false; errors.push('كلمة المرور قصيرة — يجب أن تكون 8 محارف على الأقل'); }
        // strong password example: at least one number and one letter
        if(!(/[0-9]/.test(pwd.value) && /[A-Za-z]/.test(pwd.value))){ valid=false; errors.push('كلمة المرور يجب أن تحتوي أحرفًا وأرقامًا'); }
      }
      if(pwd && pwdConfirm){
        if(pwd.value !== pwdConfirm.value){ valid=false; errors.push('كلمتا المرور غير متطابقتين'); }
      }

      // show errors
      const errBox = form.querySelector('.form-errors');
      if(errBox){
        errBox.innerHTML = '';
        if(!valid){
          e.preventDefault();
          errors.forEach(msg=>{
            const p = document.createElement('p');
            p.textContent = msg;
            p.style.color = 'crimson';
            errBox.appendChild(p);
          });
          window.scrollTo({top: form.offsetTop - 20, behavior:'smooth'});
        }
      }
    });
  });

});