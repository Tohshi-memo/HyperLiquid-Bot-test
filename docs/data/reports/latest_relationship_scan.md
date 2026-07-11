# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T06:07:24.592094+00:00`
- Price records: `672`
- Market context records: `6362`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11106`

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

- `news_risk_high->crypto_alt_24h` score `14.8119` n `32` status `ready` deltaP `40.4514` edge `0.9794` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2902` n `32` status `ready` deltaP `52.2569` edge `0.1758` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4506` n `32` status `ready` deltaP `17.7083` edge `0.5305` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0766` n `32` status `ready` deltaP `42.3018` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8951` n `32` status `ready` deltaP `33.6806` edge `0.1206` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3248` n `32` status `ready` deltaP `27.994` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5395` n `32` status `ready` deltaP `15.0262` edge `0.1439` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9486` n `32` status `ready` deltaP `11.9199` edge `0.0883` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7798` n `207` status `ready` deltaP `15.3507` edge `0.0423` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1052` n `207` status `ready` deltaP `8.1301` edge `0.0222` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `0.088` n `218` status `ready` deltaP `-7.1032` edge `0.1555` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.4158` n `218` status `ready` deltaP `3.2783` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.4713` n `129` status `ready` deltaP `-3.4076` edge `0.1487` maxDD `-6.2457`
- `news_risk_high->unknown_1h` score `-0.5631` n `32` status `ready` deltaP `5.4828` edge `-0.049` maxDD `-0.7581`
- `market_context_high->index_1h` score `-0.5993` n `218` status `ready` deltaP `-1.1976` edge `0.0031` maxDD `-0.7564`
- `market_context_high->metal_24h` score `-0.6262` n `129` status `ready` deltaP `15.0839` edge `0.076` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.656` n `207` status `ready` deltaP `5.8626` edge `0.0467` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.705` n `32` status `ready` deltaP `0.5208` edge `-0.0067` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7139` n `218` status `ready` deltaP `-0.6757` edge `-0.0016` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7488` n `32` status `ready` deltaP `-3.1437` edge `-0.0253` maxDD `-1.6464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
