# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T00:22:32.577966+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `302.9785` n `84` status `ready` deltaP `6.2996` edge `25.2203` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `69.3786` n `94` status `ready` deltaP `8.1053` edge `5.7723` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.2158` n `53` status `ready` deltaP `25.6814` edge `2.4174` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.1984` n `84` status `ready` deltaP `23.4127` edge `1.7644` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.0032` n `53` status `ready` deltaP `38.2239` edge `1.4806` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4285` n `53` status `ready` deltaP `32.7341` edge `0.6805` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.0736` n `84` status `ready` deltaP `43.8244` edge `1.2807` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.1627` n `53` status `ready` deltaP `43.2292` edge `0.3087` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5327` n `84` status `ready` deltaP `40.0794` edge `0.3185` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6154` n `53` status `ready` deltaP `43.9571` edge `0.1292` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3202` n `84` status `ready` deltaP `24.6776` edge `0.205` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9119` n `53` status `ready` deltaP `22.8806` edge `0.2038` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `2.9685` n `53` status `ready` deltaP `27.1687` edge `0.0916` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.8884` n `53` status `ready` deltaP `16.3682` edge `0.1946` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6907` n `53` status `ready` deltaP `19.6762` edge `0.2418` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1559` n `53` status `ready` deltaP `25.4406` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6835` n `53` status `ready` deltaP `18.0022` edge `0.0639` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.636` n `53` status `ready` deltaP `13.9052` edge `0.5676` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.3766` n `53` status `ready` deltaP `24.5168` edge `0.1769` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1016` n `53` status `ready` deltaP `15.679` edge `0.0174` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
