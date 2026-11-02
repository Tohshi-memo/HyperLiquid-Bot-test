# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T14:22:41.555430+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4879`

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

- `news_risk_high->crypto_alt_4h` score `-0.0011` n `146` status `ready` deltaP `5.4753` edge `0.227` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.526` n `146` status `ready` deltaP `0.7711` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5352` n `146` status `ready` deltaP `1.134` edge `0.0466` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8235` n `126` status `ready` deltaP `12.5744` edge `0.1362` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0652` n `146` status `ready` deltaP `-0.4491` edge `-0.0058` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1168` n `146` status `ready` deltaP `-1.0671` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.286` n `146` status `ready` deltaP `-4.9483` edge `-0.0097` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-1.9855` n `126` status `ready` deltaP `-13.3185` edge `0.0051` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2181` n `146` status `ready` deltaP `-4.6463` edge `-0.0233` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3505` n `146` status `ready` deltaP `-8.3279` edge `-0.0037` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5648` n `126` status `ready` deltaP `-6.4237` edge `-0.0018` maxDD `-7.402`
- `news_risk_high->crypto_alt_24h` score `-2.6116` n `126` status `ready` deltaP `14.4593` edge `0.5193` maxDD `-65.3749`
- `news_risk_high->equity_1h` score `-2.8816` n `146` status `ready` deltaP `-7.3845` edge `-0.0526` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3314` n `146` status `ready` deltaP `-8.7544` edge `-0.0467` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9024` n `146` status `ready` deltaP `-11.5604` edge `-0.0127` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.561` n `146` status `ready` deltaP `-4.7089` edge `-0.0282` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.0462` n `126` status `ready` deltaP `8.9038` edge `0.3032` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2096` n `146` status `ready` deltaP `-14.0787` edge `-0.105` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.1712` n `126` status `ready` deltaP `-22.2222` edge `-0.1851` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.3618` n `126` status `ready` deltaP `-26.4881` edge `-0.1647` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
