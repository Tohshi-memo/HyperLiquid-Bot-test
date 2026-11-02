# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T17:07:34.428290+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4939`

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

- `news_risk_high->crypto_alt_4h` score `-0.1314` n `146` status `ready` deltaP `4.5607` edge `0.2164` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4854` n `146` status `ready` deltaP `1.7328` edge `0.049` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5346` n `146` status `ready` deltaP `0.6214` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8695` n `126` status `ready` deltaP `12.5744` edge `0.1303` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0377` n `146` status `ready` deltaP `-0.1497` edge `-0.0055` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1928` n `146` status `ready` deltaP `-2.439` edge `-0.0115` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3452` n `146` status `ready` deltaP `-5.8465` edge `-0.0113` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.1355` n `126` status `ready` deltaP `-15.2282` edge `-0.0014` maxDD `-2.336`
- `news_risk_high->crypto_alt_24h` score `-2.2345` n `126` status `ready` deltaP `15.501` edge `0.5607` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.2624` n `146` status `ready` deltaP `-5.4085` edge `-0.0239` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.263` n `146` status `ready` deltaP `-7.7291` edge `-0.0004` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5468` n `126` status `ready` deltaP `-6.4237` edge `0.0005` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.767` n `146` status `ready` deltaP `-6.7857` edge `-0.0419` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2139` n `146` status `ready` deltaP `-7.8562` edge `-0.0429` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7816` n `146` status `ready` deltaP `-10.9506` edge `-0.0067` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.6751` n `126` status `ready` deltaP `10.6399` edge `0.3392` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.7741` n `146` status `ready` deltaP `-6.2333` edge `-0.0358` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.3052` n `146` status `ready` deltaP `-14.6885` edge `-0.1089` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.7263` n `126` status `ready` deltaP `-20.4861` edge `-0.1596` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.2574` n `126` status `ready` deltaP `-26.4881` edge `-0.156` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
