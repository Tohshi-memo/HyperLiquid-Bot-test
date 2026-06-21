# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T13:37:29.289625+00:00`
- Price records: `672`
- Market context records: `4317`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `130.7665` n `44` status `ready` deltaP `-0.8315` edge `11.0846` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7665` n `44` status `ready` deltaP `-0.8315` edge `11.0846` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `28.8202` n `233` status `ready` deltaP `3.3198` edge `2.5375` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.5485` n `233` status `ready` deltaP `1.7534` edge `1.327` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `3.6677` n `211` status `ready` deltaP `-7.2744` edge `0.7575` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.3031` n `44` status `ready` deltaP `31.4163` edge `-0.0128` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.3031` n `44` status `ready` deltaP `31.4163` edge `-0.0128` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.1858` n `42` status `ready` deltaP `-20.2877` edge `0.4769` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.1858` n `42` status `ready` deltaP `-20.2877` edge `0.4769` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.9881` n `42` status `ready` deltaP `22.9167` edge `0.0129` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9881` n `42` status `ready` deltaP `22.9167` edge `0.0129` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.4935` n `44` status `ready` deltaP `17.0871` edge `0.0771` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4935` n `44` status `ready` deltaP `17.0871` edge `0.0771` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3931` n `44` status `ready` deltaP `7.8933` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3931` n `44` status `ready` deltaP `7.8933` edge `0.0031` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1791` n `44` status `ready` deltaP `8.3969` edge `0.0212` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1791` n `44` status `ready` deltaP `8.3969` edge `0.0212` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0203` n `44` status `ready` deltaP `8.786` edge `0.0031` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0203` n `44` status `ready` deltaP `8.786` edge `0.0031` maxDD `-0.3925`
- `risk_on_high->index_24h` score `-0.0003` n `42` status `ready` deltaP `19.2708` edge `-0.1285` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
