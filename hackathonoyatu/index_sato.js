// 地図を初期化し、表示するための関数
function initMap() {
  // 地図の中心座標（例: 東京の緯度と経度）
  const tokyo = [35.6762, 139.6503];

  // 地図を初期化して、表示する
  const map = L.map('map').setView(tokyo, 12); // 第2引数はズームレベル

  // OpenStreetMapのタイルレイヤーを追加
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // マーカーを東京に追加
  L.marker(tokyo).addTo(map)
    .bindPopup('東京')
    .openPopup();
}

// 地図を初期化
initMap();
