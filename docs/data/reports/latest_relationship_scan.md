# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T03:52:29.414939+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9843`

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

- `market_context_high->crypto_alt_4h` score `6.45` n `117` status `ready` deltaP `16.0022` edge `0.5757` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.4408` n `54` status `ready` deltaP `32.0` edge `0.3234` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.4408` n `54` status `ready` deltaP `32.0` edge `0.3234` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.996` n `117` status `ready` deltaP `20.8151` edge `0.5168` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.0388` n `54` status `ready` deltaP `18.2814` edge `0.3428` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0388` n `54` status `ready` deltaP `18.2814` edge `0.3428` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.4825` n `117` status `ready` deltaP `-3.6194` edge `0.4623` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.4372` n `54` status `ready` deltaP `33.9205` edge `0.428` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4372` n `54` status `ready` deltaP `33.9205` edge `0.428` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6643` n `117` status `ready` deltaP `13.4168` edge `0.156` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2297` n `117` status `ready` deltaP `6.56` edge `0.1393` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.245` n `117` status `ready` deltaP `13.6127` edge `0.0342` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3179` n `117` status `ready` deltaP `1.3976` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3571` n `54` status `ready` deltaP `2.0016` edge `0.0131` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3571` n `54` status `ready` deltaP `2.0016` edge `0.0131` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.4141` n `117` status `ready` deltaP `6.9656` edge `0.006` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4835` n `54` status `ready` deltaP `1.5525` edge `0.0008` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4835` n `54` status `ready` deltaP `1.5525` edge `0.0008` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.6125` n `117` status `ready` deltaP `-0.1271` edge `-0.0029` maxDD `-1.3154`
- `risk_on_high->metal_4h` score `-0.6217` n `54` status `ready` deltaP `1.2195` edge `0.0167` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
