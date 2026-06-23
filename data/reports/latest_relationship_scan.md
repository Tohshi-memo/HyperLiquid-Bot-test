# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T08:52:30.285330+00:00`
- Price records: `672`
- Market context records: `4500`
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

- `risk_on_high->unknown_4h` score `124.8461` n `49` status `ready` deltaP `4.6354` edge `10.556` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.8461` n `49` status `ready` deltaP `4.6354` edge `10.556` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `38.4903` n `208` status `ready` deltaP `3.731` edge `3.3332` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `17.0823` n `208` status `ready` deltaP `1.8293` edge `1.9578` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.9559` n `49` status `ready` deltaP `41.1585` edge `0.1386` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.9559` n `49` status `ready` deltaP `41.1585` edge `0.1386` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.5678` n `49` status `ready` deltaP `23.6809` edge `0.206` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.5678` n `49` status `ready` deltaP `23.6809` edge `0.206` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.4528` n `49` status `ready` deltaP `-13.3964` edge `0.5017` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.4528` n `49` status `ready` deltaP `-13.3964` edge `0.5017` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.2584` n `49` status `ready` deltaP `11.6284` edge `0.191` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.2584` n `49` status `ready` deltaP `11.6284` edge `0.191` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `1.9629` n `49` status `ready` deltaP `15.3061` edge `0.0951` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.9629` n `49` status `ready` deltaP `15.3061` edge `0.0951` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3699` n `49` status `ready` deltaP `16.0394` edge `0.0415` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3699` n `49` status `ready` deltaP `16.0394` edge `0.0415` maxDD `-0.7415`
- `risk_on_high->index_24h` score `0.7568` n `49` status `ready` deltaP `19.1362` edge `-0.0128` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.7568` n `49` status `ready` deltaP `19.1362` edge `-0.0128` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
