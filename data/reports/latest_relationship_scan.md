# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T17:57:47.611722+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4026`

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

- `news_risk_high->crypto_alt_4h` score `0.0023` n `146` status `ready` deltaP `7.7619` edge `0.2122` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5564` n `146` status `ready` deltaP `2.1819` edge `0.0369` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6249` n `146` status `ready` deltaP `-1.175` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.87` n `146` status `ready` deltaP `1.497` edge `-0.0025` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4228` n `146` status `ready` deltaP `-7.0122` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.4301` n `146` status `ready` deltaP `-6.8944` edge `-0.0152` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.8426` n `146` status `ready` deltaP `0.3842` edge `-0.0087` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1358` n `146` status `ready` deltaP `-7.7291` edge `0.0102` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.1503` n `146` status `ready` deltaP `-4.3774` edge `0.0377` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4452` n `146` status `ready` deltaP `-18.6638` edge `-0.0182` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6329` n `146` status `ready` deltaP `-6.7857` edge `-0.0247` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3376` n `146` status `ready` deltaP `-7.5568` edge `-0.0552` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.3628` n `146` status `ready` deltaP `-10.036` edge `0.0221` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-3.3931` n `146` status `ready` deltaP `3.7849` edge `0.0502` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.8367` n `146` status `ready` deltaP `-5.4711` edge `-0.0461` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2033` n `146` status `ready` deltaP `-11.9446` edge `-0.1187` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.0492` n `146` status `ready` deltaP `14.8221` edge `0.4405` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9411` n `146` status `ready` deltaP `0.2318` edge `-0.0772` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4091` n `146` status `ready` deltaP `11.8809` edge `0.4204` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.1913` n `146` status `ready` deltaP `-20.6807` edge `-0.052` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
