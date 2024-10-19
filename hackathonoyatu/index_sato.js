// 地図を初期化し、表示するための関数
function initMap() {
  // 初期の地図の中心座標（例: 東京）
  const initialCoords = [35.6762, 139.6503]; // 東京の緯度・経度

  // 地図を初期化して、表示する
  const map = L.map('map').setView(initialCoords, 12);

  // OpenStreetMapのタイルレイヤーを追加
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  // マーカーを初期位置に追加
  let marker = L.marker(initialCoords)
    .addTo(map)
    .bindPopup('東京')
    .openPopup();

  // 住所検索機能を追加（日本国内に限定）
  document.getElementById('search-btn').addEventListener('click', function () {
    const address = document.getElementById('address-input').value;

    if (address) {
      // Nominatim APIを使用して、住所をジオコーディング（日本国内に限定）
      fetch(
        `https://nominatim.openstreetmap.org/search?format=json&countrycodes=JP&limit=1&q=${encodeURIComponent(
          address
        )}`
      )
        .then((response) => response.json())
        .then((data) => {
          if (data && data.length > 0) {
            const lat = parseFloat(data[0].lat);
            const lon = parseFloat(data[0].lon);

            // 地図を検索結果の位置に移動
            const latLng = [lat, lon];
            map.setView(latLng, 15); // ズームレベルを調整

            // 既存のマーカーを削除
            if (marker) {
              map.removeLayer(marker);
            }

            // 新しいマーカーを追加
            marker = L.marker(latLng)
              .addTo(map)
              .bindPopup(data[0].display_name)
              .openPopup();
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
