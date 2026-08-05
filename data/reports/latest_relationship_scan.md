# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T09:52:35.634174+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `14.4076` n `88` status `ready` deltaP `10.6692` edge `1.1338` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4383` n `92` status `ready` deltaP `2.2402` edge `0.5378` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7071` n `92` status `ready` deltaP `18.1336` edge `0.106` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1785` n `88` status `ready` deltaP `27.7304` edge `0.0868` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8749` n `88` status `ready` deltaP `1.231` edge `0.2208` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.3158` n `93` status `ready` deltaP `6.2134` edge `0.0265` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0851` n `92` status `ready` deltaP `13.4411` edge `0.0073` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0241` n `93` status `ready` deltaP `6.1458` edge `-0.004` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4533` n `93` status `ready` deltaP `-0.2511` edge `-0.007` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5447` n `93` status `ready` deltaP `0.2801` edge `-0.0183` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8152` n `93` status `ready` deltaP `-2.6334` edge `-0.0159` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.8974` n `92` status `ready` deltaP `1.7431` edge `-0.0032` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3366` n `88` status `ready` deltaP `1.6572` edge `-0.0381` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5249` n `92` status `ready` deltaP `-0.7224` edge `-0.0517` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6726` n `93` status `ready` deltaP `4.1595` edge `-0.0886` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1266` n `92` status `ready` deltaP `-13.1694` edge `-0.0594` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3187` n `88` status `ready` deltaP `-9.6275` edge `-0.0136` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.2667` n `93` status `ready` deltaP `3.0697` edge `-0.248` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3552` n `93` status `ready` deltaP `-11.1406` edge `-0.068` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0303` n `88` status `ready` deltaP `9.7853` edge `-0.0422` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
