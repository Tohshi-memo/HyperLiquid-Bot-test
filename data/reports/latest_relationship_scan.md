# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T10:22:23.967659+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0197` n `54` status `ready` deltaP `38.5017` edge `0.3283` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0197` n `54` status `ready` deltaP `38.5017` edge `0.3283` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2315` n `141` status `ready` deltaP `14.7909` edge `0.545` maxDD `-5.6115`
- `risk_on_high->crypto_major_4h` score `5.8897` n `67` status `ready` deltaP `33.3409` edge `0.3538` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.8897` n `67` status `ready` deltaP `33.3409` edge `0.3538` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `5.8234` n `141` status `ready` deltaP `22.9567` edge `0.4644` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `2.4454` n `67` status `ready` deltaP `9.2442` edge `0.2656` maxDD `-5.5423`
- `risk_on_and_context->crypto_alt_4h` score `2.4454` n `67` status `ready` deltaP `9.2442` edge `0.2656` maxDD `-5.5423`
- `market_context_high->crypto_major_1h` score `0.8595` n `153` status `ready` deltaP `6.6583` edge `0.1078` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.5708` n `153` status `ready` deltaP `7.9654` edge `0.1259` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.4033` n `141` status `ready` deltaP `13.3259` edge `0.0493` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.3219` n `79` status `ready` deltaP `8.8703` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.3219` n `79` status `ready` deltaP `8.8703` edge `0.0061` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.0958` n `153` status `ready` deltaP `8.6469` edge `0.0049` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.3356` n `153` status `ready` deltaP `7.5418` edge `0.0087` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.4038` n `153` status `ready` deltaP `9.3447` edge `0.0369` maxDD `-7.0778`
- `risk_on_high->crypto_major_1h` score `-0.4252` n `79` status `ready` deltaP `3.6137` edge `0.0127` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4252` n `79` status `ready` deltaP `3.6137` edge `0.0127` maxDD `-3.7781`
- `risk_on_high->equity_1h` score `-0.4293` n `79` status `ready` deltaP `10.2217` edge `0.0257` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4293` n `79` status `ready` deltaP `10.2217` edge `0.0257` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
