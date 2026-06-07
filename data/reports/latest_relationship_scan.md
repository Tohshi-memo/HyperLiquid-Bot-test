# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T21:37:26.879741+00:00`
- Price records: `672`
- Market context records: `3218`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11250`

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

- `market_context_high->commodity_24h` score `13.6611` n `102` status `ready` deltaP `47.9473` edge `0.8616` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.2143` n `102` status `ready` deltaP `15.0225` edge `2.4634` maxDD `-71.142`
- `market_context_high->index_24h` score `9.377` n `102` status `ready` deltaP `29.3198` edge `0.8414` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.6192` n `102` status `ready` deltaP `15.094` edge `1.4614` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.38` n `128` status `ready` deltaP `22.8849` edge `0.1749` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.2784` n `140` status `ready` deltaP `5.9795` edge `0.0256` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.5487` n `102` status `ready` deltaP `3.0944` edge `-0.0114` maxDD `-1.3658`
- `market_context_high->unknown_4h` score `-0.7175` n `128` status `ready` deltaP `7.6029` edge `0.0839` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.8914` n `140` status `ready` deltaP `3.3747` edge `0.0095` maxDD `-4.5023`
- `market_context_high->fx_4h` score `-1.1148` n `128` status `ready` deltaP `-7.2218` edge `-0.0063` maxDD `-1.4115`
- `market_context_high->crypto_alt_1h` score `-1.5404` n `140` status `ready` deltaP `3.8238` edge `0.0716` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.6025` n `140` status `ready` deltaP `3.1908` edge `0.0021` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.7235` n `140` status `ready` deltaP `3.4303` edge `0.0598` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.737` n `140` status `ready` deltaP `-10.6459` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->index_4h` score `-2.015` n `128` status `ready` deltaP `10.9184` edge `0.0502` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.2272` n `140` status `ready` deltaP `-3.9863` edge `-0.0109` maxDD `-8.1833`
- `market_context_high->crypto_major_24h` score `-2.4686` n `102` status `ready` deltaP `15.8089` edge `1.8265` maxDD `-163.2039`
- `market_context_high->unknown_1h` score `-2.8114` n `140` status `ready` deltaP `1.5227` edge `-0.1227` maxDD `-17.8311`
- `market_context_high->crypto_major_4h` score `-5.1196` n `128` status `ready` deltaP `2.2676` edge `0.1209` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-5.3031` n `128` status `ready` deltaP `10.8804` edge `0.0161` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
