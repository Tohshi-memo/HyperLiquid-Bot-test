# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T22:37:30.376101+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4542`

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

- `news_risk_high->crypto_alt_4h` score `0.2269` n `146` status `ready` deltaP `5.7802` edge `0.2542` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.49` n `146` status `ready` deltaP `1.4334` edge `0.0504` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.614` n `146` status `ready` deltaP `-0.8756` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.889` n `126` status `ready` deltaP `12.5744` edge `0.1278` maxDD `-14.0483`
- `news_risk_high->crypto_alt_24h` score `-0.8987` n `126` status `ready` deltaP `19.3204` edge `0.7065` maxDD `-65.3749`
- `news_risk_high->index_1h` score `-0.9478` n `146` status `ready` deltaP `0.7485` edge `-0.004` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2854` n `146` status `ready` deltaP `-4.1159` edge `-0.0122` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3242` n `146` status `ready` deltaP `-5.5471` edge `-0.0106` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0851` n `146` status `ready` deltaP `-3.2743` edge `-0.0154` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3121` n `146` status `ready` deltaP `-8.3279` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3724` n `126` status `ready` deltaP `-5.0348` edge `0.0136` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4317` n `126` status `ready` deltaP `-19.0477` edge `-0.0139` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6369` n `146` status `ready` deltaP `-6.0372` edge `-0.0302` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2331` n `146` status `ready` deltaP `-8.1556` edge `-0.0425` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.3322` n `126` status `ready` deltaP `14.4593` edge `0.4859` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.7342` n `146` status `ready` deltaP `-11.4079` edge `0.0003` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7829` n `146` status `ready` deltaP `-6.5382` edge `-0.0345` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.7846` n `146` status `ready` deltaP `-13.0116` edge `-0.0767` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.15` n `126` status `ready` deltaP `-16.6666` edge `-0.0537` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.3822` n `146` status `ready` deltaP `-1.2926` edge `-0.1038` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
