# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T04:22:25.898786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9622`

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

- `market_context_high->unknown_24h` score `181.6858` n `54` status `ready` deltaP `-16.0879` edge `15.2841` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `33.9053` n `119` status `ready` deltaP `-7.066` edge `2.9431` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.2527` n `54` status `ready` deltaP `25.1158` edge `0.5777` maxDD `-1.9265`
- `market_context_high->index_24h` score `5.7605` n `54` status `ready` deltaP `49.0741` edge `0.1572` maxDD `-0.012`
- `market_context_high->crypto_major_24h` score `5.7089` n `54` status `ready` deltaP `5.4398` edge `1.0019` maxDD `-17.1674`
- `risk_on_high->crypto_major_4h` score `5.3257` n `43` status `ready` deltaP `32.5759` edge `0.3119` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.3257` n `43` status `ready` deltaP `32.5759` edge `0.3119` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.2252` n `43` status `ready` deltaP `19.5406` edge `0.2666` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.2252` n `43` status `ready` deltaP `19.5406` edge `0.2666` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `3.1461` n `43` status `ready` deltaP `29.2612` edge `0.0903` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.1461` n `43` status `ready` deltaP `29.2612` edge `0.0903` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.2365` n `55` status `ready` deltaP `8.2254` edge `0.1079` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.2365` n `55` status `ready` deltaP `8.2254` edge `0.1079` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `0.885` n `55` status `ready` deltaP `8.1818` edge `0.0845` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.885` n `55` status `ready` deltaP `8.1818` edge `0.0845` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `0.8179` n `55` status `ready` deltaP `11.5406` edge `0.0193` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.8179` n `55` status `ready` deltaP `11.5406` edge `0.0193` maxDD `-0.2466`
- `market_context_high->metal_4h` score `0.5993` n `119` status `ready` deltaP `13.4121` edge `0.0328` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.5415` n `119` status `ready` deltaP `8.9683` edge `0.2202` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.0684` n `131` status `ready` deltaP `4.4225` edge `0.0827` maxDD `-4.9401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
