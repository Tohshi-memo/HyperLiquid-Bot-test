# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T00:37:24.004518+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `54.5062` n `40` status `ready` deltaP `17.1875` edge `4.4276` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.6509` n `40` status `ready` deltaP `53.7847` edge `1.2272` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0577` n `51` status `ready` deltaP `23.4965` edge `0.9361` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8772` n `40` status `ready` deltaP `57.8472` edge `0.1959` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `5.52` n `40` status `ready` deltaP `28.125` edge `0.2725` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.8756` n `37` status `ready` deltaP `-9.7103` edge `0.6065` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8756` n `37` status `ready` deltaP `-9.7103` edge `0.6065` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0471` n `51` status `ready` deltaP `35.9487` edge `0.0277` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.9779` n `51` status `ready` deltaP `15.8858` edge `0.1727` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.9385` n `37` status `ready` deltaP `3.2507` edge `0.2662` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.9385` n `37` status `ready` deltaP `3.2507` edge `0.2662` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.6766` n `51` status `ready` deltaP `22.9645` edge `0.147` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4247` n `40` status `ready` deltaP `40.1042` edge `-0.0653` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.3381` n `37` status `ready` deltaP `30.5002` edge `0.0003` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3381` n `37` status `ready` deltaP `30.5002` edge `0.0003` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.6734` n `142` status `ready` deltaP `21.2319` edge `0.0116` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.507` n `154` status `ready` deltaP `9.5069` edge `0.1071` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2278` n `51` status `ready` deltaP `16.8457` edge `0.007` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.0591` n `37` status `ready` deltaP `13.6866` edge `0.045` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.0591` n `37` status `ready` deltaP `13.6866` edge `0.045` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
