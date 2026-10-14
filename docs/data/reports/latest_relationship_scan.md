# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T09:37:29.335689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8970`

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

- `market_context_high->crypto_alt_4h` score `6.3788` n `117` status `ready` deltaP `16.612` edge `0.5657` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.196` n `54` status `ready` deltaP `32.0` edge `0.303` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.196` n `54` status `ready` deltaP `32.0` edge `0.303` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.8712` n `117` status `ready` deltaP `20.8151` edge `0.5064` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `4.9676` n `54` status `ready` deltaP `18.8912` edge `0.3328` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9676` n `54` status `ready` deltaP `18.8912` edge `0.3328` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.3561` n `54` status `ready` deltaP `33.9205` edge `0.4176` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3561` n `54` status `ready` deltaP `33.9205` edge `0.4176` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7578` n `117` status `ready` deltaP `14.0156` edge `0.1598` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.3016` n `117` status `ready` deltaP `6.8594` edge `0.1433` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0718` n `117` status `ready` deltaP `12.3932` edge `0.0279` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3103` n `54` status `ready` deltaP `2.301` edge `0.0171` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3103` n `54` status `ready` deltaP `2.301` edge `0.0171` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.384` n `117` status `ready` deltaP `0.6468` edge `0.0017` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4189` n `117` status `ready` deltaP `6.9656` edge `0.0056` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4867` n `54` status `ready` deltaP `1.5525` edge `0.0004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4867` n `54` status `ready` deltaP `1.5525` edge `0.0004` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5906` n `54` status `ready` deltaP `3.7592` edge `0.0018` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5906` n `54` status `ready` deltaP `3.7592` edge `0.0018` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.6671` n `117` status `ready` deltaP `-1.1782` edge `-0.0029` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
