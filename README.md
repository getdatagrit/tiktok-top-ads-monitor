# TikTok Top Ads Monitor: New Ads by Industry

Daily monitor of TikTok Creative Center Top Ads: new ads per country, industry and objective with CTR, likes, landing page and video links, no login.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/tiktok-top-ads-monitor) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/tiktok-top-ads-monitor/)

**from $2.10 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

TikTok Top Ads Monitor reads the public **TikTok Creative Center Top Ads** ranking for the countries, industries and campaign objectives you choose and returns every ad as one clean row: title, brand, industry, objective, likes, CTR, video and cover links, and, when you ask for details, the landing page, comments, shares and the countries the ad ran in. No login and no cookies are needed. Turn on **Only new ads** and schedule the Actor, and each run returns just the ads that entered your ranking since the last run, so a daily run is a feed of fresh winning creatives instead of the same top 20 again.

## Quick start

1. Open [TikTok Top Ads Monitor: New Ads by Industry on Apify Store](https://apify.com/datagrit/tiktok-top-ads-monitor) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "countries": [
    "US",
    "GB"
  ],
  "sortBy": [
    "for_you",
    "ctr"
  ],
  "periodDays": "7",
  "includeDetails": true,
  "maxItems": 50
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `countries` | array | Countries whose Top Ads ranking to read. Use two-letter codes or names. Each country is read separately and the same ad found in several lists is returned once. Available: AR Argentina, AU Australia, BR Brazil, CA Canada, CO Colombia, FR France, DE Germany, ID Indonesia, IT Italy, JP Japan, MY Malaysia, MX Mexico, NL Netherlands, PK Pakistan, PH Philippines, RO Romania, SA Saudi Arabia, SG Singapore, ZA South Africa, KR South Korea, ES Spain, SE Sweden, TH Thailand, TR Turkey, AE United Arab Emirates, GB United Kingdom, US United States, VN Vietnam. |
| `periodDays` | string | Window the Top Ads ranking is calculated over. |
| `sortBy` | array | Ranking orders to read. Each order returns a different top 20, so several orders widen coverage. Ads found in more than one are returned once with their best rank. Available: for_you (default ranking), ctr, like, impression, cvr (conversion rate). |
| `industries` | array | Limit to these top-level industries. Leave empty for all industries. Available: Apparel & Accessories, Appliances, Apps, Baby, Kids & Maternity, Beauty & Personal Care, Business Services, E-Commerce (Non-app), Education, Financial Services, Food & Beverage, Games, Health, Home Improvement, Household Products, Life Services, News & Entertainment, Pets, Sports & Outdoor, Tech & Electronics, Travel, Vehicle & Transportation. |
| `objectives` | array | Limit to these campaign objectives. Leave empty for all objectives. Available: Traffic, App Installs, Conversions, Video Views, Reach, Lead Generation, Product sales. |
| `adLanguages` | array | Limit to ads in these languages, by code. Leave empty for all languages. Available: en English, es Spanish, ar Arabic, vi Vietnamese, th Thai, de German, id Indonesian, pt Portuguese, fr French, ms Malay, nl Dutch, ja Japanese, it Italian, ro Romanian, zh-Hant Traditional Chinese, ko Korean. |
| `onlyNew` | boolean | Return only ads not delivered by an earlier run with the same countries, industries, objectives, languages, sort orders and period. Turn on for a daily or weekly monitor; the first run returns everything. |
| `includeDetails` | boolean | Read each ad detail for its landing page, comments, shares and the countries it ran in. Adds one request per ad; turn off for a faster list-only run. |
| `maxItems` | integer | Stop after this many ads in total across all lists. |
| `proxyConfiguration` | object | Optional proxy. Leave disabled unless TikTok blocks datacenter traffic from your location; residential proxy raises the platform cost of the run. |

## Output

| Field | Type | Description |
|---|---|---|
| `adId` | string | TikTok Creative Center material ID of the ad. Empty only on the status row. |
| `title` | string | Caption of the ad as shown in Top Ads, hashtags included. |
| `brandName` | string | Advertiser or brand name when Creative Center shows one; many ads have none. |
| `industry` | string | Most specific Creative Center industry of the ad, for example Hotels & Accommodation. Empty when Creative Center uses a code missing from its own industry list. |
| `industryGroup` | string | Top-level Creative Center industry, for example Travel. This is the value the Industries input filters on. |
| `objective` | string | Campaign objective of the ad, for example Conversions or Video Views. |
| `likes` | integer | Number of likes on the ad. |
| `comments` | integer | Number of comments. Empty when details were not read or failed. |
| `shares` | integer | Number of shares. Empty when details were not read or failed. |
| `ctr` | number | Click-through rate in percent as ranked by Creative Center. |
| `costLevel` | integer | Creative Center cost bracket of the ad, from 1 (lowest) upward. |
| `durationSeconds` | number | Video length in seconds. |
| `videoWidth` | integer | Video width in pixels. |
| `videoHeight` | integer | Video height in pixels. |
| `coverUrl` | string | Signed link to the cover image on the TikTok CDN. The link expires after a few days; download the image if you need to keep it. |
| `videoUrl720p` | string | Signed link to the 720p video on the TikTok CDN. Expires after a few days. |
| `videoUrl1080p` | string | Signed link to the 1080p video on the TikTok CDN. Expires after a few days. |
| `landingPage` | string | Landing page URL of the ad as stored by Creative Center, tracking macros such as __CID__ left as they are. Empty when the ad has none or details were not read. |
| `landingDomain` | string | Domain of the landing page without www. |
| `adSource` | string | Tool the ad was made with, for example TikTok Ads Manager, TikTok Video Editor or Others. Empty when details were not read. |
| `shownInCountries` | array | Country codes the ad ran in. Empty when details were not read. |
| `bestRank` | integer | Best position of the ad (1 is top) across the lists it appeared in. |
| `matchedSlices` | array | Every list the ad appeared in, as country \| period \| sort order \| industry \| objective \| language. On the status row, all lists that were read. |
| `isNew` | boolean | True when no earlier run with the same countries, industries, objectives, languages, sort orders and period delivered this ad. On the first run every ad is new. |
| `firstSeenAt` | string | ISO 8601 time this monitor first delivered the ad; the current run time for new ads. |
| `timesSeen` | integer | How many runs of this monitor have delivered the ad, this run included. |
| `detailStatus` | string | ok when the ad detail was read, failed when the detail request failed, notRequested when Include ad details was off. |
| `sourceUrl` | string | Creative Center page of the ad. Empty only on the status row. |
| `found` | boolean | False only for the single status row emitted when no ad matched. |
| `scrapedAt` | string | ISO 8601 timestamp of extraction. |

Sample record:

```json
{
  "adId": "7687879583547113492",
  "title": "Discover a slower side of Dubai #UnforgettableJourneys",
  "brandName": "Anantara",
  "industry": "Hotels & Accommodation",
  "industryGroup": "Travel",
  "objective": "Video Views",
  "likes": 554,
  "comments": 3,
  "shares": 0,
  "ctr": 0.95,
  "costLevel": 1,
  "durationSeconds": 14.08,
  "videoWidth": 576,
  "videoHeight": 1024,
  "coverUrl": "https://p16-common-sign.tiktokcdn.com/example.image",
  "videoUrl720p": "https://v16m-default.tiktokcdn.com/example.mp4",
  "videoUrl1080p": "https://v16m-default.tiktokcdn.com/example-1080.mp4",
  "landingPage": "https://example.com/product?utm_source=tiktok",
  "landingDomain": "example.com",
  "adSource": "TikTok Ads Manager",
  "shownInCountries": [
    "US",
    "GB"
  ],
  "bestRank": 3,
  "matchedSlices": [
    "US | 7d | for_you"
  ],
  "isNew": true,
  "firstSeenAt": "2026-10-05T08:00:00.000Z",
  "timesSeen": 1,
  "detailStatus": "ok",
  "sourceUrl": "https://ads.tiktok.com/business/creativecenter/topads/7687879583547113492/pc/en",
  "found": true,
  "scrapedAt": "2026-10-05T08:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~tiktok-top-ads-monitor/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"countries":["US","GB"],"sortBy":["for_you","ctr"],"periodDays":"7","includeDetails":true,"maxItems":50}'
```


## More from datagrit

- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.
- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.
- [Poland KRS New Company Registrations Feed](https://github.com/getdatagrit/poland-krs-new-companies) - Newly registered Polish companies, foundations and associations from the official KRS court register: NIP, address, PKD, capital, email, with filters and change detection.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/tiktok-top-ads-monitor). Examples are MIT licensed.
