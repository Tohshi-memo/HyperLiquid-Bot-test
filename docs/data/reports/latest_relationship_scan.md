# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T06:37:27.651748+00:00`
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

- `market_context_high->unknown_1h` score `10078.2485` n `126` status `ready` deltaP `1.1643` edge `839.8661` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6143.4945` n `126` status `ready` deltaP `-0.3145` edge `511.9905` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.5488` n `108` status `ready` deltaP `26.794` edge `1.0831` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1922` n `126` status `ready` deltaP `3.9516` edge `0.0155` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.296` n `126` status `ready` deltaP `2.8585` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5029` n `126` status `ready` deltaP `11.7958` edge `0.0375` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3819` n `126` status `ready` deltaP `-8.6565` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7532` n `126` status `ready` deltaP `6.1377` edge `0.0189` maxDD `-13.1399`
- `market_context_high->crypto_alt_24h` score `-1.8547` n `108` status `ready` deltaP `13.8311` edge `0.7433` maxDD `-72.5383`
- `market_context_high->fx_4h` score `-1.9334` n `126` status `ready` deltaP `-7.0315` edge `0.0006` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.244` n `126` status `ready` deltaP `-7.7726` edge `-0.022` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.2832` n `126` status `ready` deltaP `3.1579` edge `0.0205` maxDD `-13.8788`
- `market_context_high->index_4h` score `-2.3447` n `126` status `ready` deltaP `-2.8794` edge `-0.0129` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.0096` n `126` status `ready` deltaP `-3.4455` edge `-0.0001` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1036` n `126` status `ready` deltaP `-0.3461` edge `0.1691` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8427` n `108` status `ready` deltaP `12.4422` edge `0.1195` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.4968` n `108` status `ready` deltaP `-15.9144` edge `-0.008` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8444` n `126` status `ready` deltaP `-18.358` edge `-0.0787` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.2145` n `126` status `ready` deltaP `-0.6509` edge `0.0844` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.6648` n `108` status `ready` deltaP `-26.3888` edge `-0.1165` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
