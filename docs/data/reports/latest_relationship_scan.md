# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T07:37:31.189867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2700`

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

- `market_context_high->unknown_1h` score `10064.0261` n `126` status `ready` deltaP `1.1643` edge `838.6809` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6141.1137` n `126` status `ready` deltaP `-0.3145` edge `511.7921` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6338` n `108` status `ready` deltaP `26.794` edge `1.094` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1976` n `126` status `ready` deltaP `3.9516` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3232` n `126` status `ready` deltaP `2.4094` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5029` n `126` status `ready` deltaP `11.7958` edge `0.0375` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3651` n `126` status `ready` deltaP `-8.5068` edge `-0.0011` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8431` n `126` status `ready` deltaP `5.8383` edge `0.0134` maxDD `-13.1399`
- `market_context_high->crypto_alt_24h` score `-1.8907` n `108` status `ready` deltaP `13.8311` edge `0.7403` maxDD `-72.5383`
- `market_context_high->fx_4h` score `-1.9287` n `126` status `ready` deltaP `-7.0315` edge `0.0012` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2044` n `126` status `ready` deltaP `-7.3235` edge `-0.0217` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3471` n `126` status `ready` deltaP `-2.8794` edge `-0.0131` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5459` n `126` status `ready` deltaP `2.8585` edge `0.0006` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2447` n `126` status `ready` deltaP `-3.8946` edge `-0.0167` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1396` n `126` status `ready` deltaP `-0.4985` edge `0.1655` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8667` n `108` status `ready` deltaP `12.4422` edge `0.1175` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.4245` n `108` status `ready` deltaP `-15.2199` edge `-0.0066` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8042` n `126` status `ready` deltaP `-17.9007` edge `-0.0784` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.2783` n `126` status `ready` deltaP `-0.8034` edge `0.0801` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.6312` n `108` status `ready` deltaP `-26.3888` edge `-0.1137` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
