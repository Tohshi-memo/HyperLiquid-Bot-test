# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T04:07:30.138681+00:00`
- Price records: `672`
- Market context records: `4480`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11059`

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

- `risk_on_high->unknown_4h` score `124.086` n `49` status `ready` deltaP `3.2634` edge `10.5018` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.086` n `49` status `ready` deltaP `3.2634` edge `10.5018` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `33.1438` n `227` status `ready` deltaP `3.6799` edge `2.888` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `15.1104` n `227` status `ready` deltaP `3.5961` edge `1.7817` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.2009` n `49` status `ready` deltaP `39.1768` edge `0.0889` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.2009` n `49` status `ready` deltaP `39.1768` edge `0.0889` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.3881` n `44` status `ready` deltaP `-12.7525` edge `0.5808` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.3881` n `44` status `ready` deltaP `-12.7525` edge `0.5808` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `3.0255` n `44` status `ready` deltaP `23.9583` edge `0.0924` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.0255` n `44` status `ready` deltaP `23.9583` edge `0.0924` maxDD `0.0`
- `risk_on_high->unknown_24h` score `2.6237` n `44` status `ready` deltaP `13.8258` edge `0.2068` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.6237` n `44` status `ready` deltaP `13.8258` edge `0.2068` maxDD `-5.0928`
- `risk_on_high->crypto_major_4h` score `2.5959` n `49` status `ready` deltaP `20.937` edge `0.1433` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.5959` n `49` status `ready` deltaP `20.937` edge `0.1433` maxDD `-2.6576`
- `risk_on_high->index_24h` score `2.4397` n `44` status `ready` deltaP `26.0417` edge `0.0297` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.4397` n `44` status `ready` deltaP `26.0417` edge `0.0297` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.576` n `49` status `ready` deltaP `13.0195` edge `0.0781` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.576` n `49` status `ready` deltaP `13.0195` edge `0.0781` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.1565` n `49` status `ready` deltaP `14.9915` edge `0.0307` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1565` n `49` status `ready` deltaP `14.9915` edge `0.0307` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
