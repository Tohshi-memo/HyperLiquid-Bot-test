# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T19:22:24.614422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1492.6753` n `98` status `ready` deltaP `3.4662` edge `124.3665` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.5773` n `40` status `ready` deltaP `67.4957` edge `4.5021` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.1482` n `40` status `ready` deltaP `55.4878` edge `1.3091` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.2702` n `40` status `ready` deltaP `33.7305` edge `2.1036` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.2378` n `98` status `ready` deltaP `45.7203` edge `1.9758` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.4485` n `98` status `ready` deltaP `31.9545` edge `1.8517` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.3186` n `40` status `ready` deltaP `58.8302` edge `0.4147` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.0365` n `40` status `ready` deltaP `54.766` edge `0.3046` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8766` n `40` status `ready` deltaP `32.7744` edge `0.5146` maxDD `-4.137`
- `news_risk_high->crypto_alt_24h` score `7.1074` n `40` status `ready` deltaP `16.7504` edge `1.2501` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `6.7047` n `40` status `ready` deltaP `55.2744` edge `0.1947` maxDD `-0.0246`
- `news_risk_high->crypto_major_4h` score `6.4598` n `40` status `ready` deltaP `25.4268` edge `0.4115` maxDD `-1.7491`
- `news_risk_high->equity_1h` score `5.8538` n `40` status `ready` deltaP `27.3952` edge `0.327` maxDD `-0.4122`
- `news_risk_high->index_4h` score `4.398` n `40` status `ready` deltaP `38.2622` edge `0.1339` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.1201` n `40` status `ready` deltaP `19.2964` edge `0.1665` maxDD `-1.4777`
- `news_risk_high->metal_1h` score `2.7485` n `40` status `ready` deltaP `29.4461` edge `0.0545` maxDD `-0.0743`
- `news_risk_high->commodity_4h` score `2.7178` n `40` status `ready` deltaP `29.3293` edge `0.0563` maxDD `-0.3611`
- `news_risk_high->crypto_alt_1h` score `2.4467` n `40` status `ready` deltaP `18.1437` edge `0.1356` maxDD `-2.5469`
- `news_risk_high->index_1h` score `2.1527` n `40` status `ready` deltaP `25.1946` edge `0.0332` maxDD `-0.0751`
- `news_risk_high->commodity_1h` score `-0.1855` n `40` status `ready` deltaP `-0.2545` edge `0.0197` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
