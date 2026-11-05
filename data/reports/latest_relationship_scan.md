# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T03:37:25.189080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3812`

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

- `news_risk_high->crypto_alt_4h` score `-0.4574` n `146` status `ready` deltaP `6.3899` edge `0.1624` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.7061` n `146` status `ready` deltaP `1.2837` edge `0.0237` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7417` n `146` status `ready` deltaP `-3.2708` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8101` n `146` status `ready` deltaP `2.2455` edge `-0.0025` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5524` n `146` status `ready` deltaP `-8.6908` edge `-0.0189` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5968` n `146` status `ready` deltaP `-9.9085` edge `-0.0135` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8602` n `146` status `ready` deltaP `-0.0731` edge `-0.0079` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1478` n `146` status `ready` deltaP `-7.7291` edge `0.0092` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4359` n `146` status `ready` deltaP `-18.6638` edge `-0.017` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.643` n `146` status `ready` deltaP `-6.636` edge `-0.027` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.7292` n `146` status `ready` deltaP `-10.9518` edge `0.0073` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1682` n `146` status `ready` deltaP `-9.8835` edge `0.0373` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.5031` n `146` status `ready` deltaP `-8.1556` edge `-0.065` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.3382` n `146` status `ready` deltaP `-9.1296` edge `-0.0635` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.5649` n `146` status `ready` deltaP `-2.9625` edge `-0.0858` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.7662` n `146` status `ready` deltaP `-13.0116` edge `-0.1585` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.9186` n `146` status `ready` deltaP `-20.1616` edge `0.0506` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.9733` n `146` status `ready` deltaP `0.3842` edge `-0.0809` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-12.9193` n `146` status `ready` deltaP `8.7667` edge `-0.0153` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.2256` n `146` status `ready` deltaP `10.6698` edge `0.2771` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
