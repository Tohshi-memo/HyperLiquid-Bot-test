# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T05:37:34.955584+00:00`
- Price records: `672`
- Market context records: `6360`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->crypto_alt_24h` score `14.8817` n `32` status `ready` deltaP `40.7986` edge `0.9829` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2576` n `32` status `ready` deltaP `51.9097` edge `0.1754` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4616` n `32` status `ready` deltaP `17.7083` edge `0.5319` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0778` n `32` status `ready` deltaP `42.3018` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8505` n `32` status `ready` deltaP `33.3333` edge `0.1192` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3248` n `32` status `ready` deltaP `27.994` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.531` n `32` status `ready` deltaP `15.0262` edge `0.1428` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9431` n `32` status `ready` deltaP `11.9199` edge `0.0876` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7591` n `205` status `ready` deltaP `15.0914` edge `0.0423` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.078` n `205` status `ready` deltaP `7.8049` edge `0.0221` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `-0.0318` n `216` status `ready` deltaP `-7.5959` edge `0.1488` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3972` n `216` status `ready` deltaP `3.651` edge `0.0025` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5003` n `129` status `ready` deltaP `-3.7549` edge `0.1473` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.5901` n `216` status `ready` deltaP `-1.034` edge `0.0032` maxDD `-0.7564`
- `market_context_high->metal_24h` score `-0.6368` n `129` status `ready` deltaP `14.9103` edge `0.0758` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.6833` n `205` status `ready` deltaP `5.4573` edge `0.0459` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.6867` n `32` status `ready` deltaP `5.4828` edge `-0.0593` maxDD `-0.7581`
- `news_risk_high->index_24h` score `-0.7042` n `32` status `ready` deltaP `0.5208` edge `-0.0066` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7573` n `216` status `ready` deltaP `-1.1727` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7574` n `32` status `ready` deltaP `-3.2934` edge `-0.0254` maxDD `-1.6464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
