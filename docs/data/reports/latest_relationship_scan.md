# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T14:46:13.670316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `34.7276` n `48` status `ready` deltaP `22.5695` edge `2.7478` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `7.1933` n `48` status `ready` deltaP `35.4167` edge `0.4035` maxDD `-2.2133`
- `market_context_high->crypto_alt_24h` score `6.6417` n `48` status `ready` deltaP `35.5902` edge `0.3338` maxDD `-0.4075`
- `market_context_high->unknown_4h` score `5.1909` n `89` status `ready` deltaP `-0.1319` edge `0.533` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0475` n `89` status `ready` deltaP `14.4628` edge `0.0755` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2508` n `89` status `ready` deltaP `5.655` edge `0.0248` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2134` n `89` status `ready` deltaP `15.7441` edge `0.0084` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5018` n `89` status `ready` deltaP `1.016` edge `-0.0177` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5543` n `89` status `ready` deltaP `-1.682` edge `-0.0104` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6068` n `89` status `ready` deltaP `4.2718` edge `0.0172` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8407` n `89` status `ready` deltaP `4.4858` edge `0.0013` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.1003` n `89` status `ready` deltaP `-1.9848` edge `-0.0074` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7037` n `89` status `ready` deltaP `4.5381` edge `-0.0951` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8607` n `89` status `ready` deltaP `-10.1261` edge `-0.0456` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-1.8835` n `48` status `ready` deltaP `-6.5972` edge `0.0076` maxDD `-4.3126`
- `market_context_high->metal_24h` score `-3.0295` n `48` status `ready` deltaP `-23.7847` edge `-0.113` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.3835` n `89` status `ready` deltaP `2.9604` edge `-0.257` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5217` n `89` status `ready` deltaP `-12.5463` edge `-0.0725` maxDD `-7.6533`
- `market_context_high->index_24h` score `-5.2571` n `48` status `ready` deltaP `-28.125` edge `-0.267` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
