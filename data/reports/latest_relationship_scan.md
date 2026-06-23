# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T04:22:29.302199+00:00`
- Price records: `672`
- Market context records: `4481`
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

- `risk_on_high->unknown_4h` score `124.0848` n `49` status `ready` deltaP `3.2634` edge `10.5017` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.0848` n `49` status `ready` deltaP `3.2634` edge `10.5017` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `33.4296` n `226` status `ready` deltaP `3.8167` edge `2.9109` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `15.2482` n `226` status `ready` deltaP `3.444` edge `1.7942` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.2443` n `49` status `ready` deltaP `39.3293` edge `0.0915` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.2443` n `49` status `ready` deltaP `39.3293` edge `0.0915` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.1863` n `45` status `ready` deltaP `-13.4375` edge `0.5595` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.1863` n `45` status `ready` deltaP `-13.4375` edge `0.5595` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.6031` n `49` status `ready` deltaP `20.937` edge `0.1439` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.6031` n `49` status `ready` deltaP `20.937` edge `0.1439` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.5456` n `45` status `ready` deltaP `13.8542` edge `0.2001` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.5456` n `45` status `ready` deltaP `13.8542` edge `0.2001` maxDD `-5.0928`
- `risk_on_high->index_24h` score `2.0138` n `45` status `ready` deltaP `23.9931` edge `0.017` maxDD `-0.3977`
- `risk_on_and_context->index_24h` score `2.0138` n `45` status `ready` deltaP `23.9931` edge `0.017` maxDD `-0.3977`
- `risk_on_high->equity_24h` score `1.6529` n `45` status `ready` deltaP `21.9097` edge `0.0269` maxDD `-2.4846`
- `risk_on_and_context->equity_24h` score `1.6529` n `45` status `ready` deltaP `21.9097` edge `0.0269` maxDD `-2.4846`
- `risk_on_high->metal_4h` score `1.5844` n `49` status `ready` deltaP `13.0195` edge `0.0788` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.5844` n `49` status `ready` deltaP `13.0195` edge `0.0788` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.1721` n `49` status `ready` deltaP `15.1412` edge `0.031` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1721` n `49` status `ready` deltaP `15.1412` edge `0.031` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
