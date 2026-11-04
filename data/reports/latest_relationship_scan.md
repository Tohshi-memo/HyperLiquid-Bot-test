# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T13:22:28.782283+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `-0.0158` n `146` status `ready` deltaP `7.3073` edge `0.2129` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4924` n `146` status `ready` deltaP `2.0322` edge `0.0461` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.709` n `146` status `ready` deltaP `-2.672` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8256` n `146` status `ready` deltaP `1.9461` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3234` n `146` status `ready` deltaP `-5.2477` edge `-0.0125` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4705` n `146` status `ready` deltaP `-7.7508` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8754` n `146` status `ready` deltaP `-0.2311` edge `-0.0088` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-1.9451` n `146` status `ready` deltaP `-1.4362` edge `0.0444` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3228` n `146` status `ready` deltaP `-8.6273` edge `0.0006` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3835` n `146` status `ready` deltaP `-17.9718` edge `-0.0149` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6127` n `146` status `ready` deltaP `-6.1869` edge `-0.0261` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.6232` n `146` status `ready` deltaP `6.8991` edge `0.0936` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.2103` n `146` status `ready` deltaP `-8.0059` edge `-0.0416` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.5821` n `146` status `ready` deltaP `-10.5113` edge `0.007` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8225` n `146` status `ready` deltaP `-5.4878` edge `-0.0448` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0207` n `146` status `ready` deltaP `-12.4079` edge `-0.1004` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.698` n `146` status `ready` deltaP `15.5141` edge `0.4809` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-11.2642` n `146` status `ready` deltaP `13.092` edge `0.4244` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.505` n `146` status `ready` deltaP `-1.4469` edge `-0.113` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2069` n `146` status `ready` deltaP `-20.6807` edge `-0.0533` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
