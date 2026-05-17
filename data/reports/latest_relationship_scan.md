# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T23:22:15.665010+00:00`
- Price records: `672`
- Market context records: `1061`
- Flow alert records: `4959`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.1087` n `175` status `ready` deltaP `34.2772` edge `1.0769` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.9423` n `175` status `ready` deltaP `11.7844` edge `0.4567` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.8572` n `175` status `ready` deltaP `12.3097` edge `0.2932` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.0939` n `175` status `ready` deltaP `11.5736` edge `0.2323` maxDD `-2.1308`
- `market_context_high->metal_24h` score `2.6072` n `175` status `ready` deltaP `-6.0325` edge `0.4242` maxDD `-6.3373`
- `market_context_high->fx_1h` score `-0.0758` n `177` status `ready` deltaP `5.3478` edge `0.0002` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.3132` n `177` status `ready` deltaP `7.3421` edge `0.0183` maxDD `-5.4676`
- `market_context_high->equity_4h` score `-0.477` n `177` status `ready` deltaP `2.7689` edge `0.0858` maxDD `-7.1875`
- `market_context_high->index_1h` score `-0.4835` n `177` status `ready` deltaP `3.8406` edge `0.0121` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5162` n `177` status `ready` deltaP `0.3493` edge `0.0274` maxDD `-4.1532`
- `market_context_high->index_4h` score `-0.6376` n `177` status `ready` deltaP `1.1188` edge `0.0473` maxDD `-4.6313`
- `market_context_high->fx_4h` score `-0.7238` n `177` status `ready` deltaP `0.7131` edge `0.0021` maxDD `-1.6381`
- `market_context_high->metal_1h` score `-0.8185` n `177` status `ready` deltaP `4.0149` edge `-0.0309` maxDD `-5.3973`
- `market_context_high->commodity_1h` score `-0.8552` n `177` status `ready` deltaP `-0.1472` edge `0.0105` maxDD `-3.7959`
- `market_context_high->crypto_alt_1h` score `-1.0498` n `177` status `ready` deltaP `1.6053` edge `0.0104` maxDD `-5.3538`
- `market_context_high->crypto_major_4h` score `-2.008` n `177` status `ready` deltaP `8.031` edge `0.0714` maxDD `-16.3819`
- `market_context_high->crypto_alt_4h` score `-2.2828` n `177` status `ready` deltaP `1.6647` edge `0.0491` maxDD `-13.0347`
- `market_context_high->commodity_4h` score `-2.5198` n `177` status `ready` deltaP `-6.3275` edge `0.0359` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-2.8162` n `177` status `ready` deltaP `0.4358` edge `-0.1342` maxDD `-12.047`
- `market_context_high->fx_24h` score `-3.1194` n `175` status `ready` deltaP `4.306` edge `-0.021` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
