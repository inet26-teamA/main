// 地図を初期化し、表示するための関数
function initMap() {
  const map = L.map('map');
  // OpenStreetMapのタイルレイヤーを追加
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
  }).addTo(map);
  async function getCoordinatesFromAddress(address) {
    try {
      const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&countrycodes=JP&limit=1&q=${encodeURIComponent(address)}`);
      const data = await response.json();
      if (data && data.length > 0) {
        const lat = parseFloat(data[0].lat);
        const lon = parseFloat(data[0].lon);
        return { lat, lon }; // 成功した場合に座標を返す
      } else {
        return null; // 何も見つからなかった場合
      }
    } catch (error) {
      console.error('Error:', error);
      return null; // エラーが発生した場合
    }
  }
  
  fetchData();
  async function fetchData() {
    const response = await fetch('add_pin_data'); // サーバーから住所データを取得
    const data = await response.json();
    console.log(data);
    for (let i = 0; i < data.length; i++) {
      (async () => {
        const address = await getCoordinatesFromAddress(data[i][0]);
        if (address) {
          // console.log(address); // 座標を表示
          // console.log(data[i][0])
          // マーカーを追加し、ピンにカーソルを合わせるとポップアップで住所を表示
          L.marker([address.lat, address.lon])
            .addTo(map)
            .bindPopup(data[i][1]);  // ここで住所をポップアップ表示
        }
      })();
    }
  }
  // 現在地を取得
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        const lat = Math.round(position.coords.latitude / 0.09) * 0.09;
        const lon = Math.round(position.coords.longitude / 0.09) * 0.09;
        const currentLocation = [lat, lon];
        map.setView(currentLocation, 12); // ズームレベルを調整
      },
      function () {
        alert('現在地を取得できませんでした。東京の地図を表示します。');
        const defaultCoords = [35.6762, 139.6503]; // 東京の座標
        map.setView(defaultCoords, 12);
      }
    );
  } else {
    alert('ブラウザが位置情報をサポートしていません。東京の地図を表示します。');
    const defaultCoords = [35.6762, 139.6503]; // 東京の座標
    map.setView(defaultCoords, 12);
  }
  // 住所検索機能を追加（日本国内に限定）
  document.getElementById('search-btn').addEventListener('click', function () {
    const address = document.getElementById('address-input').value;
    if (address) {
      // Nominatim APIを使用して、住所をジオコーディング
      fetch(`https://nominatim.openstreetmap.org/search?format=json&countrycodes=JP&limit=1&q=${encodeURIComponent(address)}`)
        .then((response) => response.json())
        .then((data) => {
          if (data && data.length > 0) {
            const lat = parseFloat(data[0].lat);
            const lon = parseFloat(data[0].lon);
            const latLng = [lat, lon];
            map.setView(latLng, 15); // ズームレベルを調整
          } else {
            alert('住所が見つかりませんでした。');
          }
        })
        .catch((error) => {
          console.error('Error:', error);
          alert('検索中にエラーが発生しました。');
        });
    } else {
      alert('住所を入力してください。');
    }
  });
}
// 地図を初期化
initMap();