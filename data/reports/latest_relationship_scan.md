# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T04:22:31.150360+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4314`

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

- `news_risk_high->crypto_alt_4h` score `-0.1917` n `146` status `ready` deltaP `6.9997` edge `0.1924` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5479` n `146` status `ready` deltaP `3.2298` edge `0.031` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6639` n `146` status `ready` deltaP `3.4431` edge `0.0017` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7129` n `146` status `ready` deltaP `-2.8217` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.467` n `146` status `ready` deltaP `-7.622` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5228` n `146` status `ready` deltaP `-8.092` edge `-0.0191` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6846` n `146` status `ready` deltaP `0.994` edge `0.0075` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3678` n `146` status `ready` deltaP `-5.4384` edge `0.0003` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.4046` n `146` status `ready` deltaP `-12.1628` edge `0.057` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.5456` n `146` status `ready` deltaP `-11.3219` edge `0.0` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.8004` n `146` status `ready` deltaP `-5.0119` edge `-0.0274` maxDD `-9.4709`
- `news_risk_high->fx_24h` score `-2.8256` n `146` status `ready` deltaP `-24.3731` edge `-0.0289` maxDD `-2.336`
- `news_risk_high->commodity_4h` score `-4.0073` n `146` status `ready` deltaP `-15.6762` edge `0.006` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7559` n `146` status `ready` deltaP `-12.9406` edge `-0.0729` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.757` n `146` status `ready` deltaP `-8.8958` edge `-0.0185` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1724` n `146` status `ready` deltaP `-16.9763` edge `-0.293` maxDD `-16.6552`
- `news_risk_high->equity_4h` score `-9.6739` n `146` status `ready` deltaP `2.0611` edge `0.0162` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-9.8587` n `146` status `ready` deltaP `-16.1824` edge `0.1124` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-10.2318` n `146` status `ready` deltaP `9.9778` edge `0.5312` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-12.9029` n `146` status `ready` deltaP `6.1715` edge `0.0041` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
