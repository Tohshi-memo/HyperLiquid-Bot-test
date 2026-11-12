# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T17:22:25.159025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `300.2479` n `84` status `ready` deltaP `6.4425` edge `24.9918` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `89.037` n `94` status `ready` deltaP `8.1053` edge `7.4105` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.6439` n `53` status `ready` deltaP `21.5676` edge `2.2305` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.6265` n `84` status `ready` deltaP `19.2989` edge `1.5775` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.1039` n `53` status `ready` deltaP `37.0699` edge `1.373` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.5937` n `53` status `ready` deltaP `33.3438` edge `0.6902` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.5396` n `53` status `ready` deltaP `43.4256` edge `0.3388` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.457` n `84` status `ready` deltaP `39.0757` edge `1.1051` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.1235` n `84` status `ready` deltaP `38.8491` edge `0.2926` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.74` n `53` status `ready` deltaP `44.7193` edge `0.1345` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8653` n `84` status `ready` deltaP `21.272` edge `0.1898` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.457` n `53` status `ready` deltaP `19.475` edge `0.1886` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.1398` n `53` status `ready` deltaP `21.8103` edge `0.265` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.1271` n `53` status `ready` deltaP `17.4161` edge `0.2075` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0375` n `53` status `ready` deltaP `26.7114` edge `0.1004` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2769` n `53` status `ready` deltaP `26.6382` edge `0.0376` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.7972` n `53` status `ready` deltaP `18.7644` edge `0.0683` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5882` n `53` status `ready` deltaP `25.7363` edge `0.1959` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2286` n `53` status `ready` deltaP `16.8766` edge `0.02` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6123` n `53` status `ready` deltaP `18.4922` edge `0.0604` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
