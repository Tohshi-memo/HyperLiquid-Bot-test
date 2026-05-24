# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T00:16:05.035034+00:00`
- Price records: `672`
- Market context records: `1682`
- Flow alert records: `6750`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `8.2588` n `152` status `ready` deltaP `27.0806` edge `0.7503` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.263` n `195` status `ready` deltaP `22.8901` edge `0.5524` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8886` n `152` status `ready` deltaP `18.5326` edge `0.3383` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.5383` n `195` status `ready` deltaP `20.0766` edge `0.4319` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.8702` n `195` status `ready` deltaP `15.7255` edge `0.2438` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.5067` n `152` status `ready` deltaP `14.69` edge `0.643` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.9044` n `152` status `ready` deltaP `17.6311` edge `0.531` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.5068` n `204` status `ready` deltaP `5.3393` edge `0.109` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4185` n `152` status `ready` deltaP `25.0774` edge `1.0486` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.1566` n `195` status `ready` deltaP `6.0373` edge `0.0817` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `-0.0853` n `152` status `ready` deltaP `23.8277` edge `0.6888` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.127` n `204` status `ready` deltaP `3.3404` edge `0.048` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.3934` n `204` status `ready` deltaP `3.2553` edge `0.0729` maxDD `-5.5244`
- `market_context_high->metal_1h` score `-0.5473` n `204` status `ready` deltaP `7.0682` edge `0.0163` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.5515` n `204` status `ready` deltaP `0.3317` edge `0.015` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.5853` n `195` status `ready` deltaP `12.6469` edge `0.1361` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.6179` n `152` status `ready` deltaP `5.8368` edge `0.0145` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.9115` n `204` status `ready` deltaP `-1.5645` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.8488` n `195` status `ready` deltaP `-7.6016` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1569` n `204` status `ready` deltaP `0.1233` edge `-0.0319` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
