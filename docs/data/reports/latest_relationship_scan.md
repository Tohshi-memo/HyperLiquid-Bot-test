# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T01:22:24.941971+00:00`
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

- `news_risk_high->unknown_24h` score `53.6638` n `43` status `ready` deltaP `17.1875` edge `4.3574` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.4515` n `43` status `ready` deltaP `54.308` edge `1.2071` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0949` n `51` status `ready` deltaP `23.4965` edge `0.9392` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8835` n `43` status `ready` deltaP `58.196` edge `0.1941` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `4.3164` n `43` status `ready` deltaP `28.125` edge `0.1722` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.8717` n `37` status `ready` deltaP `-9.86` edge `0.607` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8717` n `37` status `ready` deltaP `-9.86` edge `0.607` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0739` n `51` status `ready` deltaP `36.2536` edge `0.0279` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `3.0267` n `37` status `ready` deltaP `3.708` edge `0.2705` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `3.0267` n `37` status `ready` deltaP `3.708` edge `0.2705` maxDD `-0.773`
- `news_risk_high->unknown_1h` score `2.9719` n `51` status `ready` deltaP `15.7361` edge `0.1732` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `2.7647` n `51` status `ready` deltaP `23.4218` edge `0.1513` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4019` n `43` status `ready` deltaP `40.1042` edge `-0.0672` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.3527` n `37` status `ready` deltaP `30.6526` edge `0.0005` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3527` n `37` status `ready` deltaP `30.6526` edge `0.0005` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.7032` n `145` status `ready` deltaP `21.3194` edge `0.0135` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.491` n `157` status `ready` deltaP `9.8163` edge `0.1037` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.241` n `51` status `ready` deltaP `16.9954` edge `0.0071` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.1005` n `37` status `ready` deltaP `14.1439` edge `0.0454` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.1005` n `37` status `ready` deltaP `14.1439` edge `0.0454` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
