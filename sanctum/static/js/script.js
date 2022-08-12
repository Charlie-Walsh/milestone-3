document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    instances = M.Sidenav.init(sidenav);
    

    let stars = document.querySelectorAll('select');
    instances = M.FormSelect.init(stars);
  });