# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T16:07:27.492574+00:00`
- Price records: `672`
- Market context records: `6298`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.2526` n `32` status `ready` deltaP `43.2292` edge `0.9976` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9773` n `32` status `ready` deltaP `50.5208` edge `0.1613` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1937` n `32` status `ready` deltaP `43.8262` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1555` n `32` status `ready` deltaP `16.6667` edge `0.4996` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.0895` n `32` status `ready` deltaP `28.125` edge `0.0905` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4507` n `32` status `ready` deltaP `14.4274` edge `0.1365` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.0419` n `208` status `ready` deltaP `-1.4797` edge `0.1975` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9283` n `32` status `ready` deltaP `11.7702` edge `0.0867` maxDD `-1.6923`
- `market_context_high->metal_4h` score `-0.0274` n `196` status `ready` deltaP `8.6455` edge `0.0364` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1151` n `173` status `ready` deltaP `21.1023` edge `0.1014` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.3689` n `196` status `ready` deltaP `6.5984` edge `0.0522` maxDD `-6.8119`
- `news_risk_high->index_24h` score `-0.3709` n `32` status `ready` deltaP `6.0764` edge `-0.0009` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3716` n `208` status `ready` deltaP `4.2492` edge `0.0018` maxDD `-1.8877`
- `market_context_high->unknown_4h` score `-0.4682` n `196` status `ready` deltaP `-6.1629` edge `0.2553` maxDD `-11.925`
- `market_context_high->commodity_1h` score `-0.6334` n `208` status `ready` deltaP `-1.4106` edge `-0.0036` maxDD `-2.123`
- `market_context_high->fx_1h` score `-0.7093` n `208` status `ready` deltaP `-0.9155` edge `-0.002` maxDD `-0.7472`
- `news_risk_high->metal_1h` score `-0.7621` n `32` status `ready` deltaP `-3.4431` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.8465` n `208` status `ready` deltaP `-3.4517` edge `0.0014` maxDD `-0.9531`
- `market_context_high->index_4h` score `-0.9608` n `196` status `ready` deltaP `1.4031` edge `0.0139` maxDD `-1.381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
