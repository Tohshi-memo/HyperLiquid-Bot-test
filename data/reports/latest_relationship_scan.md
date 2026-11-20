# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T21:37:31.411573+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2748`

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

- `market_context_high->unknown_1h` score `10139.9753` n `126` status `ready` deltaP `1.4638` edge `845.008` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6182.7813` n `126` status `ready` deltaP `-0.3145` edge `515.2644` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6775` n `108` status `ready` deltaP `26.794` edge `1.0996` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1836` n `126` status `ready` deltaP `4.1013` edge `0.0156` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2376` n `126` status `ready` deltaP `3.9064` edge `0.0047` maxDD `-1.2295`
- `market_context_high->crypto_alt_24h` score `-0.2695` n `108` status `ready` deltaP `13.8311` edge `0.8754` maxDD `-72.5383`
- `market_context_high->metal_4h` score `-0.4823` n `126` status `ready` deltaP `12.2531` edge `0.0371` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3843` n `126` status `ready` deltaP `-8.6565` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.704` n `126` status `ready` deltaP `6.2874` edge `0.022` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9887` n `126` status `ready` deltaP `-7.9462` edge `-0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.25` n `126` status `ready` deltaP `-7.7726` edge `-0.0225` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.2838` n `126` status `ready` deltaP `-2.1172` edge `-0.0129` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.3072` n `126` status `ready` deltaP `3.3076` edge `0.0175` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.0253` n `126` status `ready` deltaP `-2.8467` edge `-0.0054` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1672` n `126` status `ready` deltaP `1.0259` edge `0.1518` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.7278` n `108` status `ready` deltaP `12.963` edge `0.1256` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8166` n `108` status `ready` deltaP `-19.3866` edge `-0.0115` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9548` n `126` status `ready` deltaP `-20.1873` edge `-0.0757` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.148` n `126` status `ready` deltaP `1.6357` edge `0.0747` maxDD `-46.5016`
- `market_context_high->index_24h` score `-13.0308` n `108` status `ready` deltaP `-26.3888` edge `-0.147` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
