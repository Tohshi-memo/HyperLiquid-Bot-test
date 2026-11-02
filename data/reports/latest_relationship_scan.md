# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T23:22:28.349217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4550`

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

- `news_risk_high->crypto_alt_4h` score `0.1821` n `146` status `ready` deltaP `5.3229` edge `0.2515` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4355` n `146` status `ready` deltaP `1.8825` edge `0.0544` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5977` n `146` status `ready` deltaP `-0.5762` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->crypto_alt_24h` score `-0.7047` n `126` status `ready` deltaP `19.8413` edge `0.7279` maxDD `-65.3749`
- `news_risk_high->metal_24h` score `-0.8851` n `126` status `ready` deltaP `12.5744` edge `0.1283` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9179` n `146` status `ready` deltaP `1.0479` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.268` n `146` status `ready` deltaP `-3.811` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3156` n `146` status `ready` deltaP `-5.3974` edge `-0.0105` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0551` n `146` status `ready` deltaP `-2.817` edge `-0.0146` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3133` n `146` status `ready` deltaP `-8.3279` edge `-0.0006` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3462` n `126` status `ready` deltaP `-4.8612` edge `0.0158` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4704` n `126` status `ready` deltaP `-19.5685` edge `-0.0154` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6033` n `146` status `ready` deltaP `-5.7378` edge `-0.0279` maxDD `-16.4088`
- `news_risk_high->equity_24h` score `-3.1336` n `126` status `ready` deltaP `14.9801` edge `0.5079` maxDD `-67.0937`
- `news_risk_high->crypto_major_1h` score `-3.1564` n `146` status `ready` deltaP `-7.7065` edge `-0.0391` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7488` n `146` status `ready` deltaP `-11.5604` edge `0.0001` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7865` n `146` status `ready` deltaP `-6.5382` edge `-0.0348` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8136` n `146` status `ready` deltaP `-13.1641` edge `-0.0781` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.9175` n `126` status `ready` deltaP `-16.1458` edge `-0.0378` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.329` n `146` status `ready` deltaP `-0.9877` edge `-0.1014` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
