# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T04:07:23.613127+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.2081` n `146` status `ready` deltaP `6.9997` edge `0.1903` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5737` n `146` status `ready` deltaP `3.0801` edge `0.0287` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6782` n `146` status `ready` deltaP `3.2934` edge `0.0015` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7136` n `146` status `ready` deltaP `-2.8217` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.467` n `146` status `ready` deltaP `-7.622` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5314` n `146` status `ready` deltaP `-8.2417` edge `-0.0192` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6846` n `146` status `ready` deltaP `0.994` edge `0.0075` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3873` n `146` status `ready` deltaP `-5.5881` edge `-0.0012` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.4139` n `146` status `ready` deltaP `-12.1628` edge `0.0558` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.5312` n `146` status `ready` deltaP `-11.1722` edge `0.0002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.8158` n `146` status `ready` deltaP `-24.2001` edge `-0.0288` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.8436` n `146` status `ready` deltaP `-5.1616` edge `-0.03` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9879` n `146` status `ready` deltaP `-15.5238` edge `0.0066` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7583` n `146` status `ready` deltaP `-12.9406` edge `-0.0731` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.8052` n `146` status `ready` deltaP `-9.0482` edge `-0.0215` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1724` n `146` status `ready` deltaP `-16.9763` edge `-0.293` maxDD `-16.6552`
- `news_risk_high->equity_4h` score `-9.6619` n `146` status `ready` deltaP `2.0611` edge `0.0172` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-9.8112` n `146` status `ready` deltaP `-16.0094` edge `0.1152` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-10.3122` n `146` status `ready` deltaP `9.9778` edge `0.5245` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-13.0219` n `146` status `ready` deltaP `5.9985` edge `-0.01` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
