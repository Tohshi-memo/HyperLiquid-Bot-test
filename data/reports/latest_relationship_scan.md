# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T23:37:33.182777+00:00`
- Price records: `672`
- Market context records: `4037`
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

- `risk_on_high->unknown_4h` score `145.7125` n `40` status `ready` deltaP `-7.1341` edge `12.3719` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.7125` n `40` status `ready` deltaP `-7.1341` edge `12.3719` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.762` n `134` status `ready` deltaP `-7.0656` edge `4.3468` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `23.6293` n `154` status `ready` deltaP `2.249` edge `2.4964` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.8344` n `40` status `ready` deltaP `35.8752` edge `0.1637` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.8344` n `40` status `ready` deltaP `35.8752` edge `0.1637` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2525` n `40` status `ready` deltaP `36.2195` edge `0.0343` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2525` n `40` status `ready` deltaP `36.2195` edge `0.0343` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.6935` n `134` status `ready` deltaP `22.8239` edge `0.0935` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.6695` n `154` status `ready` deltaP `15.9922` edge `0.1606` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.4794` n `134` status `ready` deltaP `11.0078` edge `0.1486` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1216` n `158` status `ready` deltaP `7.9702` edge `0.0963` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9137` n `40` status `ready` deltaP `18.689` edge `0.0181` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9137` n `40` status `ready` deltaP `18.689` edge `0.0181` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.5222` n `40` status `ready` deltaP `2.4697` edge `0.2552` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.5222` n `40` status `ready` deltaP `2.4697` edge `0.2552` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.4227` n `158` status `ready` deltaP `10.2081` edge `0.0487` maxDD `-3.0049`
- `risk_on_high->equity_1h` score `0.4064` n `40` status `ready` deltaP `10.9132` edge `0.0002` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4064` n `40` status `ready` deltaP `10.9132` edge `0.0002` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.2775` n `158` status `ready` deltaP `6.9147` edge `0.0492` maxDD `-3.7739`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
