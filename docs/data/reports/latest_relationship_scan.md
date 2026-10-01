# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T17:07:31.240439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6796`

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

- `market_context_high->unknown_1h` score `334.8158` n `50` status `ready` deltaP `7.8802` edge `27.8537` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `284.5624` n `50` status `ready` deltaP `6.8598` edge `23.6678` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1983` n `111` status `ready` deltaP `34.6565` edge `1.4731` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.0973` n `50` status `ready` deltaP `32.6944` edge `0.7651` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.5022` n `50` status `ready` deltaP `20.1341` edge `0.5613` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2246` n `50` status `ready` deltaP `16.9512` edge `0.4517` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `5.0951` n `111` status `ready` deltaP `21.8656` edge `0.5942` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.9111` n `50` status `ready` deltaP `10.4583` edge `0.5105` maxDD `-11.6768`
- `market_context_high->equity_24h` score `4.0053` n `50` status `ready` deltaP `19.2153` edge `0.5716` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4145` n `124` status `ready` deltaP `27.0506` edge `0.1738` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1552` n `50` status `ready` deltaP `35.4329` edge `0.0402` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `3.1111` n `111` status `ready` deltaP `22.3865` edge `0.4845` maxDD `-9.4579`
- `market_context_high->crypto_major_1h` score `3.0611` n `50` status `ready` deltaP `14.7485` edge `0.2018` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.983` n `50` status `ready` deltaP `13.7545` edge `0.2232` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.546` n `111` status `ready` deltaP `24.9719` edge `0.0935` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2996` n `111` status `ready` deltaP `27.1678` edge `0.2411` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5645` n `50` status `ready` deltaP `21.6886` edge `0.0122` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8933` n `50` status `ready` deltaP `14.7917` edge `0.073` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5219` n `50` status `ready` deltaP `14.4306` edge `0.0725` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.5134` n `124` status `ready` deltaP `7.1905` edge `0.0485` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
