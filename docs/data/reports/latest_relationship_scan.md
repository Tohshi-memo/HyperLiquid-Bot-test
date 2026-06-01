# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T04:52:19.304676+00:00`
- Price records: `672`
- Market context records: `2530`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_alt_4h` score `5.0445` n `161` status `ready` deltaP `23.4557` edge `0.5319` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.7438` n `118` status `ready` deltaP `19.4768` edge `0.2983` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.5423` n `161` status `ready` deltaP `16.7986` edge `0.3642` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.4509` n `118` status `ready` deltaP `12.1704` edge `0.6051` maxDD `-24.0946`
- `market_context_high->unknown_4h` score `1.9546` n `161` status `ready` deltaP `11.3041` edge `0.1925` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1166` n `161` status `ready` deltaP `9.1178` edge `0.151` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.679` n `161` status `ready` deltaP `8.0253` edge `0.1225` maxDD `-4.2199`
- `market_context_high->index_4h` score `-0.0393` n `161` status `ready` deltaP `6.9857` edge `0.0343` maxDD `-2.3986`
- `market_context_high->crypto_alt_24h` score `-0.0417` n `118` status `ready` deltaP `0.409` edge `0.6841` maxDD `-43.3741`
- `market_context_high->index_24h` score `-0.1003` n `118` status `ready` deltaP `2.9572` edge `0.07` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1513` n `118` status `ready` deltaP `17.3435` edge `0.0171` maxDD `-6.6264`
- `market_context_high->commodity_1h` score `-0.3578` n `161` status `ready` deltaP `4.2539` edge `0.0136` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4362` n `161` status `ready` deltaP `1.1325` edge `0.0055` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4722` n `161` status `ready` deltaP `2.2185` edge `0.0161` maxDD `-2.9523`
- `market_context_high->metal_1h` score `-0.4862` n `161` status `ready` deltaP `0.7373` edge `0.0087` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5162` n `161` status `ready` deltaP `0.954` edge `0.0041` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.798` n `161` status `ready` deltaP `0.1135` edge `0.0166` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8187` n `161` status `ready` deltaP `0.8019` edge `0.0124` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8959` n `118` status `ready` deltaP `2.4511` edge `0.0038` maxDD `-2.4663`
- `market_context_high->metal_4h` score `-0.9032` n `161` status `ready` deltaP `3.1615` edge `0.0424` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
