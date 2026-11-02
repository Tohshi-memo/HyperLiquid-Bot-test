# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T17:37:26.165881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4987`

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

- `news_risk_high->crypto_alt_4h` score `-0.1298` n `146` status `ready` deltaP `4.5607` edge `0.2166` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4799` n `146` status `ready` deltaP `1.7328` edge `0.0497` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5502` n `146` status `ready` deltaP `0.322` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8765` n `126` status `ready` deltaP `12.5744` edge `0.1294` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0377` n `146` status `ready` deltaP `-0.1497` edge `-0.0055` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2094` n `146` status `ready` deltaP `-2.7439` edge `-0.0116` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3452` n `146` status `ready` deltaP `-5.8465` edge `-0.0113` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-2.1346` n `126` status `ready` deltaP `15.8482` edge `0.5712` maxDD `-65.3749`
- `news_risk_high->fx_24h` score `-2.163` n `126` status `ready` deltaP `-15.5754` edge `-0.0026` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.263` n `146` status `ready` deltaP `-7.7291` edge `-0.0004` maxDD `-3.2657`
- `news_risk_high->index_4h` score `-2.2711` n `146` status `ready` deltaP `-5.5609` edge `-0.024` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.5421` n `126` status `ready` deltaP `-6.4237` edge `0.0011` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.7507` n `146` status `ready` deltaP `-6.636` edge `-0.0408` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1959` n `146` status `ready` deltaP `-7.8562` edge `-0.0414` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7636` n `146` status `ready` deltaP `-10.9506` edge `-0.0052` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.5884` n `126` status `ready` deltaP `10.9871` edge `0.348` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8141` n `146` status `ready` deltaP `-6.5382` edge `-0.0371` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2992` n `146` status `ready` deltaP `-14.6885` edge `-0.1084` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.6013` n `126` status `ready` deltaP `-20.1389` edge `-0.1515` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.2298` n `126` status `ready` deltaP `-26.4881` edge `-0.1537` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
