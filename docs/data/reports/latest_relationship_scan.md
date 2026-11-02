# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T11:52:36.687324+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `0.6662` n `117` status `ready` deltaP `18.71` edge `0.6394` maxDD `-46.6312`
- `news_risk_high->crypto_alt_4h` score `0.3382` n `139` status `ready` deltaP `6.511` edge `0.2364` maxDD `-12.2489`
- `news_risk_high->fx_1h` score `-0.5105` n `146` status `ready` deltaP `1.0705` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.529` n `146` status `ready` deltaP `1.4334` edge `0.0454` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.7742` n `117` status `ready` deltaP `14.3163` edge `0.1309` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1084` n `146` status `ready` deltaP `-0.8982` edge `-0.0064` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2203` n `139` status `ready` deltaP `-2.9084` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.279` n `146` status `ready` deltaP `-4.9483` edge `-0.0088` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.2062` n `117` status `ready` deltaP `-15.6117` edge `-0.0079` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2273` n `139` status `ready` deltaP `-4.4328` edge `-0.0259` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3613` n `146` status `ready` deltaP `-8.3279` edge `-0.0046` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.9175` n `146` status `ready` deltaP `-7.5342` edge `-0.0562` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9508` n `117` status `ready` deltaP `-10.6972` edge `-0.0228` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.3158` n `146` status `ready` deltaP `-8.6047` edge `-0.0464` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1417` n `139` status `ready` deltaP `-13.6625` edge `-0.0199` maxDD `-9.3996`
- `news_risk_high->metal_4h` score `-4.4856` n `139` status `ready` deltaP `-3.7671` edge `-0.0282` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.6641` n `117` status `ready` deltaP `6.1566` edge `0.2423` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.235` n `139` status `ready` deltaP `-14.4861` edge `-0.1044` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.3601` n `139` status `ready` deltaP `-3.256` edge `-0.214` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.2685` n `117` status `ready` deltaP `-25.6945` edge `-0.1463` maxDD `-27.382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
