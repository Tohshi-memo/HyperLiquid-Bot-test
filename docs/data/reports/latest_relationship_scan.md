# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T20:52:34.348681+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10236`

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

- `risk_on_high->crypto_alt_24h` score `11.8162` n `117` status `ready` deltaP `25.2404` edge `0.8394` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `11.8162` n `117` status `ready` deltaP `25.2404` edge `0.8394` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `6.7688` n `241` status `ready` deltaP `17.8956` edge `0.5275` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `6.2636` n `117` status `ready` deltaP `20.9268` edge `1.0703` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.2636` n `117` status `ready` deltaP `20.9268` edge `1.0703` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.0531` n `117` status `ready` deltaP `33.9887` edge `0.315` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.0531` n `117` status `ready` deltaP `33.9887` edge `0.315` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.2113` n `117` status `ready` deltaP `24.1518` edge `0.2758` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2113` n `117` status `ready` deltaP `24.1518` edge `0.2758` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.5377` n `117` status `ready` deltaP `25.5609` edge `0.0453` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.5377` n `117` status `ready` deltaP `25.5609` edge `0.0453` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.8162` n `241` status `ready` deltaP `20.6561` edge `0.053` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.4614` n `241` status `ready` deltaP `9.0278` edge `0.0616` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0437` n `117` status `ready` deltaP `4.2467` edge `0.0939` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0437` n `117` status `ready` deltaP `4.2467` edge `0.0939` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.7762` n `117` status `ready` deltaP `9.0278` edge `0.0045` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.7762` n `117` status `ready` deltaP `9.0278` edge `0.0045` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7738` n `117` status `ready` deltaP `19.7383` edge `0.0832` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7738` n `117` status `ready` deltaP `19.7383` edge `0.0832` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4233` n `117` status `ready` deltaP `14.2229` edge `-0.0064` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
