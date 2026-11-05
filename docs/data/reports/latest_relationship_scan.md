# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T02:37:27.906300+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3809`

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

- `news_risk_high->crypto_alt_4h` score `-0.4331` n `146` status `ready` deltaP `6.5424` edge `0.1645` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6437` n `146` status `ready` deltaP `1.8825` edge `0.0277` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7339` n `146` status `ready` deltaP `-3.1211` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8113` n `146` status `ready` deltaP `2.2455` edge `-0.0026` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5135` n `146` status `ready` deltaP `-8.092` edge `-0.0179` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5714` n `146` status `ready` deltaP `-9.4512` edge `-0.0133` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.909` n `146` status `ready` deltaP `-0.6828` edge `-0.0101` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.137` n `146` status `ready` deltaP `-7.5794` edge `0.0091` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4382` n `146` status `ready` deltaP `-18.6638` edge `-0.0173` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6384` n `146` status `ready` deltaP `-6.4863` edge `-0.0274` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.6488` n `146` status `ready` deltaP `-10.2597` edge `0.013` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1984` n `146` status `ready` deltaP `-10.036` edge `0.0358` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4779` n `146` status `ready` deltaP `-8.0059` edge `-0.0639` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.2414` n `146` status `ready` deltaP `-8.5199` edge `-0.0595` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.2863` n `146` status `ready` deltaP `-2.2705` edge `-0.0672` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.8038` n `146` status `ready` deltaP `-13.3165` edge `-0.1596` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-11.0705` n `146` status `ready` deltaP `-20.3347` edge `0.0391` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-11.0988` n `146` status `ready` deltaP `-0.2255` edge `-0.0873` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-12.3552` n `146` status `ready` deltaP `9.4587` edge `0.0524` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.8318` n `146` status `ready` deltaP `11.3619` edge `0.3053` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
