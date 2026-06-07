# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T23:07:24.846205+00:00`
- Price records: `672`
- Market context records: `3225`
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

- `market_context_high->commodity_24h` score `13.879` n `102` status `ready` deltaP `49.5609` edge `0.869` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.7322` n `102` status `ready` deltaP `19.0563` edge `2.6234` maxDD `-70.5257`
- `market_context_high->index_24h` score `9.7768` n `102` status `ready` deltaP `32.547` edge `0.8532` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.4077` n `102` status `ready` deltaP `19.1278` edge `1.5356` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.2194` n `128` status `ready` deltaP `21.6273` edge `0.1699` maxDD `-1.9973`
- `market_context_high->crypto_major_24h` score `0.9636` n `102` status `ready` deltaP `20.6495` edge `2.1083` maxDD `-155.1276`
- `market_context_high->commodity_1h` score `0.3164` n `140` status `ready` deltaP `6.5441` edge `0.025` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5313` n `140` status `ready` deltaP `3.9393` edge `0.0119` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5994` n `140` status `ready` deltaP `4.9529` edge `0.1156` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.6648` n `140` status `ready` deltaP `5.124` edge `0.1069` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-0.7495` n `128` status `ready` deltaP `8.2317` edge `0.0756` maxDD `-15.1257`
- `market_context_high->equity_1h` score `-0.901` n `140` status `ready` deltaP `4.3199` edge `0.0126` maxDD `-8.8863`
- `market_context_high->fx_24h` score `-1.0734` n `102` status `ready` deltaP `-1.7464` edge `-0.0165` maxDD `-1.7577`
- `market_context_high->fx_1h` score `-1.7967` n `140` status `ready` deltaP `-11.2104` edge `-0.0056` maxDD `-0.8846`
- `market_context_high->index_4h` score `-2.0737` n `128` status `ready` deltaP `10.2896` edge `0.0495` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-2.0772` n `128` status `ready` deltaP `-10.9946` edge `-0.0106` maxDD `-1.4696`
- `market_context_high->metal_1h` score `-2.3912` n `140` status `ready` deltaP `-4.5509` edge `-0.0194` maxDD `-8.2956`
- `market_context_high->unknown_1h` score `-2.8437` n `140` status `ready` deltaP `2.0873` edge `-0.1306` maxDD `-17.8311`
- `market_context_high->crypto_alt_4h` score `-4.4514` n `128` status `ready` deltaP `7.6792` edge `0.1826` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.7169` n `128` status `ready` deltaP `4.154` edge `0.1584` maxDD `-54.2659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
