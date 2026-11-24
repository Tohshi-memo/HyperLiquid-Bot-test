# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T00:07:28.275597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32422.0105` n `45` status `ready` deltaP `2.6147` edge `2701.8262` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22245.6438` n `45` status `ready` deltaP `3.4824` edge `1853.7943` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1212.4811` n `31` status `ready` deltaP `2.8298` edge `101.0388` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1010.2906` n `31` status `ready` deltaP `4.701` edge `84.1652` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.1812` n `31` status `ready` deltaP `43.75` edge `2.8901` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9493` n `31` status `ready` deltaP `45.4861` edge `2.6092` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9312` n `31` status `ready` deltaP `45.6597` edge `2.2732` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.2725` n `31` status `ready` deltaP `44.5341` edge `0.7533` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5012` n `31` status `ready` deltaP `23.2543` edge `0.8071` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6947` n `31` status `ready` deltaP `30.8222` edge `0.5673` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6075` n `31` status `ready` deltaP `56.4684` edge `0.187` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.3968` n `31` status `ready` deltaP `12.8147` edge `0.8764` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9205` n `31` status `ready` deltaP `41.6667` edge `0.2156` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3219` n `45` status `ready` deltaP `39.5393` edge `0.0417` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1833` n `31` status `ready` deltaP `17.5922` edge `0.1667` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9405` n `31` status `ready` deltaP `32.499` edge `0.0544` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4949` n `31` status `ready` deltaP `29.747` edge `0.0181` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4524` n `31` status `ready` deltaP `10.6094` edge `0.2898` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0836` n `31` status `ready` deltaP `10.0106` edge `0.2361` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5469` n `31` status `ready` deltaP `29.8821` edge `0.027` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
