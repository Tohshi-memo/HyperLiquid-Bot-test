# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T13:07:25.250403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3787`

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

- `news_risk_high->crypto_alt_4h` score `0.0787` n `146` status `ready` deltaP `7.6094` edge `0.223` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4372` n `146` status `ready` deltaP `3.5292` edge `0.0432` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7323` n `146` status `ready` deltaP `-3.1211` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7418` n `146` status `ready` deltaP `2.8443` edge `-0.0008` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4505` n `146` status `ready` deltaP `-7.4695` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.568` n `146` status `ready` deltaP `-8.8405` edge `-0.0199` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7703` n `146` status `ready` deltaP `1.1464` edge `-0.0045` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2668` n `146` status `ready` deltaP `-16.1173` edge `-0.0123` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3755` n `146` status `ready` deltaP `-9.5255` edge `0.0022` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.4809` n `146` status `ready` deltaP `-5.139` edge `-0.0162` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9386` n `146` status `ready` deltaP `-12.3382` edge `-0.0103` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.0714` n `146` status `ready` deltaP `-5.9101` edge `-0.044` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6823` n `146` status `ready` deltaP `-13.0847` edge `0.0158` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6707` n `146` status `ready` deltaP `-12.026` edge `-0.0719` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.6521` n `146` status `ready` deltaP `-10.7251` edge `-0.0809` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.309` n `146` status `ready` deltaP `-9.4035` edge `-0.1882` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.3642` n `146` status `ready` deltaP `-16.6167` edge `0.1565` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.4911` n `146` status `ready` deltaP `2.0611` edge `-0.0519` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.1996` n `146` status `ready` deltaP `9.8198` edge `0.2016` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.6285` n `146` status `ready` deltaP `2.7017` edge `-0.3222` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
