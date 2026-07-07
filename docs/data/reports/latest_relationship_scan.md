# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T06:22:27.070502+00:00`
- Price records: `672`
- Market context records: `5954`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.918` n `30` status `ready` deltaP `63.1944` edge `0.1552` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4524` n `30` status `ready` deltaP `39.2709` edge `0.2131` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8454` n `30` status `ready` deltaP `39.8476` edge `0.0594` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0945` n `30` status `ready` deltaP `25.2794` edge `0.0199` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5388` n `223` status `ready` deltaP `10.0008` edge `0.171` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8964` n `30` status `ready` deltaP `10.7884` edge `0.0897` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2652` n `30` status `ready` deltaP `5.9182` edge `0.0407` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1905` n `30` status `ready` deltaP `6.9791` edge `0.0162` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3246` n `30` status `ready` deltaP `2.8842` edge `-0.0242` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3544` n `235` status `ready` deltaP `4.8312` edge `0.0352` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4885` n `235` status `ready` deltaP `2.3169` edge `0.0018` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.619` n `213` status `ready` deltaP `20.0949` edge `0.2943` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.6379` n `235` status `ready` deltaP `-3.5935` edge `-0.0021` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6434` n `235` status `ready` deltaP `0.6383` edge `0.0046` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6874` n `235` status `ready` deltaP `-0.8199` edge `-0.0007` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0836` n `30` status `ready` deltaP `-10.0` edge `-0.0208` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.117` n `235` status `ready` deltaP `2.0175` edge `0.0186` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.1196` n `235` status `ready` deltaP `1.9232` edge `0.0204` maxDD `-9.807`
- `market_context_high->metal_4h` score `-1.5424` n `223` status `ready` deltaP `-1.6673` edge `-0.0234` maxDD `-5.725`
- `market_context_high->commodity_4h` score `-1.6732` n `223` status `ready` deltaP `-4.0011` edge `-0.0165` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
