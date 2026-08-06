# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T07:22:25.716648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.8199` n `92` status `ready` deltaP `4.4686` edge `0.9595` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0994` n `109` status `ready` deltaP `-1.0405` edge `0.4481` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2444` n `109` status `ready` deltaP `14.209` edge `0.0936` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8703` n `92` status `ready` deltaP `2.7626` edge `0.21` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5736` n `92` status `ready` deltaP `21.407` edge `0.0514` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4659` n `109` status `ready` deltaP `8.2088` edge `0.0257` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0255` n `109` status `ready` deltaP `5.3837` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1691` n `109` status `ready` deltaP `8.552` edge `0.0073` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5557` n `109` status `ready` deltaP `-2.0093` edge `-0.0084` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7712` n `109` status `ready` deltaP `-3.8057` edge `-0.0201` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8036` n `109` status `ready` deltaP `2.6321` edge `0.0029` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2993` n `92` status `ready` deltaP `0.6341` edge `-0.0265` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.3313` n `92` status `ready` deltaP `-3.4496` edge `0.0718` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5445` n `109` status `ready` deltaP `-5.4373` edge `-0.0214` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8689` n `109` status `ready` deltaP `0.82` edge `-0.0915` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1225` n `109` status `ready` deltaP `-12.8203` edge `-0.0612` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1283` n `109` status `ready` deltaP `1.3845` edge `-0.0476` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.1724` n `109` status `ready` deltaP `1.5835` edge `-0.1469` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3522` n `109` status `ready` deltaP `-11.7481` edge `-0.0637` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.379` n `92` status `ready` deltaP `7.4124` edge `-0.0351` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
