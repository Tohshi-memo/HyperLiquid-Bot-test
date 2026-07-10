# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T15:52:31.888836+00:00`
- Price records: `672`
- Market context records: `6297`
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

- `news_risk_high->crypto_alt_24h` score `15.2538` n `32` status `ready` deltaP `43.2292` edge `0.9977` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9749` n `32` status `ready` deltaP `50.5208` edge `0.1611` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1937` n `32` status `ready` deltaP `43.8262` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1523` n `32` status `ready` deltaP `16.6667` edge `0.4992` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.0636` n `32` status `ready` deltaP `27.9514` edge `0.0895` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4491` n `32` status `ready` deltaP `14.4274` edge `0.1363` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.0479` n `208` status `ready` deltaP `-1.4797` edge `0.198` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9275` n `32` status `ready` deltaP `11.7702` edge `0.0866` maxDD `-1.6923`
- `market_context_high->metal_4h` score `-0.0322` n `196` status `ready` deltaP `8.6455` edge `0.036` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1145` n `174` status `ready` deltaP `21.1147` edge `0.1014` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3611` n `32` status `ready` deltaP `6.25` edge `-0.0008` maxDD `-2.3058`
- `market_context_high->unknown_4h` score `-0.3796` n `196` status `ready` deltaP `-5.8051` edge `0.2603` maxDD `-11.925`
- `market_context_high->metal_1h` score `-0.3919` n `208` status `ready` deltaP `3.9181` edge `0.0014` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.4344` n `196` status `ready` deltaP `6.9562` edge `0.0543` maxDD `-6.2835`
- `market_context_high->commodity_1h` score `-0.6096` n `208` status `ready` deltaP `-1.0796` edge `-0.0031` maxDD `-2.0952`
- `market_context_high->fx_1h` score `-0.7064` n `208` status `ready` deltaP `-0.9155` edge `-0.0019` maxDD `-0.7358`
- `news_risk_high->metal_1h` score `-0.7527` n `32` status `ready` deltaP `-3.2934` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.8661` n `208` status `ready` deltaP `-3.7828` edge `0.0011` maxDD `-0.9531`
- `market_context_high->index_4h` score `-0.9631` n `196` status `ready` deltaP `1.4031` edge `0.0136` maxDD `-1.381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
