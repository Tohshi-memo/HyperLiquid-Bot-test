# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T17:37:28.205221+00:00`
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

- `market_context_high->unknown_24h` score `301.0459` n `84` status `ready` deltaP `6.4425` edge `25.0583` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `88.2426` n `94` status `ready` deltaP `8.1053` edge `7.3443` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.7051` n `53` status `ready` deltaP `21.5676` edge `2.2356` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.6877` n `84` status `ready` deltaP `19.2989` edge `1.5826` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.1288` n `53` status `ready` deltaP `37.0699` edge `1.3762` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.5359` n `53` status `ready` deltaP `33.1914` edge `0.6864` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.536` n `53` status `ready` deltaP `43.4256` edge `0.3385` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.5315` n `84` status `ready` deltaP `39.2487` edge `1.1135` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.1355` n `84` status `ready` deltaP `38.8491` edge `0.2936` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.74` n `53` status `ready` deltaP `44.7193` edge `0.1345` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8678` n `84` status `ready` deltaP `21.272` edge `0.19` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4594` n `53` status `ready` deltaP `19.475` edge `0.1888` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.1218` n `53` status `ready` deltaP `21.8103` edge `0.2635` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.1055` n `53` status `ready` deltaP `17.4161` edge `0.2057` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0375` n `53` status `ready` deltaP `26.7114` edge `0.1004` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2637` n `53` status `ready` deltaP `26.4885` edge `0.0375` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.7766` n `53` status `ready` deltaP `18.6119` edge `0.0676` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5905` n `53` status `ready` deltaP `25.7363` edge `0.1962` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2142` n `53` status `ready` deltaP `16.7269` edge `0.0198` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.589` n `53` status `ready` deltaP `18.3425` edge `0.0584` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
