# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T08:07:39.016625+00:00`
- Price records: `672`
- Market context records: `4073`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10216`

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

- `risk_on_high->unknown_4h` score `144.9097` n `40` status `ready` deltaP `-7.1341` edge `12.305` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9097` n `40` status `ready` deltaP `-7.1341` edge `12.305` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.1328` n `172` status `ready` deltaP `2.1794` edge `4.4043` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.1653` n `144` status `ready` deltaP `-8.7197` edge `3.5581` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.944` n `172` status `ready` deltaP `-1.262` edge `1.9627` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.7094` n `40` status `ready` deltaP `37.8963` edge `0.0612` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.7094` n `40` status `ready` deltaP `37.8963` edge `0.0612` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `1.507` n `40` status `ready` deltaP `29.9827` edge `-0.0743` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.507` n `40` status `ready` deltaP `29.9827` edge `-0.0743` maxDD `0.0`
- `market_context_high->index_24h` score `1.4526` n `144` status `ready` deltaP `17.6776` edge `0.0032` maxDD `0.0`
- `market_context_high->equity_4h` score `1.3341` n `172` status `ready` deltaP `14.8149` edge `0.1655` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `0.9727` n `40` status `ready` deltaP `18.8415` edge `0.022` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9727` n `40` status `ready` deltaP `18.8415` edge `0.022` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.7454` n `172` status `ready` deltaP `5.6225` edge `0.0806` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4496` n `40` status `ready` deltaP `10.9132` edge `0.0038` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4496` n `40` status `ready` deltaP `10.9132` edge `0.0038` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.2284` n `40` status `ready` deltaP `11.7073` edge `-0.0152` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2284` n `40` status `ready` deltaP `11.7073` edge `-0.0152` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.1635` n `40` status `ready` deltaP `11.6159` edge `0.0026` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1635` n `40` status `ready` deltaP `11.6159` edge `0.0026` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
