const cookie =
  "sessionid=59926273089:bEWe0xXDnRa8ro:20:AYc3ZlpAw8Rip1zHO2egPM0_2u_yQZ0Q6oyAyMF1Ow; ds_user_id=59926273089";

function follow() {
  fetch("https://www.instagram.com/api/v1/friendships/create/173560420/", {
    headers: {
      accept: "*/*",
      "content-type": "application/x-www-form-urlencoded",
      dpr: "1",
      "sec-ch-prefers-color-scheme": "dark",
      "sec-ch-ua":
        '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      "sec-ch-ua-full-version-list":
        '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.189", "Chromium";v="121.0.6167.189"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-model": '""',
      "sec-ch-ua-platform": '"Windows"',
      "sec-ch-ua-platform-version": '"15.0.0"',
      "viewport-width": "1920",
      "x-asbd-id": "129477",
      "x-csrftoken": "lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc",
      "x-ig-app-id": "936619743392459",
      "x-ig-www-claim": "hmac.AR0-Z9qsjV6d9kzC5Ho9jJXHm6Z-XPiw054VbG6I-byK4bNO",
      "x-instagram-ajax": "1011670208",
      "x-requested-with": "XMLHttpRequest",
      Referer: "https://www.instagram.com/",
      "Referrer-Policy": "strict-origin-when-cross-origin",
      cookie,
    },
    body: "container_module=feed_timeline&nav_chain=PolarisFeedRoot%3AfeedPage%3A1%3Avia_cold_start&user_id=173560420",
    method: "POST",
  })
    .then((res) => res.json())
    .then((res) => console.log(res));
}

function unfollow() {
  fetch("https://www.instagram.com/api/v1/friendships/destroy/173560420/", {
    headers: {
      accept: "*/*",
      "content-type": "application/x-www-form-urlencoded",
      dpr: "1",
      "sec-ch-prefers-color-scheme": "dark",
      "sec-ch-ua":
        '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      "sec-ch-ua-full-version-list":
        '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.189", "Chromium";v="121.0.6167.189"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-model": '""',
      "sec-ch-ua-platform": '"Windows"',
      "sec-ch-ua-platform-version": '"15.0.0"',
      "viewport-width": "1920",
      "x-asbd-id": "129477",
      "x-csrftoken": "lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc",
      "x-ig-app-id": "936619743392459",
      "x-ig-www-claim": "hmac.AR0-Z9qsjV6d9kzC5Ho9jJXHm6Z-XPiw054VbG6I-byK4bNO",
      "x-instagram-ajax": "1011670208",
      "x-requested-with": "XMLHttpRequest",
      Referer: "https://www.instagram.com/",
      "Referrer-Policy": "strict-origin-when-cross-origin",
      cookie,
    },
    body: "container_module=feed_timeline&nav_chain=PolarisFeedRoot%3AfeedPage%3A1%3Avia_cold_start&user_id=173560420",
    method: "POST",
  })
    .then((res) => res.json())
    .then((res) => console.log(res));
}

function like() {
  fetch(
    "https://www.instagram.com/api/v1/web/likes/3308285953951901063/like/",
    {
      headers: {
        accept: "*/*",
        "content-type": "application/x-www-form-urlencoded",
        dpr: "1",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua":
          '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-full-version-list":
          '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.189", "Chromium";v="121.0.6167.189"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "viewport-width": "1920",
        "x-asbd-id": "129477",
        "x-csrftoken": "lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim":
          "hmac.AR0-Z9qsjV6d9kzC5Ho9jJXHm6Z-XPiw054VbG6I-byK4bNO",
        "x-instagram-ajax": "1011670208",
        "x-requested-with": "XMLHttpRequest",
        Referer: "https://www.instagram.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        cookie,
      },
      body: "",
      method: "POST",
    }
  )
    .then((res) => res.json())
    .then((res) => console.log(res));
}
function unlike() {
  fetch(
    "https://www.instagram.com/api/v1/web/likes/3308285953951901063/unlike/",
    {
      headers: {
        accept: "*/*",
        "content-type": "application/x-www-form-urlencoded",
        dpr: "1",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua":
          '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-full-version-list":
          '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.189", "Chromium";v="121.0.6167.189"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "viewport-width": "1920",
        "x-asbd-id": "129477",
        "x-csrftoken": "lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim":
          "hmac.AR0-Z9qsjV6d9kzC5Ho9jJXHm6Z-XPiw054VbG6I-byK4bNO",
        "x-instagram-ajax": "1011670208",
        "x-requested-with": "XMLHttpRequest",
        Referer: "https://www.instagram.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        cookie,
      },
      body: "",
      method: "POST",
    }
  )
    .then((res) => res.json())
    .then((res) => console.log(res));
}

// follow()
// unfollow();
// like();
// unlike();
// comment();
