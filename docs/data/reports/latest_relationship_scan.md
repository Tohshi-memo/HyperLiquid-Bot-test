# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T05:52:26.762362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.7119` n `146` status `ready` deltaP `9.2863` edge `0.293` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3771` n `146` status `ready` deltaP `2.7807` edge `0.0559` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6926` n `146` status `ready` deltaP `-2.3726` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7501` n `146` status `ready` deltaP `2.6946` edge `-0.0005` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2627` n `146` status `ready` deltaP `-4.6489` edge `-0.0087` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.373` n `146` status `ready` deltaP `11.9506` edge `0.1641` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4638` n `146` status `ready` deltaP `-7.622` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6451` n `146` status `ready` deltaP `2.5923` edge `0.056` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.734` n `146` status `ready` deltaP `0.6891` edge `0.0032` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3345` n `146` status `ready` deltaP `-17.8534` edge `-0.0094` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4438` n `146` status `ready` deltaP `-9.8249` edge `-0.0015` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.4973` n `146` status `ready` deltaP `-5.139` edge `-0.0183` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0473` n `146` status `ready` deltaP `-6.958` edge `-0.035` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8014` n `146` status `ready` deltaP `-12.3225` edge `0.0008` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3128` n `146` status `ready` deltaP `-3.0321` edge `-0.0187` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0215` n `146` status `ready` deltaP `-10.2677` edge `-0.0314` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.6303` n `146` status `ready` deltaP `20.5837` edge `0.7122` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.6117` n `146` status `ready` deltaP `18.1531` edge `0.6117` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.3331` n `146` status `ready` deltaP `0.8415` edge `-0.0306` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3237` n `146` status `ready` deltaP `-20.6098` edge `-0.0635` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
