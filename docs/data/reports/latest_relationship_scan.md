# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T19:07:44.312557+00:00`
- Price records: `672`
- Market context records: `6312`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11133`

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

- `news_risk_high->crypto_alt_24h` score `15.303` n `32` status `ready` deltaP `43.2292` edge `1.0018` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0085` n `32` status `ready` deltaP `50.5208` edge `0.1639` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2608` n `32` status `ready` deltaP `16.6667` edge `0.5131` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2009` n `32` status `ready` deltaP `43.8262` edge `0.0625` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.281` n `32` status `ready` deltaP `29.5139` edge `0.0972` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4616` n `32` status `ready` deltaP `14.4274` edge `0.1379` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9416` n `32` status `ready` deltaP `11.9199` edge `0.0874` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6476` n `208` status `ready` deltaP `-4.278` edge `0.1833` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.0132` n `196` status `ready` deltaP `9.0032` edge `0.0374` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1018` n `161` status `ready` deltaP `21.4943` edge `0.1005` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.4607` n `32` status `ready` deltaP `4.5139` edge `-0.002` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4639` n `208` status `ready` deltaP `2.5939` edge `0.001` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5749` n `208` status `ready` deltaP `-0.7485` edge `-0.0004` maxDD `-2.1314`
- `news_risk_high->metal_1h` score `-0.72` n `32` status `ready` deltaP `-2.6946` edge `-0.0246` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7266` n `208` status `ready` deltaP `-0.9155` edge `-0.0022` maxDD `-0.8463`
- `market_context_high->index_1h` score `-0.805` n `208` status `ready` deltaP `-2.7896` edge `0.0023` maxDD `-0.9531`
- `market_context_high->index_4h` score `-0.9149` n `196` status `ready` deltaP `1.7609` edge `0.0174` maxDD `-1.381`
- `market_context_high->equity_1h` score `-0.9966` n `208` status `ready` deltaP `-2.2685` edge `-0.0011` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-1.0145` n `208` status `ready` deltaP `4.468` edge `0.0154` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
