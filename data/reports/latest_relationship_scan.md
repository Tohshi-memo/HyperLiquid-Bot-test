# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T12:37:25.880345+00:00`
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

- `risk_on_high->crypto_alt_24h` score `21.0357` n `57` status `ready` deltaP `47.1492` edge `1.5166` maxDD `-4.9026`
- `risk_on_and_context->crypto_alt_24h` score `21.0357` n `57` status `ready` deltaP `47.1492` edge `1.5166` maxDD `-4.9026`
- `risk_on_high->crypto_major_24h` score `10.3438` n `57` status `ready` deltaP `30.8571` edge `0.8389` maxDD `-11.6104`
- `risk_on_and_context->crypto_major_24h` score `10.3438` n `57` status `ready` deltaP `30.8571` edge `0.8389` maxDD `-11.6104`
- `risk_on_high->unknown_4h` score `8.1264` n `107` status `ready` deltaP `25.4032` edge `0.5695` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1264` n `107` status `ready` deltaP `25.4032` edge `0.5695` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5804` n `159` status `ready` deltaP `22.0998` edge `0.4704` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.2511` n `57` status `ready` deltaP `71.3176` edge `0.0567` maxDD `-0.2311`
- `risk_on_and_context->fx_24h` score `6.2511` n `57` status `ready` deltaP `71.3176` edge `0.0567` maxDD `-0.2311`
- `market_context_high->crypto_major_24h` score `5.097` n `99` status `ready` deltaP `22.6168` edge `0.5314` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.768` n `99` status `ready` deltaP `34.7222` edge `0.2392` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.5201` n `99` status `ready` deltaP `22.8536` edge `0.8461` maxDD `-27.517`
- `risk_on_high->metal_24h` score `3.9054` n `57` status `ready` deltaP `37.6462` edge `0.1351` maxDD `-1.183`
- `risk_on_and_context->metal_24h` score `3.9054` n `57` status `ready` deltaP `37.6462` edge `0.1351` maxDD `-1.183`
- `risk_on_high->unknown_1h` score `2.4035` n `107` status `ready` deltaP `6.3658` edge `0.2155` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4035` n `107` status `ready` deltaP `6.3658` edge `0.2155` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.1808` n `159` status `ready` deltaP `5.7075` edge `0.2067` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5` n `61` status `ready` deltaP `3.4701` edge `0.1365` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.1801` n `99` status `ready` deltaP `39.4729` edge `0.034` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `0.7483` n `44` status `ready` deltaP `8.4281` edge `0.0713` maxDD `-1.1904`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
