import MaterialDateTimePicker from 'material-datetime-picker';
 
const input = document.querySelector('.c-datepicker-input');
const picker = new MaterialDateTimePicker()
    .on('submit', (val) => {
      input.value = val.format("DD/MM/YYYY");
    });
 
input.addEventListener('focus', () => picker.open());  