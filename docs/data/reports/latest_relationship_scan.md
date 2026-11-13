# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T00:37:27.724625+00:00`
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

- `market_context_high->unknown_24h` score `302.0965` n `84` status `ready` deltaP `6.2996` edge `25.1468` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `66.3246` n `94` status `ready` deltaP `8.1053` edge `5.5178` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.3209` n `53` status `ready` deltaP `25.855` edge `2.425` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.3035` n `84` status `ready` deltaP `23.5863` edge `1.772` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.0473` n `53` status `ready` deltaP `38.3976` edge `1.4851` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4597` n `53` status `ready` deltaP `32.7341` edge `0.6831` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.1286` n `84` status `ready` deltaP `43.998` edge `1.2866` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.1471` n `53` status `ready` deltaP `43.2292` edge `0.3074` maxDD `0.0`
- `market_context_high->metal_24h` score `6.561` n `84` status `ready` deltaP `40.253` edge `0.3197` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5984` n `53` status `ready` deltaP `43.8047` edge `0.1288` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3298` n `84` status `ready` deltaP `24.6776` edge `0.2058` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9215` n `53` status `ready` deltaP `22.8806` edge `0.2046` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `2.9867` n `53` status `ready` deltaP `27.3211` edge `0.0921` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.9388` n `53` status `ready` deltaP `16.5179` edge `0.1978` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6943` n `53` status `ready` deltaP `19.6762` edge `0.2421` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1571` n `53` status `ready` deltaP `25.4406` edge `0.0356` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.691` n `53` status `ready` deltaP `14.0788` edge `0.5735` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6871` n `53` status `ready` deltaP `18.0022` edge `0.0642` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.3906` n `53` status `ready` deltaP `24.5168` edge `0.1787` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1052` n `53` status `ready` deltaP `15.679` edge `0.0177` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
