# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T16:37:20.599554+00:00`
- Price records: `672`
- Market context records: `2159`
- Flow alert records: `8110`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.5692` n `143` status `ready` deltaP `37.5746` edge `0.9739` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8864` n `143` status `ready` deltaP `41.6446` edge `0.7659` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.9818` n `143` status `ready` deltaP `24.225` edge `0.4119` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.3731` n `143` status `ready` deltaP `25.4062` edge `0.3045` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0906` n `40` status `ready` deltaP `31.5244` edge `0.3814` maxDD `-3.0367`
- `market_context_high->crypto_major_1h` score `3.4143` n `143` status `ready` deltaP `18.0803` edge `0.2117` maxDD `-1.817`
- `market_context_high->index_24h` score `3.3458` n `143` status `ready` deltaP `13.1787` edge `0.3138` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `3.289` n `143` status `ready` deltaP `16.733` edge `0.2489` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.1696` n `143` status `ready` deltaP `23.7293` edge `0.1743` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.7482` n `143` status `ready` deltaP `27.4585` edge `0.578` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.5247` n `40` status `ready` deltaP `31.7073` edge `0.0174` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.507` n `143` status `ready` deltaP `24.9988` edge `0.5321` maxDD `-33.1875`
- `market_context_high->metal_4h` score `2.4646` n `143` status `ready` deltaP `20.0292` edge `0.2106` maxDD `-4.7664`
- `market_context_high->crypto_major_24h` score `2.1647` n `143` status `ready` deltaP `20.1754` edge `1.0016` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.5422` n `40` status `ready` deltaP `15.3963` edge `0.0982` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0807` n `43` status `ready` deltaP `19.0189` edge `0.0102` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.776` n `43` status `ready` deltaP `10.4651` edge `0.0977` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7709` n `143` status `ready` deltaP `10.3472` edge `0.0741` maxDD `-2.6402`
- `news_risk_high->equity_4h` score `0.5665` n `40` status `ready` deltaP `-4.9085` edge `0.2261` maxDD `-4.6598`
- `market_context_high->metal_1h` score `0.5637` n `143` status `ready` deltaP `9.1904` edge `0.0527` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
