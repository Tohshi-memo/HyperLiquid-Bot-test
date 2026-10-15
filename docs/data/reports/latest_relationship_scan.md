# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T15:07:29.682620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9112`

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

- `risk_on_high->commodity_24h` score `7.9035` n `54` status `ready` deltaP `41.4634` edge `0.3822` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9035` n `54` status `ready` deltaP `41.4634` edge `0.3822` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5943` n `122` status `ready` deltaP `17.8054` edge `0.6056` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.8477` n `122` status `ready` deltaP `19.4048` edge `0.4901` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.4006` n `54` status `ready` deltaP `20.568` edge `0.3576` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.4006` n `54` status `ready` deltaP `20.568` edge `0.3576` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0112` n `54` status `ready` deltaP `32.8535` edge `0.3805` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0112` n `54` status `ready` deltaP `32.8535` edge `0.3805` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6013` n `122` status `ready` deltaP `13.4068` edge `0.1505` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9537` n `122` status `ready` deltaP `5.3598` edge `0.1243` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.0269` n `122` status `ready` deltaP `9.7036` edge `0.0376` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2867` n `115` status `ready` deltaP `13.6373` edge `0.1505` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3454` n `122` status `ready` deltaP `-0.613` edge `-0.0018` maxDD `-0.4047`
- `risk_on_high->crypto_major_1h` score `-0.4732` n `54` status `ready` deltaP `0.6543` edge `0.0072` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4732` n `54` status `ready` deltaP `0.6543` edge `0.0072` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.5061` n `122` status `ready` deltaP `1.5139` edge `-0.0002` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5248` n `54` status `ready` deltaP `0.804` edge `0.0005` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5248` n `54` status `ready` deltaP `0.804` edge `0.0005` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5344` n `54` status `ready` deltaP `4.2083` edge `0.0057` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.5344` n `54` status `ready` deltaP `4.2083` edge `0.0057` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
