# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T23:52:27.398512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.1195` n `146` status `ready` deltaP `7.6094` edge `0.1976` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4722` n `146` status `ready` deltaP `2.7807` edge `0.0437` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7059` n `146` status `ready` deltaP `-2.672` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8352` n `146` status `ready` deltaP `1.9461` edge `-0.0026` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4332` n `146` status `ready` deltaP `-7.0441` edge `-0.0146` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5517` n `146` status `ready` deltaP `-9.1463` edge `-0.0128` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.961` n `146` status `ready` deltaP `-1.2926` edge `-0.0127` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2017` n `146` status `ready` deltaP `-8.1782` edge `0.0077` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4581` n `146` status `ready` deltaP `-18.8368` edge `-0.0187` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4746` n `146` status `ready` deltaP `-8.5296` edge `0.0238` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6103` n `146` status `ready` deltaP `-6.4863` edge `-0.0238` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2236` n `146` status `ready` deltaP `-10.036` edge `0.0337` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2393` n `146` status `ready` deltaP `-6.958` edge `-0.051` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.6325` n `146` status `ready` deltaP `-0.3673` edge `-0.0254` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.0259` n `146` status `ready` deltaP `-6.9955` edge `-0.0517` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.4159` n `146` status `ready` deltaP `-12.097` edge `-0.1354` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-10.7633` n `146` status `ready` deltaP `11.3619` edge `0.2438` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.1968` n `146` status `ready` deltaP `-0.8353` edge `-0.0914` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.4749` n `146` status `ready` deltaP `-20.6807` edge `0.0077` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-12.0307` n `146` status `ready` deltaP `11.8809` edge `0.3686` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
