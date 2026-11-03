# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T13:52:30.722186+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4300`

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

- `news_risk_high->crypto_alt_4h` score `0.2383` n `146` status `ready` deltaP `6.3899` edge `0.2516` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5321` n `146` status `ready` deltaP `1.134` edge `0.047` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6296` n `146` status `ready` deltaP `-1.175` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9323` n `146` status `ready` deltaP `0.8982` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.23` n `146` status `ready` deltaP `-4.0501` edge `-0.0085` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3456` n `146` status `ready` deltaP `-5.1829` edge `-0.0128` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.7949` n `146` status `ready` deltaP `11.777` edge `0.1301` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.9958` n `146` status `ready` deltaP `-1.2271` edge `0.0365` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0144` n `146` status `ready` deltaP `-2.6646` edge `-0.0104` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3254` n `146` status `ready` deltaP `-16.4645` edge `-0.0175` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4786` n `146` status `ready` deltaP `-10.1243` edge `-0.0024` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7023` n `146` status `ready` deltaP `-6.9354` edge `-0.0326` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3074` n `146` status `ready` deltaP `-8.7544` edge `-0.0447` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2833` n `146` status `ready` deltaP `-15.6762` edge `-0.017` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.402` n `146` status `ready` deltaP `-4.2516` edge `-0.018` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.948` n `146` status `ready` deltaP `21.1045` edge `0.7962` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8538` n `146` status `ready` deltaP `-13.6214` edge `-0.0784` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-9.0574` n `146` status `ready` deltaP `16.2434` edge `0.5921` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.1942` n `146` status `ready` deltaP `-0.6828` edge `-0.0922` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.6551` n `146` status `ready` deltaP `-22.1723` edge `-0.0807` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
