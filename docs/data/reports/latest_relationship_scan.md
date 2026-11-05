# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T02:52:28.224262+00:00`
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
- `news_risk_high->crypto_alt_1h` score `-0.6609` n `146` status `ready` deltaP `1.7328` edge `0.0265` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7339` n `146` status `ready` deltaP `-3.1211` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8245` n `146` status `ready` deltaP `2.0958` edge `-0.0027` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5236` n `146` status `ready` deltaP `-8.2417` edge `-0.0182` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5802` n `146` status `ready` deltaP `-9.6037` edge `-0.0134` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8964` n `146` status `ready` deltaP `-0.5304` edge `-0.0095` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.137` n `146` status `ready` deltaP `-7.5794` edge `0.0091` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4374` n `146` status `ready` deltaP `-18.6638` edge `-0.0172` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6493` n `146` status `ready` deltaP `-6.636` edge `-0.0278` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.6687` n `146` status `ready` deltaP `-10.4327` edge `0.0116` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1936` n `146` status `ready` deltaP `-10.036` edge `0.0362` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4791` n `146` status `ready` deltaP `-8.0059` edge `-0.064` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.2668` n `146` status `ready` deltaP `-8.6723` edge `-0.0606` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.3554` n `146` status `ready` deltaP `-2.4435` edge `-0.0718` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.7832` n `146` status `ready` deltaP `-13.1641` edge `-0.1589` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-11.0218` n `146` status `ready` deltaP `-20.1616` edge `0.042` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-11.0627` n `146` status `ready` deltaP `-0.0731` edge `-0.0853` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-12.4937` n `146` status `ready` deltaP `9.2857` edge `0.0358` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.9285` n `146` status `ready` deltaP `11.1888` edge `0.2984` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
