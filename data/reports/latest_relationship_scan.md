# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T12:22:28.733575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11637`

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

- `risk_on_high->crypto_alt_24h` score `21.8518` n `56` status `ready` deltaP `48.8096` edge `1.5557` maxDD `-3.8092`
- `risk_on_and_context->crypto_alt_24h` score `21.8518` n `56` status `ready` deltaP `48.8096` edge `1.5557` maxDD `-3.8092`
- `risk_on_high->crypto_major_24h` score `11.1091` n `56` status `ready` deltaP `32.0932` edge `0.8721` maxDD `-10.1568`
- `risk_on_and_context->crypto_major_24h` score `11.1091` n `56` status `ready` deltaP `32.0932` edge `0.8721` maxDD `-10.1568`
- `risk_on_high->unknown_4h` score `8.118` n `107` status `ready` deltaP `25.4032` edge `0.5688` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.118` n `107` status `ready` deltaP `25.4032` edge `0.5688` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.572` n `159` status `ready` deltaP `22.0998` edge `0.4697` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.4686` n `56` status `ready` deltaP `72.8671` edge `0.0589` maxDD `-0.1171`
- `risk_on_and_context->fx_24h` score `6.4686` n `56` status `ready` deltaP `72.8671` edge `0.0589` maxDD `-0.1171`
- `market_context_high->crypto_major_24h` score `5.3661` n `98` status `ready` deltaP `23.1647` edge `0.546` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.9295` n `98` status `ready` deltaP `35.5158` edge `0.2432` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.6743` n `98` status `ready` deltaP `23.5545` edge `0.8612` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.1643` n `56` status `ready` deltaP `39.0873` edge `0.1402` maxDD `-0.9672`
- `risk_on_and_context->metal_24h` score `4.1643` n `56` status `ready` deltaP `39.0873` edge `0.1402` maxDD `-0.9672`
- `risk_on_high->unknown_1h` score `2.4035` n `107` status `ready` deltaP `6.3658` edge `0.2155` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4035` n `107` status `ready` deltaP `6.3658` edge `0.2155` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.1808` n `159` status `ready` deltaP `5.7075` edge `0.2067` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5` n `61` status `ready` deltaP `3.4701` edge `0.1365` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.2124` n `98` status `ready` deltaP `39.9589` edge `0.0349` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `1.2018` n `56` status `ready` deltaP `21.627` edge `0.0461` maxDD `-4.2103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
