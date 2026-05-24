# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T18:07:17.174747+00:00`
- Price records: `672`
- Market context records: `1762`
- Flow alert records: `6973`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1945` n `171` status `ready` deltaP `27.7869` edge `0.6569` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.1726` n `195` status `ready` deltaP `21.7949` edge `0.5457` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.705` n `195` status `ready` deltaP `23.3615` edge `0.4769` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.0431` n `171` status `ready` deltaP `18.8048` edge `0.3344` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.2849` n `171` status `ready` deltaP `14.8026` edge `0.7071` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.2111` n `195` status `ready` deltaP `17.3608` edge `0.2613` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.1019` n `30` status `ready` deltaP `24.2715` edge `0.1284` maxDD `-1.2043`
- `market_context_high->unknown_4h` score `3.0315` n `195` status `ready` deltaP `13.3271` edge `0.3909` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.8627` n `171` status `ready` deltaP `17.1601` edge `0.614` maxDD `-33.1875`
- `market_context_high->index_4h` score `1.0132` n `195` status `ready` deltaP `12.6203` edge `0.1092` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7774` n `195` status `ready` deltaP `7.4328` edge `0.1176` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.6558` n `171` status `ready` deltaP `19.2799` edge `0.7847` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2527` n `195` status `ready` deltaP `4.891` edge `0.0958` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0892` n `195` status `ready` deltaP `5.1428` edge `0.054` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1501` n `195` status `ready` deltaP `4.3751` edge `0.0215` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1976` n `195` status `ready` deltaP `12.758` edge `0.1588` maxDD `-12.5349`
- `news_risk_high->fx_1h` score `-0.5091` n `30` status `ready` deltaP `-5.7285` edge `-0.0009` maxDD `-0.0948`
- `market_context_high->metal_1h` score `-0.5172` n `195` status `ready` deltaP `5.7255` edge `0.0291` maxDD `-6.3532`
- `news_risk_high->unknown_1h` score `-0.5409` n `30` status `ready` deltaP `16.2575` edge `-0.1305` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.5583` n `171` status `ready` deltaP `7.5566` edge `0.008` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
