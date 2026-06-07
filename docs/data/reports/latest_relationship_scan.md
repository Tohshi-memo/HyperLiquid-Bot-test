# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T23:52:25.839241+00:00`
- Price records: `672`
- Market context records: `3229`
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

- `market_context_high->crypto_alt_24h` score `14.2486` n `102` status `ready` deltaP `19.0563` edge `2.6896` maxDD `-70.5257`
- `market_context_high->commodity_24h` score `13.8814` n `102` status `ready` deltaP `49.5609` edge `0.8692` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.79` n `102` status `ready` deltaP `32.547` edge `0.8543` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.6961` n `102` status `ready` deltaP `19.9346` edge `1.5672` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8379` n `128` status `ready` deltaP `19.7409` edge `0.1561` maxDD `-2.0974`
- `market_context_high->crypto_major_24h` score `2.4084` n `102` status `ready` deltaP `23.0699` edge `2.2417` maxDD `-153.2716`
- `market_context_high->commodity_1h` score `-0.016` n `140` status `ready` deltaP `4.8503` edge `0.021` maxDD `-2.0401`
- `market_context_high->index_1h` score `-0.5911` n `140` status `ready` deltaP `3.3747` edge `0.008` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.6185` n `128` status `ready` deltaP `8.8605` edge `0.0882` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.8488` n `140` status `ready` deltaP `3.4303` edge `0.0946` maxDD `-15.1032`
- `market_context_high->crypto_alt_1h` score `-0.8801` n `140` status `ready` deltaP `3.2592` edge `0.0909` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.9855` n `140` status `ready` deltaP `3.1908` edge `0.0093` maxDD `-8.8863`
- `market_context_high->fx_24h` score `-1.3329` n `102` status `ready` deltaP `-4.1666` edge `-0.019` maxDD `-1.929`
- `market_context_high->index_4h` score `-1.45` n `128` status `ready` deltaP `9.6609` edge `0.0406` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.9414` n `140` status `ready` deltaP `-12.9042` edge `-0.0062` maxDD `-0.8978`
- `market_context_high->fx_4h` score `-2.2816` n `128` status `ready` deltaP `-12.8811` edge `-0.0133` maxDD `-1.61`
- `market_context_high->metal_1h` score `-2.3115` n `140` status `ready` deltaP `-3.9863` edge `-0.0166` maxDD `-8.2892`
- `market_context_high->unknown_1h` score `-2.9164` n `140` status `ready` deltaP `0.9581` edge `-0.1324` maxDD `-17.8311`
- `market_context_high->equity_4h` score `-3.4283` n `128` status `ready` deltaP `10.8804` edge `0.0185` maxDD `-36.7784`
- `market_context_high->metal_4h` score `-4.0726` n `128` status `ready` deltaP `-11.3186` edge `-0.0304` maxDD `-24.6352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
