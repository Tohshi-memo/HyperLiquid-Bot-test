# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T16:52:33.919436+00:00`
- Price records: `672`
- Market context records: `6519`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7848`

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

- `news_risk_high->crypto_alt_24h` score `13.2319` n `32` status `ready` deltaP `36.211` edge `0.876` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.5336` n `139` status `ready` deltaP `10.5445` edge `0.8042` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5164` n `32` status `ready` deltaP `53.8995` edge `0.1837` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.912` n `32` status `ready` deltaP `20.911` edge `0.5683` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7121` n `38` status `ready` deltaP `39.3213` edge `0.0518` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.6827` n `181` status `ready` deltaP `-5.4802` edge `0.3502` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.2568` n `32` status `ready` deltaP `23.7164` edge `0.0505` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8035` n `38` status `ready` deltaP `22.6127` edge `0.0176` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.663` n `139` status `ready` deltaP `14.881` edge `0.2262` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6125` n `170` status `ready` deltaP `13.4667` edge `0.0289` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.559` n `38` status `ready` deltaP `4.9007` edge `0.0927` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3364` n `170` status `ready` deltaP `9.8709` edge `0.1176` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0765` n `38` status `ready` deltaP `1.5837` edge `0.0502` maxDD `-2.0756`
- `market_context_high->unknown_4h` score `-0.0736` n `170` status `ready` deltaP `-20.1094` edge `0.3685` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-0.3296` n `170` status `ready` deltaP `10.4143` edge `0.0582` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.339` n `32` status `ready` deltaP `6.1633` edge `0.0026` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.4344` n `181` status `ready` deltaP `-0.5045` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.5039` n `181` status `ready` deltaP `7.227` edge `0.0138` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5126` n `181` status `ready` deltaP `0.7932` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->crypto_major_4h` score `-0.5372` n `170` status `ready` deltaP `11.5477` edge `0.0832` maxDD `-12.6576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
