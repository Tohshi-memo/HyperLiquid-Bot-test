# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T11:52:32.539200+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11636`

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

- `risk_on_high->crypto_alt_24h` score `22.4617` n `55` status `ready` deltaP `50.183` edge `1.5853` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `22.4617` n `55` status `ready` deltaP `50.183` edge `1.5853` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `11.7082` n `55` status `ready` deltaP `33.2071` edge `0.8961` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `11.7082` n `55` status `ready` deltaP `33.2071` edge `0.8961` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.0868` n `107` status `ready` deltaP `25.4032` edge `0.5662` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0868` n `107` status `ready` deltaP `25.4032` edge `0.5662` maxDD `-2.266`
- `risk_on_high->fx_24h` score `6.6879` n `55` status `ready` deltaP `74.4792` edge `0.0608` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.6879` n `55` status `ready` deltaP `74.4792` edge `0.0608` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.5408` n `159` status `ready` deltaP `22.0998` edge `0.4671` maxDD `-2.5493`
- `market_context_high->crypto_major_24h` score `5.7689` n `96` status `ready` deltaP `24.3056` edge `0.5678` maxDD `-17.2607`
- `market_context_high->metal_24h` score `5.2396` n `96` status `ready` deltaP `37.1527` edge `0.2498` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.8897` n `96` status `ready` deltaP `24.6527` edge `0.8815` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.42` n `55` status `ready` deltaP `40.5808` edge `0.145` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.42` n `55` status `ready` deltaP `40.5808` edge `0.145` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `2.4011` n `107` status `ready` deltaP `6.3658` edge `0.2153` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4011` n `107` status `ready` deltaP `6.3658` edge `0.2153` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.1784` n `159` status `ready` deltaP `5.7075` edge `0.2065` maxDD `-2.041`
- `risk_on_high->equity_24h` score `1.4713` n `55` status `ready` deltaP `22.7083` edge `0.052` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `1.4713` n `55` status `ready` deltaP `22.7083` edge `0.052` maxDD `-3.7955`
- `news_risk_high->unknown_1h` score `1.4605` n `59` status `ready` deltaP `2.1364` edge `0.1421` maxDD `-1.1043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
