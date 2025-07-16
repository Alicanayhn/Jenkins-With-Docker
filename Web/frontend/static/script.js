async function control_num() {
    const number = document.getElementById("input-num").value.trim();
    alert('Girilen sayi '+ number);
}

async function control_api() {
    const res = await fetch('/api/v1/users/control');
    const data_json = await res.json();
    alert("Flask apinin gönderdiği data : " + data_json.data);
}