# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T03:37:25.970337+00:00`
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

- `market_context_high->unknown_24h` score `561.5278` n `54` status `ready` deltaP `-16.0879` edge `46.9376` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `34.6085` n `119` status `ready` deltaP `-7.066` edge `3.0017` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.4568` n `54` status `ready` deltaP `25.1158` edge `0.581` maxDD `-1.1632`
- `market_context_high->index_24h` score `5.9092` n `54` status `ready` deltaP `50.7523` edge `0.1584` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.4059` n `40` status `ready` deltaP `31.4634` edge `0.326` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.4059` n `40` status `ready` deltaP `31.4634` edge `0.326` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.0233` n `40` status `ready` deltaP `25.122` edge `0.2959` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0233` n `40` status `ready` deltaP `25.122` edge `0.2959` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `4.7282` n `54` status `ready` deltaP `0.4051` edge `0.9183` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.326` n `40` status `ready` deltaP `30.6707` edge `0.0959` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.326` n `40` status `ready` deltaP `30.6707` edge `0.0959` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.5807` n `52` status `ready` deltaP `11.3427` edge `0.1158` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.5807` n `52` status `ready` deltaP `11.3427` edge `0.1158` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.1981` n `52` status `ready` deltaP `11.0894` edge `0.0912` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.1981` n `52` status `ready` deltaP `11.0894` edge `0.0912` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.1784` n `52` status `ready` deltaP `15.0622` edge `0.0217` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.1784` n `52` status `ready` deltaP `15.0622` edge `0.0217` maxDD `-0.2466`
- `market_context_high->metal_4h` score `0.446` n `119` status `ready` deltaP `12.0362` edge `0.0292` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.3353` n `131` status `ready` deltaP `6.2634` edge `0.0896` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.3125` n `119` status `ready` deltaP `6.9046` edge `0.2046` maxDD `-11.1784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
