# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T10:52:34.045296+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3500`

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

- `news_risk_high->crypto_alt_4h` score `-0.2576` n `146` status `ready` deltaP `6.5424` edge `0.187` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5557` n `146` status `ready` deltaP `2.631` edge `0.034` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6903` n `146` status `ready` deltaP `-2.3726` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7537` n `146` status `ready` deltaP `2.6946` edge `-0.0008` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4892` n `146` status `ready` deltaP `-8.0793` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5446` n `146` status `ready` deltaP `-8.5411` edge `-0.0189` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7695` n `146` status `ready` deltaP `1.1464` edge `-0.0044` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2485` n `146` status `ready` deltaP `-8.4776` edge `0.0058` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3417` n `146` status `ready` deltaP `-17.3928` edge `-0.0134` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5589` n `146` status `ready` deltaP `-5.8875` edge `-0.0212` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9099` n `146` status `ready` deltaP `-12.2504` edge `-0.0072` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.2885` n `146` status `ready` deltaP `-7.1077` edge `-0.0541` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4478` n `146` status `ready` deltaP `-11.7128` edge `0.0262` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.5626` n `146` status `ready` deltaP `-10.9589` edge `-0.07` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.9411` n `146` status `ready` deltaP `-7.9105` edge `-0.1675` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.1537` n `146` status `ready` deltaP `-11.6397` edge `-0.1166` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-9.7255` n `146` status `ready` deltaP `-18.1323` edge `0.1365` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7503` n `146` status `ready` deltaP `1.1464` edge `-0.0674` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.9509` n `146` status `ready` deltaP `9.8989` edge `0.2218` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.1204` n `146` status `ready` deltaP `3.8331` edge `-0.2646` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
