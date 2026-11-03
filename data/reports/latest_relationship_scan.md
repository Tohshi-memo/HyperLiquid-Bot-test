# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T22:23:36.219453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4454`

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

- `news_risk_high->crypto_alt_4h` score `0.3818` n `146` status `ready` deltaP `8.2192` edge `0.2578` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4565` n `146` status `ready` deltaP `1.8825` edge `0.0517` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7284` n `146` status `ready` deltaP `-2.9714` edge `-0.0035` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9143` n `146` status `ready` deltaP `1.0479` edge `-0.0032` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1093` n `146` status `ready` deltaP `-2.104` edge `-0.006` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.464` n `146` status `ready` deltaP `12.2979` edge `0.1542` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.5143` n `146` status `ready` deltaP `-8.2317` edge `-0.0141` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7339` n `146` status `ready` deltaP `1.7243` edge `0.0504` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9725` n `146` status `ready` deltaP `-1.9024` edge `-0.0101` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2451` n `146` status `ready` deltaP `-16.4645` edge `-0.0072` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.6703` n `146` status `ready` deltaP `-12.2201` edge `-0.0044` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7631` n `146` status `ready` deltaP `-7.5342` edge `-0.0364` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2055` n `146` status `ready` deltaP `-8.0059` edge `-0.0412` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1187` n `146` status `ready` deltaP `-14.6091` edge `-0.0104` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2048` n `146` status `ready` deltaP `-2.1174` edge `-0.0158` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9462` n `146` status `ready` deltaP `21.7989` edge `0.7918` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.7647` n `146` status `ready` deltaP `-12.4019` edge `-0.0791` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.0918` n `146` status `ready` deltaP `18.8476` edge `0.6504` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.474` n `146` status `ready` deltaP `-1.7499` edge `-0.1084` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2237` n `146` status `ready` deltaP `-19.9153` edge `-0.0598` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
