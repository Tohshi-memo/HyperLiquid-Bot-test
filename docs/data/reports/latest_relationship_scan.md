# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T06:22:33.785380+00:00`
- Price records: `672`
- Market context records: `6577`
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

- `market_context_high->unknown_24h` score `6.0605` n `145` status `ready` deltaP `10.601` edge `0.7644` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.782` n `210` status `ready` deltaP `-5.1297` edge `0.2728` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4227` n `145` status `ready` deltaP `13.512` edge `0.2153` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3534` n `210` status `ready` deltaP `0.8583` edge `-0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3955` n `210` status `ready` deltaP `7.197` edge `0.0279` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5134` n `210` status `ready` deltaP `6.0408` edge `0.0252` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5639` n `210` status `ready` deltaP `-0.5304` edge `0.0032` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6258` n `210` status `ready` deltaP `-1.008` edge `-0.0052` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9629` n `210` status `ready` deltaP `8.3891` edge `0.0086` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2112` n `210` status `ready` deltaP `1.7822` edge `-0.0018` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2883` n `210` status `ready` deltaP `-3.7268` edge `-0.0018` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3407` n `210` status `ready` deltaP `-1.7122` edge `-0.011` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5501` n `210` status `ready` deltaP `-15.8561` edge `0.2171` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7207` n `210` status `ready` deltaP `7.8825` edge `0.0583` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7799` n `210` status `ready` deltaP `-0.537` edge `-0.0034` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9286` n `210` status `ready` deltaP `5.2381` edge `0.058` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-2.033` n `145` status `ready` deltaP `5.7996` edge `0.0891` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.1429` n `210` status `ready` deltaP `-1.3779` edge `0.0205` maxDD `-5.2172`
- `market_context_high->index_24h` score `-3.8018` n `145` status `ready` deltaP `1.1316` edge `0.0019` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8034` n `145` status `ready` deltaP `-4.3833` edge `-0.0049` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
