# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T18:52:30.871956+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.036` n `146` status `ready` deltaP `7.9143` edge `0.2155` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4808` n `146` status `ready` deltaP `2.7807` edge `0.0426` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6171` n `146` status `ready` deltaP `-1.0253` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.828` n `146` status `ready` deltaP `1.9461` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4099` n `146` status `ready` deltaP `-6.595` edge `-0.0146` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4204` n `146` status `ready` deltaP `-7.0122` edge `-0.0102` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8719` n `146` status `ready` deltaP `-0.0731` edge `-0.0094` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1933` n `146` status `ready` deltaP `-8.1782` edge `0.0084` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.2011` n `146` status `ready` deltaP `-5.0694` edge `0.0358` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.446` n `146` status `ready` deltaP `-18.6638` edge `-0.0183` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5674` n `146` status `ready` deltaP `-6.3366` edge `-0.0193` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.292` n `146` status `ready` deltaP `-7.4071` edge `-0.0524` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.3124` n `146` status `ready` deltaP `-10.036` edge `0.0263` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-3.5888` n `146` status `ready` deltaP `3.0929` edge `0.0385` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.8451` n `146` status `ready` deltaP `-5.4711` edge `-0.0468` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2705` n `146` status `ready` deltaP `-11.9446` edge `-0.1243` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.1217` n `146` status `ready` deltaP `14.8221` edge `0.4312` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9015` n `146` status `ready` deltaP `0.2318` edge `-0.0739` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4235` n `146` status `ready` deltaP `11.8809` edge `0.4192` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.1061` n `146` status `ready` deltaP `-20.6807` edge `-0.0449` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
