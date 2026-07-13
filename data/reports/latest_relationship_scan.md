# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T07:35:53.301352+00:00`
- Price records: `672`
- Market context records: `6582`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `5.367` n `150` status `ready` deltaP `8.532` edge `0.7204` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0052` n `210` status `ready` deltaP `-5.2794` edge `0.2924` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3557` n `150` status `ready` deltaP `13.7997` edge `0.2078` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3604` n `210` status `ready` deltaP `0.7086` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4025` n `210` status `ready` deltaP `7.197` edge `0.027` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5545` n `210` status `ready` deltaP `-0.3807` edge `0.0034` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.5703` n `210` status `ready` deltaP `5.2923` edge `0.0229` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5868` n `210` status `ready` deltaP `-0.4092` edge `-0.0042` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9215` n `210` status `ready` deltaP `8.9896` edge `0.0099` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1489` n `210` status `ready` deltaP `2.2313` edge `0.0004` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.3088` n `210` status `ready` deltaP `-1.279` edge `-0.0098` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3482` n `210` status `ready` deltaP `-4.3256` edge `-0.0028` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.6207` n `210` status `ready` deltaP `-16.3037` edge `0.2142` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.7464` n `210` status `ready` deltaP `0.0769` edge `-0.0032` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.7637` n `210` status `ready` deltaP `7.5813` edge `0.0548` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0282` n `210` status `ready` deltaP `4.6283` edge `0.0493` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1532` n `210` status `ready` deltaP `-1.5012` edge `0.02` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-2.7494` n `150` status `ready` deltaP `4.3973` edge `0.0784` maxDD `-7.2798`
- `market_context_high->fx_24h` score `-3.7146` n `150` status `ready` deltaP `-3.0052` edge `-0.0027` maxDD `-9.2795`
- `market_context_high->index_24h` score `-4.4752` n `150` status `ready` deltaP `-0.3627` edge `-0.0097` maxDD `-11.8655`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
