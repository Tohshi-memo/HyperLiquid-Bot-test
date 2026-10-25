# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T15:52:25.820487+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5252`

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

- `market_context_high->unknown_4h` score `33.5283` n `113` status `ready` deltaP `-0.2914` edge `2.8295` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.0905` n `62` status `ready` deltaP `7.9413` edge `0.0455` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.042` n `113` status `ready` deltaP `4.0088` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0427` n `113` status `ready` deltaP `7.1539` edge `0.0086` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.5326` n `113` status `ready` deltaP `-0.4822` edge `0.0089` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6263` n `113` status `ready` deltaP `4.7838` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6768` n `113` status `ready` deltaP `-2.3356` edge `-0.006` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8221` n `113` status `ready` deltaP `-2.0856` edge `0.0314` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3636` n `113` status `ready` deltaP `2.6482` edge `-0.0344` maxDD `-9.3126`
- `market_context_high->crypto_major_24h` score `-1.3722` n `62` status `ready` deltaP `-5.606` edge `-0.036` maxDD `-4.5369`
- `market_context_high->fx_24h` score `-1.5595` n `62` status `ready` deltaP `2.621` edge `0.0098` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8916` n `113` status `ready` deltaP `4.7661` edge `-0.0184` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1092` n `62` status `ready` deltaP `-1.9321` edge `-0.1293` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.187` n `113` status `ready` deltaP `-8.3774` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1642` n `113` status `ready` deltaP `-1.86` edge `-0.0639` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7453` n `62` status `ready` deltaP `-10.1367` edge `0.0225` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.8919` n `113` status `ready` deltaP `-0.6889` edge `-0.0924` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.5204` n `62` status `ready` deltaP `-3.797` edge `-0.2932` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.956` n `113` status `ready` deltaP `-12.7428` edge `-0.2449` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.891` n `62` status `ready` deltaP `-17.9883` edge `-0.8762` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
