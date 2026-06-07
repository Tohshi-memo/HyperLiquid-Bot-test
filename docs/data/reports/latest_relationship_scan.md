# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T20:22:22.594319+00:00`
- Price records: `672`
- Market context records: `3213`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11150`

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

- `market_context_high->commodity_24h` score `13.7802` n `100` status `ready` deltaP `47.7708` edge `0.8727` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.642` n `100` status `ready` deltaP `13.8264` edge `2.398` maxDD `-71.142`
- `market_context_high->index_24h` score `9.311` n `100` status `ready` deltaP `28.9444` edge `0.8384` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.1646` n `100` status `ready` deltaP `13.3264` edge `1.4149` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.444` n `126` status `ready` deltaP `22.5005` edge `0.1828` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.5603` n `138` status `ready` deltaP `7.2225` edge `0.0408` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.2098` n `100` status `ready` deltaP `6.7361` edge `-0.0074` maxDD `-1.066`
- `market_context_high->unknown_4h` score `-0.4079` n `126` status `ready` deltaP `9.5601` edge `0.1245` maxDD `-14.7778`
- `market_context_high->index_1h` score `-1.0141` n `138` status `ready` deltaP `2.2455` edge `0.0068` maxDD `-4.5023`
- `market_context_high->fx_4h` score `-1.0514` n `126` status `ready` deltaP `-6.2283` edge `-0.0048` maxDD `-1.4115`
- `market_context_high->crypto_major_1h` score `-1.1572` n `138` status `ready` deltaP `3.8141` edge `0.0525` maxDD `-15.1032`
- `market_context_high->crypto_alt_1h` score `-1.5843` n `138` status `ready` deltaP `3.6948` edge `0.0688` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.5952` n `138` status `ready` deltaP `-8.9473` edge `-0.0046` maxDD `-0.8278`
- `market_context_high->index_4h` score `-1.7359` n `126` status `ready` deltaP `13.4921` edge `0.0563` maxDD `-17.6057`
- `market_context_high->equity_1h` score `-1.8752` n `138` status `ready` deltaP `0.7724` edge `-0.0045` maxDD `-8.8863`
- `market_context_high->metal_1h` score `-2.3144` n `138` status `ready` deltaP `-4.7731` edge `-0.0134` maxDD `-8.145`
- `market_context_high->unknown_1h` score `-2.9004` n `138` status `ready` deltaP `0.4556` edge `-0.127` maxDD `-17.8311`
- `market_context_high->crypto_major_24h` score `-4.3409` n `100` status `ready` deltaP `12.2847` edge `1.6609` maxDD `-166.279`
- `market_context_high->crypto_major_4h` score `-4.8304` n `126` status `ready` deltaP `4.4691` edge `0.1433` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-4.9534` n `126` status `ready` deltaP `12.1468` edge `0.0368` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
