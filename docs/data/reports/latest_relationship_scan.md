# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T09:07:28.744884+00:00`
- Price records: `672`
- Market context records: `4501`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `124.8233` n `49` status `ready` deltaP `4.6354` edge `10.5541` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.8233` n `49` status `ready` deltaP `4.6354` edge `10.5541` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `38.847` n `207` status `ready` deltaP `3.5545` edge `3.3641` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `17.7227` n `207` status `ready` deltaP `2.1312` edge `1.9811` maxDD `-34.1398`
- `risk_on_high->equity_4h` score `4.9933` n `49` status `ready` deltaP `41.311` edge `0.1407` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.9933` n `49` status `ready` deltaP `41.311` edge `0.1407` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.646` n `49` status `ready` deltaP `23.8334` edge `0.2115` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.646` n `49` status `ready` deltaP `23.8334` edge `0.2115` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.4868` n `49` status `ready` deltaP `-13.2228` edge `0.5049` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.4868` n `49` status `ready` deltaP `-13.2228` edge `0.5049` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.2145` n `49` status `ready` deltaP `11.4548` edge `0.1885` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.2145` n `49` status `ready` deltaP `11.4548` edge `0.1885` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `1.9847` n `49` status `ready` deltaP `15.4585` edge `0.0959` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.9847` n `49` status `ready` deltaP `15.4585` edge `0.0959` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3711` n `49` status `ready` deltaP `16.0394` edge `0.0416` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3711` n `49` status `ready` deltaP `16.0394` edge `0.0416` maxDD `-0.7415`
- `risk_on_high->index_24h` score `0.7923` n `49` status `ready` deltaP `19.3098` edge `-0.011` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.7923` n `49` status `ready` deltaP `19.3098` edge `-0.011` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
