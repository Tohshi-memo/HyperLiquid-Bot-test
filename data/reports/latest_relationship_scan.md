# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T05:07:31.265552+00:00`
- Price records: `672`
- Market context records: `4484`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11089`

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

- `risk_on_high->unknown_4h` score `124.1511` n `49` status `ready` deltaP `3.5683` edge `10.5052` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.1511` n `49` status `ready` deltaP `3.5683` edge `10.5052` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `34.0892` n `223` status `ready` deltaP `3.3465` edge `2.969` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `15.6831` n `223` status `ready` deltaP `3.2846` edge `1.8315` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.3781` n `49` status `ready` deltaP `39.7866` edge `0.0996` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.3781` n `49` status `ready` deltaP `39.7866` edge `0.0996` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.042` n `46` status `ready` deltaP `-13.7379` edge `0.543` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.042` n `46` status `ready` deltaP `-13.7379` edge `0.543` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.6877` n `49` status `ready` deltaP `21.3943` edge `0.1479` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.6877` n `49` status `ready` deltaP `21.3943` edge `0.1479` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.3106` n `46` status `ready` deltaP `13.5265` edge `0.1827` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.3106` n `46` status `ready` deltaP `13.5265` edge `0.1827` maxDD `-5.0928`
- `risk_on_high->index_24h` score `1.6758` n `46` status `ready` deltaP `22.3883` edge `0.0081` maxDD `-0.75`
- `risk_on_and_context->index_24h` score `1.6758` n `46` status `ready` deltaP `22.3883` edge `0.0081` maxDD `-0.75`
- `risk_on_high->metal_4h` score `1.6508` n `49` status `ready` deltaP `13.3244` edge `0.0823` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.6508` n `49` status `ready` deltaP `13.3244` edge `0.0823` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.22` n `49` status `ready` deltaP `15.4406` edge `0.033` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.22` n `49` status `ready` deltaP `15.4406` edge `0.033` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6315` n `49` status `ready` deltaP `15.7043` edge `0.007` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6315` n `49` status `ready` deltaP `15.7043` edge `0.007` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
