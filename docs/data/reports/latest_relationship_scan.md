# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T20:22:27.168425+00:00`
- Price records: `672`
- Market context records: `6318`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.387` n `32` status `ready` deltaP `43.2292` edge `1.0088` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0241` n `32` status `ready` deltaP `50.5208` edge `0.1652` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3278` n `32` status `ready` deltaP `16.6667` edge `0.5217` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2033` n `32` status `ready` deltaP `43.8262` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3455` n `32` status `ready` deltaP `30.0347` edge `0.0991` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4123` n `32` status `ready` deltaP `29.0419` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4749` n `32` status `ready` deltaP `14.5771` edge `0.1386` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9353` n `32` status `ready` deltaP `11.7702` edge `0.0876` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.3461` n `208` status `ready` deltaP `-5.6022` edge `0.167` maxDD `-3.7317`
- `market_context_high->metal_4h` score `-0.019` n `196` status `ready` deltaP `8.6455` edge `0.0371` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1819` n `156` status `ready` deltaP `20.4193` edge `0.0974` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4443` n `208` status `ready` deltaP `2.9249` edge `0.0013` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.5121` n `32` status `ready` deltaP `3.6458` edge `-0.0028` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.5929` n `208` status `ready` deltaP `-1.0796` edge `-0.0005` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.6913` n `196` status `ready` deltaP `3.1919` edge `0.0186` maxDD `-1.2805`
- `news_risk_high->metal_1h` score `-0.7286` n `32` status `ready` deltaP `-2.8443` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7531` n `208` status `ready` deltaP `-1.2466` edge `-0.0021` maxDD `-0.8545`
- `market_context_high->index_1h` score `-0.8778` n `208` status `ready` deltaP `-4.1139` edge `0.0018` maxDD `-0.9531`
- `news_risk_high->unknown_1h` score `-0.917` n `32` status `ready` deltaP `4.7343` edge `-0.0735` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-0.9996` n `208` status `ready` deltaP `4.799` edge `0.0151` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
