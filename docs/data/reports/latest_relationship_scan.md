# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T03:37:34.410054+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11780`

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

- `market_context_high->unknown_24h` score `290.8633` n `84` status `ready` deltaP `6.2996` edge `24.2107` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `56.1526` n `94` status `ready` deltaP `7.4955` edge `4.6742` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.0153` n `53` status `ready` deltaP `27.5911` edge `2.4713` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.9979` n `84` status `ready` deltaP `25.3224` edge `1.8183` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.4601` n `53` status `ready` deltaP `39.092` edge `1.5334` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.6122` n `84` status `ready` deltaP `46.0814` edge `1.3347` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.4381` n `53` status `ready` deltaP `32.7341` edge `0.6813` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.8689` n `53` status `ready` deltaP `42.3611` edge `0.29` maxDD `0.0`
- `market_context_high->metal_24h` score `6.7897` n `84` status `ready` deltaP `41.6419` edge `0.3295` maxDD `-0.3044`
- `market_context_high->index_24h` score `4.3809` n `84` status `ready` deltaP `24.8512` edge `0.2089` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.3429` n `53` status `ready` deltaP `41.9754` edge `0.1197` maxDD `-1.0104`
- `news_risk_high->index_24h` score `3.9726` n `53` status `ready` deltaP `23.0542` edge `0.2077` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.1955` n `53` status `ready` deltaP `29.1504` edge `0.0973` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1487` n `53` status `ready` deltaP `17.2664` edge `0.2103` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6915` n `53` status `ready` deltaP `19.3713` edge `0.2439` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.1745` n `53` status `ready` deltaP `16.1622` edge `0.6216` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0528` n `53` status `ready` deltaP `24.5424` edge `0.0329` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6579` n `53` status `ready` deltaP `17.6973` edge `0.0638` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5276` n `53` status `ready` deltaP `25.1265` edge `0.1922` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
