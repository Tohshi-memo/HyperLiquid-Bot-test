# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T03:37:28.358712+00:00`
- Price records: `672`
- Market context records: `6153`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `12.1524` n `30` status `ready` deltaP `42.2916` edge `0.7455` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.6281` n `30` status `ready` deltaP `67.3611` edge `0.1866` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2653` n `32` status `ready` deltaP `44.436` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3787` n `32` status `ready` deltaP `28.5928` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6662` n `195` status `ready` deltaP `0.9543` edge `0.2333` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3135` n `32` status `ready` deltaP `13.9783` edge `0.1219` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7156` n `32` status `ready` deltaP `9.2253` edge `0.0764` maxDD `-1.6923`
- `news_risk_high->crypto_major_24h` score `0.6826` n `30` status `ready` deltaP `12.9861` edge `0.0789` maxDD `-4.2368`
- `market_context_high->equity_4h` score `0.0116` n `195` status `ready` deltaP `2.6829` edge `0.0748` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2274` n `30` status `ready` deltaP `7.5` edge `0.008` maxDD `-2.3058`
- `market_context_high->unknown_4h` score `-0.2745` n `195` status `ready` deltaP `-2.0021` edge `0.2437` maxDD `-11.925`
- `market_context_high->fx_1h` score `-0.284` n `195` status `ready` deltaP `1.2851` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3005` n `195` status `ready` deltaP `18.4669` edge `0.0952` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5746` n `195` status `ready` deltaP `4.1518` edge `0.0174` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6055` n `30` status `ready` deltaP `14.0973` edge `-0.1239` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.7216` n `32` status `ready` deltaP `-2.3952` edge `-0.0268` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7445` n `195` status `ready` deltaP `2.9894` edge `-0.0021` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.7631` n `195` status `ready` deltaP `-2.1388` edge `-0.0047` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.8499` n `195` status `ready` deltaP `-1.4571` edge `0.0123` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.8603` n `195` status `ready` deltaP `4.2093` edge `0.0369` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
