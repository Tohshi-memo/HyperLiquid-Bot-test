# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T12:52:26.476445+00:00`
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

- `risk_on_high->crypto_alt_24h` score `20.0936` n `58` status `ready` deltaP `45.546` edge `1.472` maxDD `-6.4273`
- `risk_on_and_context->crypto_alt_24h` score `20.0936` n `58` status `ready` deltaP `45.546` edge `1.472` maxDD `-6.4273`
- `risk_on_high->unknown_4h` score `8.1348` n `107` status `ready` deltaP `25.4032` edge `0.5702` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1348` n `107` status `ready` deltaP `25.4032` edge `0.5702` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5888` n `159` status `ready` deltaP `22.0998` edge `0.4711` maxDD `-2.5493`
- `risk_on_high->crypto_major_24h` score `6.1505` n `58` status `ready` deltaP `29.6695` edge `0.8006` maxDD `-13.4567`
- `risk_on_and_context->crypto_major_24h` score `6.1505` n `58` status `ready` deltaP `29.6695` edge `0.8006` maxDD `-13.4567`
- `risk_on_high->fx_24h` score `6.0273` n `58` status `ready` deltaP `69.654` edge `0.0547` maxDD `-0.3427`
- `risk_on_and_context->fx_24h` score `6.0273` n `58` status `ready` deltaP `69.654` edge `0.0547` maxDD `-0.3427`
- `market_context_high->crypto_major_24h` score `4.792` n `100` status `ready` deltaP `22.0833` edge `0.5137` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.5994` n `100` status `ready` deltaP `33.9444` edge `0.2345` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.34` n `100` status `ready` deltaP `22.1667` edge `0.8276` maxDD `-27.517`
- `risk_on_high->unknown_1h` score `2.4023` n `107` status `ready` deltaP `6.3658` edge `0.2154` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4023` n `107` status `ready` deltaP `6.3658` edge `0.2154` maxDD `-1.9453`
- `risk_on_high->metal_24h` score `2.3513` n `58` status `ready` deltaP `36.2547` edge `0.1287` maxDD `-1.5161`
- `risk_on_and_context->metal_24h` score `2.3513` n `58` status `ready` deltaP `36.2547` edge `0.1287` maxDD `-1.5161`
- `market_context_high->unknown_1h` score `2.1796` n `159` status `ready` deltaP `5.7075` edge `0.2066` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.4988` n `61` status `ready` deltaP `3.4701` edge `0.1364` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.1394` n `100` status `ready` deltaP `38.8264` edge `0.0331` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `0.7214` n `44` status `ready` deltaP `8.2545` edge `0.069` maxDD `-1.1904`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
