# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T22:28:23.763141+00:00`
- Price records: `672`
- Market context records: `4032`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.8331` n `40` status `ready` deltaP `-6.6768` edge `12.3789` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.8331` n `40` status `ready` deltaP `-6.6768` edge `12.3789` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.1223` n `134` status `ready` deltaP `-6.3724` edge `4.3722` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.1802` n `149` status `ready` deltaP `1.595` edge `2.63` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.2973` n `40` status `ready` deltaP `36.7418` edge `0.1965` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.2973` n `40` status `ready` deltaP `36.7418` edge `0.1965` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.1893` n `40` status `ready` deltaP `35.6098` edge `0.0331` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.1893` n `40` status `ready` deltaP `35.6098` edge `0.0331` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.9524` n `134` status `ready` deltaP `23.6904` edge `0.1093` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.9626` n `149` status `ready` deltaP `17.9756` edge `0.1718` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.7551` n `134` status `ready` deltaP `11.8744` edge `0.1658` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1459` n `156` status `ready` deltaP `8.199` edge `0.0968` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9233` n `40` status `ready` deltaP `18.689` edge `0.0189` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9233` n `40` status `ready` deltaP `18.689` edge `0.0189` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.6899` n `40` status `ready` deltaP `3.3362` edge `0.2634` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.6899` n `40` status `ready` deltaP `3.3362` edge `0.2634` maxDD `-12.9187`
- `risk_on_high->index_24h` score `0.5101` n `40` status `ready` deltaP `24.4367` edge `-0.1204` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.5101` n `40` status `ready` deltaP `24.4367` edge `-0.1204` maxDD `0.0`
- `market_context_high->crypto_major_1h` score `0.5058` n `156` status `ready` deltaP `7.5196` edge `0.053` maxDD `-2.8785`
- `market_context_high->metal_1h` score `0.3992` n `156` status `ready` deltaP `9.6806` edge `0.0492` maxDD `-3.0049`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
