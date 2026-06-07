# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T21:52:20.388066+00:00`
- Price records: `672`
- Market context records: `3219`
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

- `market_context_high->commodity_24h` score `13.6539` n `102` status `ready` deltaP `47.9473` edge `0.861` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.2884` n `102` status `ready` deltaP `15.0225` edge `2.4729` maxDD `-71.142`
- `market_context_high->index_24h` score `9.4739` n `102` status `ready` deltaP `30.1266` edge `0.8441` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.6878` n `102` status `ready` deltaP `15.094` edge `1.4702` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.368` n `128` status `ready` deltaP `22.8849` edge `0.1739` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.2796` n `140` status `ready` deltaP `5.9795` edge `0.0257` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.6362` n `102` status `ready` deltaP `2.2876` edge `-0.0123` maxDD `-1.4283`
- `market_context_high->unknown_4h` score `-0.7276` n `128` status `ready` deltaP `7.6029` edge `0.0826` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.833` n `140` status `ready` deltaP `3.9393` edge `0.0106` maxDD `-4.5023`
- `market_context_high->fx_4h` score `-1.1522` n `128` status `ready` deltaP `-7.8506` edge `-0.0069` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.5941` n `140` status `ready` deltaP `3.1908` edge `0.0028` maxDD `-8.8863`
- `market_context_high->crypto_alt_1h` score `-1.6516` n `140` status `ready` deltaP `3.2592` edge `0.0661` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.737` n `140` status `ready` deltaP `-10.6459` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->crypto_major_1h` score `-1.8214` n `140` status `ready` deltaP `2.8657` edge `0.0554` maxDD `-15.1032`
- `market_context_high->index_4h` score `-2.0186` n `128` status `ready` deltaP `10.9184` edge `0.0499` maxDD `-17.6057`
- `market_context_high->crypto_major_24h` score `-2.0287` n `102` status `ready` deltaP `16.6156` edge `1.8577` maxDD `-161.9511`
- `market_context_high->metal_1h` score `-2.2284` n `140` status `ready` deltaP `-3.9863` edge `-0.011` maxDD `-8.1833`
- `market_context_high->unknown_1h` score `-2.8855` n `140` status `ready` deltaP `1.5227` edge `-0.1322` maxDD `-17.8311`
- `market_context_high->crypto_major_4h` score `-5.1293` n `128` status `ready` deltaP `2.2676` edge `0.1181` maxDD `-54.2659`
- `market_context_high->equity_4h` score `-5.3355` n `128` status `ready` deltaP `10.8804` edge `0.0134` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
