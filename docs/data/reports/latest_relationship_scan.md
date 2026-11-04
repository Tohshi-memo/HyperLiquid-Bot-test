# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T16:22:33.136917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4030`

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

- `news_risk_high->crypto_alt_4h` score `0.007` n `146` status `ready` deltaP `7.7619` edge `0.2128` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6063` n `146` status `ready` deltaP `1.8825` edge `0.0325` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6327` n `146` status `ready` deltaP `-1.3247` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8256` n `146` status `ready` deltaP `1.9461` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3795` n `146` status `ready` deltaP `-6.1459` edge `-0.0137` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4251` n `146` status `ready` deltaP `-7.0122` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8095` n `146` status `ready` deltaP `0.8415` edge `-0.0075` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.0737` n `146` status `ready` deltaP `-3.3393` edge `0.0406` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.191` n `146` status `ready` deltaP `-7.5794` edge `0.0046` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4413` n `146` status `ready` deltaP `-18.6638` edge `-0.0177` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5791` n `146` status `ready` deltaP `-6.1869` edge `-0.0218` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-3.1084` n `146` status `ready` deltaP `4.823` edge `0.067` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.4551` n `146` status `ready` deltaP `-8.3053` edge `-0.06` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4672` n `146` status `ready` deltaP `-10.036` edge `0.0134` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8223` n `146` status `ready` deltaP `-5.4711` edge `-0.0449` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0521` n `146` status `ready` deltaP `-11.9446` edge `-0.1061` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.9875` n `146` status `ready` deltaP `14.8221` edge `0.4484` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9905` n `146` status `ready` deltaP `0.0793` edge `-0.0803` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4259` n `146` status `ready` deltaP `11.8809` edge `0.419` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.3005` n `146` status `ready` deltaP `-20.6807` edge `-0.0611` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
