# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T04:07:29.544700+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `308.521` n `54` status `ready` deltaP `-16.0879` edge `25.8537` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `34.1237` n `119` status `ready` deltaP `-7.066` edge `2.9613` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.3828` n `54` status `ready` deltaP `25.1158` edge `0.58` maxDD `-1.5767`
- `market_context_high->index_24h` score `5.9008` n `54` status `ready` deltaP `50.7523` edge `0.1577` maxDD `-0.012`
- `market_context_high->crypto_major_24h` score `5.3675` n `54` status `ready` deltaP `3.7615` edge `0.9734` maxDD `-17.4937`
- `risk_on_high->crypto_major_4h` score `5.3412` n `42` status `ready` deltaP `32.2299` edge `0.3155` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.3412` n `42` status `ready` deltaP `32.2299` edge `0.3155` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.4557` n `42` status `ready` deltaP `21.3125` edge `0.274` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.4557` n `42` status `ready` deltaP `21.3125` edge `0.274` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `3.3443` n `42` status `ready` deltaP `31.1992` edge `0.0939` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.3443` n `42` status `ready` deltaP `31.1992` edge `0.0939` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.3413` n `54` status `ready` deltaP `9.2205` edge `0.11` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.3413` n `54` status `ready` deltaP `9.2205` edge `0.11` maxDD `-2.4421`
- `risk_on_high->metal_1h` score `0.9729` n `54` status `ready` deltaP `12.719` edge `0.0202` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.9729` n `54` status `ready` deltaP `12.719` edge `0.0202` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `0.9713` n `54` status `ready` deltaP `9.1096` edge `0.0855` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.9713` n `54` status `ready` deltaP `9.1096` edge `0.0855` maxDD `-3.2233`
- `market_context_high->metal_4h` score `0.5885` n `119` status `ready` deltaP `13.4121` edge `0.0319` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.4699` n `119` status `ready` deltaP `8.2803` edge `0.2156` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.1819` n `131` status `ready` deltaP `5.0361` edge `0.085` maxDD `-4.9401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
