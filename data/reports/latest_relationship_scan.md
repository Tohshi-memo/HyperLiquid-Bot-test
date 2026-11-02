# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T16:52:35.454335+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4951`

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

- `news_risk_high->crypto_alt_4h` score `-0.1228` n `146` status `ready` deltaP `4.5607` edge `0.2175` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4877` n `146` status `ready` deltaP `1.7328` edge `0.0487` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5338` n `146` status `ready` deltaP `0.6214` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.864` n `126` status `ready` deltaP `12.5744` edge `0.131` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0509` n `146` status `ready` deltaP `-0.2994` edge `-0.0056` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1841` n `146` status `ready` deltaP `-2.2866` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3359` n `146` status `ready` deltaP `-5.6968` edge `-0.0111` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.1218` n `126` status `ready` deltaP `-15.0546` edge `-0.0008` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2545` n `146` status `ready` deltaP `-5.256` edge `-0.0239` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2654` n `146` status `ready` deltaP `-7.7291` edge `-0.0006` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.2779` n `126` status `ready` deltaP `15.3274` edge `0.5563` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5492` n `126` status `ready` deltaP `-6.4237` edge `0.0002` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.7834` n `146` status `ready` deltaP `-6.9354` edge `-0.043` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2307` n `146` status `ready` deltaP `-8.0059` edge `-0.0433` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.79` n `146` status `ready` deltaP `-10.9506` edge `-0.0074` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.7145` n `126` status `ready` deltaP `10.4663` edge `0.3353` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.7523` n `146` status `ready` deltaP `-6.0809` edge `-0.035` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2956` n `146` status `ready` deltaP `-14.6885` edge `-0.1081` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.7762` n `126` status `ready` deltaP `-20.6597` edge `-0.1626` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.2694` n `126` status `ready` deltaP `-26.4881` edge `-0.157` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
