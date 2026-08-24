# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T00:52:25.910410+00:00`
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

- `news_risk_high->unknown_24h` score `54.2014` n `41` status `ready` deltaP `17.1875` edge `4.4022` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.5695` n `41` status `ready` deltaP `53.9676` edge `1.2192` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0841` n `51` status `ready` deltaP `23.4965` edge `0.9383` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8797` n `41` status `ready` deltaP `57.9692` edge `0.1953` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `5.0652` n `41` status `ready` deltaP `28.125` edge `0.2346` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.8818` n `37` status `ready` deltaP `-9.7103` edge `0.6073` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8818` n `37` status `ready` deltaP `-9.7103` edge `0.6073` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0471` n `51` status `ready` deltaP `35.9487` edge `0.0277` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.9875` n `51` status `ready` deltaP `15.8858` edge `0.1735` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.9699` n `37` status `ready` deltaP `3.4031` edge `0.2678` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.9699` n `37` status `ready` deltaP `3.4031` edge `0.2678` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.708` n `51` status `ready` deltaP `23.1169` edge `0.1486` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4211` n `41` status `ready` deltaP `40.1042` edge `-0.0656` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.3515` n `37` status `ready` deltaP `30.6526` edge `0.0004` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3515` n `37` status `ready` deltaP `30.6526` edge `0.0004` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.689` n `143` status `ready` deltaP `21.2615` edge `0.0127` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.5026` n `155` status `ready` deltaP `9.6619` edge `0.1057` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.229` n `51` status `ready` deltaP `16.8457` edge `0.0071` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.0737` n `37` status `ready` deltaP `13.839` edge `0.0452` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.0737` n `37` status `ready` deltaP `13.839` edge `0.0452` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
