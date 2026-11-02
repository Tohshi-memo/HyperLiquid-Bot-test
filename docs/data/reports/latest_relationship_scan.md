# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T14:07:27.989237+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4863`

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

- `news_risk_high->crypto_alt_4h` score `-0.0097` n `146` status `ready` deltaP `5.4753` edge `0.2259` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.5338` n `146` status `ready` deltaP `0.6214` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5485` n `146` status `ready` deltaP `1.134` edge `0.0449` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8227` n `126` status `ready` deltaP `12.5744` edge `0.1363` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0688` n `146` status `ready` deltaP `-0.4491` edge `-0.0061` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1255` n `146` status `ready` deltaP `-1.2195` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2868` n `146` status `ready` deltaP `-4.9483` edge `-0.0098` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-1.9726` n `126` status `ready` deltaP `-13.1449` edge `0.0056` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2212` n `146` status `ready` deltaP `-4.6463` edge `-0.0237` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3697` n `146` status `ready` deltaP `-8.4776` edge `-0.0043` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5663` n `126` status `ready` deltaP `-6.4237` edge `-0.002` maxDD `-7.402`
- `news_risk_high->crypto_alt_24h` score `-2.6558` n `126` status `ready` deltaP `14.2857` edge `0.5148` maxDD `-65.3749`
- `news_risk_high->equity_1h` score `-2.8988` n `146` status `ready` deltaP `-7.3845` edge `-0.0548` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3458` n `146` status `ready` deltaP `-8.7544` edge `-0.0479` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.923` n `146` status `ready` deltaP `-11.7128` edge `-0.0134` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.561` n `146` status `ready` deltaP `-4.7089` edge `-0.0282` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.0711` n `126` status `ready` deltaP `8.9038` edge `0.3` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.241` n `146` status `ready` deltaP `-14.2312` edge `-0.1066` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.2187` n `126` status `ready` deltaP `-22.3958` edge `-0.1879` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.3774` n `126` status `ready` deltaP `-26.4881` edge `-0.166` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
