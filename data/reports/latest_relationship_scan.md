# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T03:37:28.606638+00:00`
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

- `news_risk_high->unknown_24h` score `52.1098` n `51` status `ready` deltaP `17.1875` edge `4.2279` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.4019` n `51` status `ready` deltaP `40.237` edge `1.025` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9737` n `51` status `ready` deltaP `23.4965` edge `0.9291` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8372` n `51` status `ready` deltaP `48.9481` edge `0.1753` maxDD `-0.2147`
- `risk_on_high->unknown_1h` score `4.6276` n `31` status `ready` deltaP `-15.1536` edge `0.7392` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.6276` n `31` status `ready` deltaP `-15.1536` edge `0.7392` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.1847` n `51` status `ready` deltaP `37.4731` edge `0.029` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.1769` n `51` status `ready` deltaP `24.7938` edge `0.1765` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `2.9143` n `51` status `ready` deltaP `15.5864` edge `0.1694` maxDD `-0.7693`
- `news_risk_high->crypto_alt_24h` score `2.1934` n `51` status `ready` deltaP `26.5625` edge `0.0057` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.1675` n `31` status `ready` deltaP `28.7127` edge `-0.002` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.1675` n `31` status `ready` deltaP `28.7127` edge `-0.002` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `2.128` n `145` status `ready` deltaP `21.3194` edge `0.0489` maxDD `-0.0956`
- `news_risk_high->metal_24h` score `2.0551` n `51` status `ready` deltaP `36.9281` edge `-0.0707` maxDD `-0.0053`
- `risk_on_high->equity_4h` score `1.7673` n `31` status `ready` deltaP `-3.2897` edge `0.2122` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.7673` n `31` status `ready` deltaP `-3.2897` edge `0.2122` maxDD `-0.773`
- `market_context_high->unknown_1h` score `1.6763` n `157` status `ready` deltaP `10.3036` edge `0.1159` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2817` n `51` status `ready` deltaP `17.4445` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8595` n `51` status `ready` deltaP `17.2948` edge `0.0313` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.765` n `51` status `ready` deltaP `12.1772` edge `0.0223` maxDD `-0.1788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
