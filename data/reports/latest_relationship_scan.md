# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T15:37:33.654596+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4094`

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

- `news_risk_high->crypto_alt_4h` score `0.443` n `146` status `ready` deltaP `8.6765` edge `0.2626` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.1838` n `146` status `ready` deltaP `4.4274` edge `0.0697` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6615` n `146` status `ready` deltaP `3.4431` edge `0.0019` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6973` n `146` status `ready` deltaP `-2.5223` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4442` n `146` status `ready` deltaP `-7.4695` edge `-0.0102` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5734` n `146` status `ready` deltaP `-8.9902` edge `-0.0196` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7192` n `146` status `ready` deltaP `1.6037` edge `-0.001` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.1652` n `146` status `ready` deltaP `-3.7917` edge `0.0153` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.2593` n `146` status `ready` deltaP `-15.9437` edge `-0.0125` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4222` n `146` status `ready` deltaP `-9.9746` edge `0.0013` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.6457` n `146` status `ready` deltaP `-4.5628` edge `-0.0175` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.9261` n `146` status `ready` deltaP `-12.3382` edge `-0.0087` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.6979` n `146` status `ready` deltaP `-13.0847` edge `0.0145` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7533` n `146` status `ready` deltaP `-12.7882` edge `-0.0737` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0434` n `146` status `ready` deltaP `-9.5056` edge `-0.0383` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.7802` n `146` status `ready` deltaP `-11.1396` edge `-0.2159` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9589` n `146` status `ready` deltaP `-14.8806` edge `0.1787` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.9467` n `146` status `ready` deltaP `2.6708` edge `-0.0106` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.1888` n `146` status `ready` deltaP `9.8198` edge `0.2025` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-16.0722` n `146` status `ready` deltaP `1.8337` edge `-0.3733` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
