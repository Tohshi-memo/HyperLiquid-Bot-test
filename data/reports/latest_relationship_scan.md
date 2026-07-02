# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T09:07:29.693793+00:00`
- Price records: `672`
- Market context records: `5439`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->equity_24h` score `4.4331` n `185` status `ready` deltaP `11.8694` edge `0.6439` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `3.9107` n `185` status `ready` deltaP `18.6327` edge `0.6557` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7598` n `196` status `ready` deltaP `16.7652` edge `0.4308` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.9607` n `196` status `ready` deltaP `13.4239` edge `0.3211` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.9204` n `196` status `ready` deltaP `11.828` edge `0.3286` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5718` n `197` status `ready` deltaP `8.577` edge `0.087` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2012` n `185` status `ready` deltaP `10.6503` edge `0.0353` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1518` n `197` status `ready` deltaP `6.7031` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1907` n `197` status `ready` deltaP `1.8093` edge `0.0682` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2649` n `197` status `ready` deltaP `2.8314` edge `0.0836` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3086` n `197` status `ready` deltaP `3.5404` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5486` n `197` status `ready` deltaP `0.4293` edge `0.0003` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7663` n `196` status `ready` deltaP `7.8397` edge `0.0448` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0842` n `185` status `ready` deltaP `16.1627` edge `0.1005` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1746` n `196` status `ready` deltaP `0.2894` edge `0.0027` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.5092` n `197` status `ready` deltaP `-3.5662` edge `-0.0072` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6836` n `196` status `ready` deltaP `-8.5802` edge `-0.0344` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3741` n `196` status `ready` deltaP `-7.737` edge `-0.0491` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.8042` n `185` status `ready` deltaP `9.345` edge `0.2404` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4479` n `185` status `ready` deltaP `-5.7742` edge `-0.1786` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
