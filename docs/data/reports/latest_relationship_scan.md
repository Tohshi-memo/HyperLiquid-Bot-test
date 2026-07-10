# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T15:22:30.113825+00:00`
- Price records: `672`
- Market context records: `6295`
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

- `news_risk_high->crypto_alt_24h` score `15.2418` n `32` status `ready` deltaP `43.2292` edge `0.9967` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9713` n `32` status `ready` deltaP `50.5208` edge `0.1608` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1913` n `32` status `ready` deltaP `43.8262` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1383` n `32` status `ready` deltaP `16.6667` edge `0.4974` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.001` n `32` status `ready` deltaP `27.6042` edge `0.0866` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4335` n `32` status `ready` deltaP `14.2777` edge `0.1353` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.1368` n `208` status `ready` deltaP `-1.1486` edge `0.2032` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9252` n `32` status `ready` deltaP `11.7702` edge `0.0863` maxDD `-1.6923`
- `market_context_high->metal_4h` score `-0.1026` n `196` status `ready` deltaP `7.9299` edge `0.0349` maxDD `-2.7056`
- `market_context_high->equity_4h` score `-0.118` n `196` status `ready` deltaP `6.9562` edge `0.0598` maxDD `-4.6142`
- `market_context_high->metal_24h` score `-0.1593` n `176` status `ready` deltaP `20.3441` edge `0.1008` maxDD `-11.8809`
- `market_context_high->unknown_4h` score `-0.1843` n `196` status `ready` deltaP `-5.0896` edge `0.2718` maxDD `-11.925`
- `news_risk_high->index_24h` score `-0.3505` n `32` status `ready` deltaP `6.4236` edge `-0.0006` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4318` n `208` status `ready` deltaP `3.256` edge `0.0007` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5204` n `208` status `ready` deltaP `-0.4174` edge `-0.0007` maxDD `-1.7253`
- `market_context_high->fx_1h` score `-0.7082` n `208` status `ready` deltaP `-0.9155` edge `-0.0019` maxDD `-0.748`
- `news_risk_high->metal_1h` score `-0.734` n `32` status `ready` deltaP `-2.994` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->index_4h` score `-0.9654` n `196` status `ready` deltaP `1.4031` edge `0.0133` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.9778` n `208` status `ready` deltaP `4.799` edge `0.0179` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
