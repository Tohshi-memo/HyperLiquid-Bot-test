# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T08:22:24.285514+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `news_risk_high->unknown_24h` score `55.2899` n `52` status `ready` deltaP `19.2441` edge `4.4968` maxDD `-0.7415`
- `news_risk_high->crypto_alt_24h` score `29.9548` n `52` status `ready` deltaP `42.8285` edge `2.311` maxDD `-6.6896`
- `market_context_high->unknown_24h` score `8.1787` n `120` status `ready` deltaP `16.4236` edge `0.6453` maxDD `-3.1917`
- `news_risk_high->crypto_major_24h` score `7.3788` n `52` status `ready` deltaP `24.8664` edge `0.5608` maxDD `-7.6009`
- `news_risk_high->unknown_4h` score `6.3113` n `80` status `ready` deltaP `10.5183` edge `0.5148` maxDD `-1.7183`
- `news_risk_high->equity_24h` score `6.2833` n `52` status `ready` deltaP `27.297` edge `0.4623` maxDD `-6.9872`
- `news_risk_high->metal_24h` score `3.9522` n `52` status `ready` deltaP `41.2794` edge `0.0776` maxDD `-1.2092`
- `market_context_high->metal_24h` score `3.6231` n `120` status `ready` deltaP `30.3819` edge `0.2013` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7447` n `80` status `ready` deltaP `5.524` edge `0.2276` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.6032` n `120` status `ready` deltaP `19.685` edge `0.1264` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2901` n `80` status `ready` deltaP `33.5976` edge `0.0218` maxDD `-0.3953`
- `news_risk_high->index_24h` score `2.1331` n `52` status `ready` deltaP `23.8515` edge `0.0373` maxDD `-0.4841`
- `market_context_high->unknown_1h` score `1.3186` n `120` status `ready` deltaP `9.6907` edge `0.0903` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6381` n `80` status `ready` deltaP `12.994` edge `0.0054` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.482` n `80` status `ready` deltaP `13.2485` edge `0.0055` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1431` n `120` status `ready` deltaP `9.4918` edge `0.0101` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3328` n `120` status `ready` deltaP `4.6607` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3832` n `80` status `ready` deltaP `0.4566` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5538` n `80` status `ready` deltaP `7.8049` edge `0.0111` maxDD `-2.0635`
- `news_risk_high->index_4h` score `-0.5689` n `80` status `ready` deltaP `1.1585` edge `-0.0165` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
