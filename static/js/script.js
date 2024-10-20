// 地図を初期化し、表示するための関数
function initMap() {
  const map = L.map('map');
  
  // OpenStreetMapのタイルレイヤーを追加
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
  }).addTo(map);

  function getCoordinatesFromAddress(address) {
    // Nominatim APIを使用して住所をジオコーディング
    fetch(`https://nominatim.openstreetmap.org/search?format=json&countrycodes=JP&limit=1&q=${encodeURIComponent(address)}`)
        .then((response) => response.json())
        .then((data) => {
            if (data && data.length > 0) {
                const lat = parseFloat(data[0].lat);
                const lon = parseFloat(data[0].lon);
                // ここに地図を更新するコードを追加
                return {lat, lon};
            } else {
                alert('住所が見つかりませんでした。');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('検索中にエラーが発生しました。');
        });
}

console.log(getCoordinatesFromAddress('山口県山陽小野田市'))
//L.marker([34.69388615509474, 135.53129439101346]).addTo(map);

  // 現在地を取得
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        // 緯度と経度を10キロメートル単位に丸める
        const lat = Math.round(position.coords.latitude / 0.09) * 0.09;
        const lon = Math.round(position.coords.longitude / 0.09) * 0.09;

        // 現在地を地図の中心に設定
        const currentLocation = [lat, lon];
        map.setView(currentLocation, 12); // ズームレベルを調整
      },
      function () {
        // 位置情報取得に失敗した場合、デフォルトの位置を使用
        alert('現在地を取得できませんでした。東京の地図を表示します。');
        const defaultCoords = [35.6762, 139.6503]; // 東京の座標
        map.setView(defaultCoords, 12);
      }
    );
  } else {
    // 位置情報がサポートされていない場合、デフォルトの位置を表示
    alert('ブラウザが位置情報をサポートしていません。東京の地図を表示します。');
    const defaultCoords = [35.6762, 139.6503]; // 東京の座標
    map.setView(defaultCoords, 12);
  }

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