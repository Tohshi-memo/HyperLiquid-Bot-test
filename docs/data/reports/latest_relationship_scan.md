# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T10:07:30.290430+00:00`
- Price records: `672`
- Market context records: `4506`
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

- `risk_on_high->unknown_4h` score `124.7141` n `49` status `ready` deltaP `4.6354` edge `10.545` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.7141` n `49` status `ready` deltaP `4.6354` edge `10.545` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `40.2554` n `203` status `ready` deltaP `3.4299` edge `3.4823` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `20.414` n `203` status `ready` deltaP `3.3687` edge `2.0781` maxDD `-25.951`
- `risk_on_high->equity_4h` score `5.0791` n `49` status `ready` deltaP `41.7683` edge `0.1448` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0791` n `49` status `ready` deltaP `41.7683` edge `0.1448` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.906` n `49` status `ready` deltaP `24.4431` edge `0.2291` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.906` n `49` status `ready` deltaP `24.4431` edge `0.2291` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.6087` n `49` status `ready` deltaP `-12.5283` edge `0.5159` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.6087` n `49` status `ready` deltaP `-12.5283` edge `0.5159` maxDD `-4.834`
- `risk_on_high->metal_4h` score `2.0259` n `49` status `ready` deltaP `15.7634` edge `0.0973` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.0259` n `49` status `ready` deltaP `15.7634` edge `0.0973` maxDD `-1.3516`
- `risk_on_high->unknown_24h` score `2.0245` n `49` status `ready` deltaP `10.7603` edge `0.1773` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.0245` n `49` status `ready` deltaP `10.7603` edge `0.1773` maxDD `-5.0928`
- `risk_on_high->equity_1h` score `1.3495` n `49` status `ready` deltaP `16.0394` edge `0.0398` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3495` n `49` status `ready` deltaP `16.0394` edge `0.0398` maxDD `-0.7415`
- `risk_on_high->index_24h` score `0.939` n `49` status `ready` deltaP `20.0042` edge `-0.0034` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.939` n `49` status `ready` deltaP `20.0042` edge `-0.0034` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6387` n `49` status `ready` deltaP `15.7043` edge `0.0076` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6387` n `49` status `ready` deltaP `15.7043` edge `0.0076` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
