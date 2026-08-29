# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T08:07:24.766749+00:00`
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

- `news_risk_high->unknown_24h` score `55.2184` n `52` status `ready` deltaP `19.0705` edge `4.492` maxDD `-0.7415`
- `news_risk_high->crypto_alt_24h` score `29.9896` n `52` status `ready` deltaP `42.8285` edge `2.3139` maxDD `-6.6896`
- `market_context_high->unknown_24h` score `8.1072` n `120` status `ready` deltaP `16.25` edge `0.6405` maxDD `-3.1917`
- `news_risk_high->crypto_major_24h` score `7.3716` n `52` status `ready` deltaP `24.8664` edge `0.5602` maxDD `-7.6009`
- `news_risk_high->unknown_4h` score `6.3125` n `80` status `ready` deltaP `10.5183` edge `0.5149` maxDD `-1.7183`
- `news_risk_high->equity_24h` score `6.2569` n `52` status `ready` deltaP `27.297` edge `0.4601` maxDD `-6.9872`
- `news_risk_high->metal_24h` score `3.9239` n `52` status `ready` deltaP `41.1058` edge `0.0764` maxDD `-1.2092`
- `market_context_high->metal_24h` score `3.5948` n `120` status `ready` deltaP `30.2083` edge `0.2001` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7424` n `80` status `ready` deltaP `5.524` edge `0.2274` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.6044` n `120` status `ready` deltaP `19.685` edge `0.1265` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2901` n `80` status `ready` deltaP `33.5976` edge `0.0218` maxDD `-0.3953`
- `news_risk_high->index_24h` score `2.1319` n `52` status `ready` deltaP `23.8515` edge `0.0372` maxDD `-0.4841`
- `market_context_high->unknown_1h` score `1.3162` n `120` status `ready` deltaP `9.6907` edge `0.0901` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6501` n `80` status `ready` deltaP `13.1437` edge `0.0054` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4743` n `80` status `ready` deltaP `13.0988` edge `0.0055` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1431` n `120` status `ready` deltaP `9.4918` edge `0.0101` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.325` n `120` status `ready` deltaP `4.8104` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3825` n `80` status `ready` deltaP `0.4566` edge `-0.0084` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5538` n `80` status `ready` deltaP `7.8049` edge `0.0111` maxDD `-2.0635`
- `news_risk_high->index_4h` score `-0.561` n `80` status `ready` deltaP `1.311` edge `-0.0165` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
