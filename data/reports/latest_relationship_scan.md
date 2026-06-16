# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T09:37:39.984795+00:00`
- Price records: `672`
- Market context records: `4079`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10232`

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

- `risk_on_high->unknown_4h` score `144.7767` n `40` status `ready` deltaP `-7.8963` edge `12.299` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7767` n `40` status `ready` deltaP `-7.8963` edge `12.299` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.0753` n `172` status `ready` deltaP `1.7303` edge `4.4025` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.086` n `144` status `ready` deltaP `-9.0663` edge `3.5538` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.811` n `172` status `ready` deltaP `-2.0242` edge `1.9567` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.6626` n `40` status `ready` deltaP `37.8963` edge `0.0573` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6626` n `40` status `ready` deltaP `37.8963` edge `0.0573` maxDD `-0.0446`
- `market_context_high->equity_4h` score `1.2873` n `172` status `ready` deltaP `14.8149` edge `0.1616` maxDD `-6.9137`
- `market_context_high->index_24h` score `1.0502` n `144` status `ready` deltaP `16.6378` edge `-0.0234` maxDD `0.0`
- `risk_on_high->equity_24h` score `0.7302` n `40` status `ready` deltaP `28.9428` edge `-0.1321` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.7302` n `40` status `ready` deltaP `28.9428` edge `-0.1321` maxDD `0.0`
- `market_context_high->equity_1h` score `0.7274` n `172` status `ready` deltaP `5.6225` edge `0.0791` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.7089` n `40` status `ready` deltaP `18.0793` edge `0.0051` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.7089` n `40` status `ready` deltaP `18.0793` edge `0.0051` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.4316` n `40` status `ready` deltaP `10.9132` edge `0.0023` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4316` n `40` status `ready` deltaP `10.9132` edge `0.0023` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.2058` n `40` status `ready` deltaP `11.7073` edge `-0.0181` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2058` n `40` status `ready` deltaP `11.7073` edge `-0.0181` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.1903` n `40` status `ready` deltaP `11.9207` edge `0.004` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1903` n `40` status `ready` deltaP `11.9207` edge `0.004` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
