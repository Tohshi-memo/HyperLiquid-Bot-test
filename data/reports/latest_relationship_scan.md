# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T22:52:24.794975+00:00`
- Price records: `672`
- Market context records: `3224`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->commodity_24h` score `13.8598` n `102` status `ready` deltaP `49.5609` edge `0.8674` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.4867` n `102` status `ready` deltaP `18.2495` edge `2.5973` maxDD `-70.5257`
- `market_context_high->index_24h` score `9.687` n `102` status `ready` deltaP `31.7402` edge `0.8511` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.2713` n `102` status `ready` deltaP `18.321` edge `1.5235` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3153` n `128` status `ready` deltaP `22.2561` edge `0.1737` maxDD `-1.9973`
- `market_context_high->crypto_major_24h` score `0.4139` n `102` status `ready` deltaP `19.8427` edge `2.0616` maxDD `-156.2652`
- `market_context_high->commodity_1h` score `0.3236` n `140` status `ready` deltaP `6.5441` edge `0.0256` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.6927` n `140` status `ready` deltaP `4.3884` edge `0.1074` maxDD `-14.7034`
- `market_context_high->unknown_4h` score `-0.7643` n `128` status `ready` deltaP `8.2317` edge `0.0737` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7768` n `140` status `ready` deltaP `4.5594` edge `0.0963` maxDD `-15.1032`
- `market_context_high->index_1h` score `-0.8818` n `140` status `ready` deltaP `3.3747` edge `0.0103` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.9577` n `140` status `ready` deltaP `3.7553` edge `0.0091` maxDD `-8.8863`
- `market_context_high->fx_24h` score `-0.9867` n `102` status `ready` deltaP `-0.9396` edge `-0.0157` maxDD `-1.6962`
- `market_context_high->fx_1h` score `-1.8419` n `140` status `ready` deltaP `-11.775` edge `-0.0056` maxDD `-0.8846`
- `market_context_high->index_4h` score `-2.003` n `128` status `ready` deltaP `10.9184` edge `0.0512` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-2.0122` n `128` status `ready` deltaP `-10.3659` edge `-0.0098` maxDD `-1.4356`
- `market_context_high->metal_1h` score `-2.3828` n `140` status `ready` deltaP `-4.5509` edge `-0.0187` maxDD `-8.2956`
- `market_context_high->unknown_1h` score `-2.8918` n `140` status `ready` deltaP `1.5227` edge `-0.133` maxDD `-17.8311`
- `market_context_high->crypto_alt_4h` score `-4.4989` n `128` status `ready` deltaP `7.6792` edge `0.1765` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.8066` n `128` status `ready` deltaP `4.154` edge `0.1469` maxDD `-54.2659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
