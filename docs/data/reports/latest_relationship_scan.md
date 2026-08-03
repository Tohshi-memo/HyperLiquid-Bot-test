# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T13:52:37.099019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->unknown_24h` score `79.257` n `40` status `ready` deltaP `30.3819` edge `6.4022` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.4572` n `40` status `ready` deltaP `51.2847` edge `0.6526` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8095` n `40` status `ready` deltaP `51.1458` edge `0.5726` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.4008` n `31` status `ready` deltaP `-6.668` edge `0.2296` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9934` n `31` status `ready` deltaP `20.5862` edge `0.0113` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9377` n `31` status `ready` deltaP `12.192` edge `0.0621` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3915` n `47` status `ready` deltaP `8.1634` edge `0.0332` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3712` n `31` status `ready` deltaP `14.1621` edge `-0.0134` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.3185` n `47` status `ready` deltaP `5.0338` edge `0.0919` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.2177` n `31` status `ready` deltaP `0.2409` edge `0.0546` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1391` n `31` status `ready` deltaP `4.8928` edge `0.0355` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.0182` n `31` status `ready` deltaP `11.2903` edge `-0.0089` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0099` n `31` status `ready` deltaP `3.6411` edge `-0.0032` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0248` n `47` status `ready` deltaP `6.6664` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1497` n `47` status `ready` deltaP `11.8935` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.2357` n `31` status `ready` deltaP `-0.2656` edge `0.0027` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5552` n `31` status `ready` deltaP `-2.062` edge `-0.0006` maxDD `-0.5538`
- `market_context_high->crypto_alt_4h` score `-0.6175` n `47` status `ready` deltaP `0.3146` edge `0.0093` maxDD `-4.9116`
- `market_context_high->fx_24h` score `-0.6743` n `40` status `ready` deltaP `0.6597` edge `0.0374` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.8072` n `31` status `ready` deltaP `3.1099` edge `-0.0522` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
