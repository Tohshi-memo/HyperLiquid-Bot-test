# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T18:07:38.094346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4954`

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

- `news_risk_high->crypto_alt_4h` score `-0.1041` n `146` status `ready` deltaP `4.5607` edge `0.2199` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4721` n `146` status `ready` deltaP `1.7328` edge `0.0507` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.558` n `146` status `ready` deltaP `0.1723` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.882` n `126` status `ready` deltaP `12.5744` edge `0.1287` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0365` n `146` status `ready` deltaP `-0.1497` edge `-0.0054` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2268` n `146` status `ready` deltaP `-3.0488` edge `-0.0118` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3444` n `146` status `ready` deltaP `-5.8465` edge `-0.0112` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-2.0245` n `126` status `ready` deltaP `16.1954` edge `0.583` maxDD `-65.3749`
- `news_risk_high->fx_24h` score `-2.1904` n `126` status `ready` deltaP `-15.9227` edge `-0.0038` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.245` n `146` status `ready` deltaP `-7.5794` edge `0.0001` maxDD `-3.2657`
- `news_risk_high->index_4h` score `-2.2688` n `146` status `ready` deltaP `-5.5609` edge `-0.0237` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.5367` n `126` status `ready` deltaP `-6.4237` edge `0.0018` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.7397` n `146` status `ready` deltaP `-6.636` edge `-0.0394` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1839` n `146` status `ready` deltaP `-7.8562` edge `-0.0404` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.748` n `146` status `ready` deltaP `-10.9506` edge `-0.0039` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.4963` n `126` status `ready` deltaP `11.3343` edge `0.3575` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8445` n `146` status `ready` deltaP `-6.843` edge `-0.0376` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2704` n `146` status `ready` deltaP `-14.6885` edge `-0.106` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.474` n `126` status `ready` deltaP `-19.7916` edge `-0.1432` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.1926` n `126` status `ready` deltaP `-26.4881` edge `-0.1506` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
