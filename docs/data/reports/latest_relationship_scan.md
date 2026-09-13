# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T23:07:25.755843+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `3960.2808` n `56` status `ready` deltaP `10.2093` edge `329.9755` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `435.9028` n `82` status `ready` deltaP `-5.4002` edge `36.4034` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.9013` n `82` status `ready` deltaP `36.7199` edge `1.3791` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.316` n `82` status `ready` deltaP `38.0236` edge `1.4199` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.2082` n `82` status `ready` deltaP `30.3743` edge `0.8262` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.5013` n `82` status `ready` deltaP `54.1463` edge `0.2818` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.207` n `56` status `ready` deltaP `39.8276` edge `0.1684` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.979` n `30` status `ready` deltaP `39.8276` edge `0.1494` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.979` n `30` status `ready` deltaP `39.8276` edge `0.1494` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.9673` n `82` status `ready` deltaP `28.5534` edge `0.269` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `3.4204` n `30` status `ready` deltaP `60.2299` edge `0.0475` maxDD `-0.1745`
- `risk_on_and_context->fx_24h` score `3.4204` n `30` status `ready` deltaP `60.2299` edge `0.0475` maxDD `-0.1745`
- `risk_on_high->crypto_alt_24h` score `1.9638` n `30` status `ready` deltaP `0.4598` edge `0.3788` maxDD `-6.7415`
- `risk_on_and_context->crypto_alt_24h` score `1.9638` n `30` status `ready` deltaP `0.4598` edge `0.3788` maxDD `-6.7415`
- `risk_on_high->commodity_4h` score `1.816` n `52` status `ready` deltaP `24.9765` edge `0.0198` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.816` n `52` status `ready` deltaP `24.9765` edge `0.0198` maxDD `-0.1313`
- `market_context_high->fx_24h` score `1.6397` n `56` status `ready` deltaP `40.1109` edge `0.0237` maxDD `-1.804`
- `market_context_high->commodity_4h` score `1.4544` n `129` status `ready` deltaP `20.1763` edge `0.0285` maxDD `-0.345`
- `market_context_high->crypto_alt_24h` score `1.0848` n `56` status `ready` deltaP `0.2217` edge `0.3114` maxDD `-14.1318`
- `news_risk_high->index_4h` score `0.4568` n `82` status `ready` deltaP `13.1097` edge `0.034` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
