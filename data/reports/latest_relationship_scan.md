# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T20:47:15.720395+00:00`
- Price records: `672`
- Market context records: `5386`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `5.8952` n `189` status `ready` deltaP `16.9478` edge `0.3913` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.3685` n `189` status `ready` deltaP `22.9498` edge `0.7484` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.5407` n `205` status `ready` deltaP `15.0915` edge `0.4237` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0362` n `205` status `ready` deltaP `12.2256` edge `0.3356` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.2885` n `205` status `ready` deltaP `10.9757` edge `0.2814` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.3809` n `189` status `ready` deltaP `10.1191` edge `0.6105` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.4117` n `205` status `ready` deltaP `7.4602` edge `0.0811` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1017` n `205` status `ready` deltaP `4.7736` edge `0.1012` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0696` n `205` status `ready` deltaP `2.5281` edge `0.0851` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0448` n `205` status `ready` deltaP `5.5762` edge `0.0159` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.2379` n `189` status `ready` deltaP `6.0764` edge `0.0292` maxDD `-0.8294`
- `market_context_high->unknown_4h` score `-0.4377` n `205` status `ready` deltaP `8.1402` edge `0.0277` maxDD `-6.1421`
- `market_context_high->metal_1h` score `-0.4579` n `205` status `ready` deltaP `2.2287` edge `0.0145` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4649` n `205` status `ready` deltaP `-1.4028` edge `-0.0013` maxDD `-0.5823`
- `market_context_high->index_24h` score `-0.8169` n `189` status `ready` deltaP `14.6412` edge `0.0809` maxDD `-10.0598`
- `market_context_high->index_4h` score `-1.0381` n `205` status `ready` deltaP `5.7926` edge `0.0358` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2035` n `205` status `ready` deltaP `0.2439` edge `0.001` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4927` n `205` status `ready` deltaP `-3.4701` edge `-0.0068` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.444` n `205` status `ready` deltaP `-5.4573` edge `-0.0245` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1251` n `189` status `ready` deltaP `13.9137` edge `0.3763` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
