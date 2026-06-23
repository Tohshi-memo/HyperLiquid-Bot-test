# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T08:37:30.647859+00:00`
- Price records: `672`
- Market context records: `4499`
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

- `risk_on_high->unknown_4h` score `124.8135` n `49` status `ready` deltaP `4.4829` edge `10.5543` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.8135` n `49` status `ready` deltaP `4.4829` edge `10.5543` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `38.1348` n `209` status `ready` deltaP `3.7562` edge `3.3034` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `16.8972` n `209` status `ready` deltaP `1.8562` edge `1.9422` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.9137` n `49` status `ready` deltaP `41.0061` edge `0.1361` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.9137` n `49` status `ready` deltaP `41.0061` edge `0.1361` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.4872` n `49` status `ready` deltaP `23.5285` edge `0.2003` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.4872` n `49` status `ready` deltaP `23.5285` edge `0.2003` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.422` n `49` status `ready` deltaP `-13.57` edge `0.4989` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.422` n `49` status `ready` deltaP `-13.57` edge `0.4989` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.3046` n `49` status `ready` deltaP `11.802` edge `0.1937` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.3046` n `49` status `ready` deltaP `11.802` edge `0.1937` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `1.94` n `49` status `ready` deltaP `15.1537` edge `0.0942` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.94` n `49` status `ready` deltaP `15.1537` edge `0.0942` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3508` n `49` status `ready` deltaP `15.8897` edge `0.0409` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3508` n `49` status `ready` deltaP `15.8897` edge `0.0409` maxDD `-0.7415`
- `risk_on_high->index_24h` score `0.7201` n `49` status `ready` deltaP `18.9626` edge `-0.0147` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.7201` n `49` status `ready` deltaP `18.9626` edge `-0.0147` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
