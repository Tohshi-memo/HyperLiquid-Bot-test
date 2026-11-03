# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T23:37:26.476465+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.3927` n `146` status `ready` deltaP `8.2192` edge `0.2592` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4464` n `146` status `ready` deltaP `2.0322` edge `0.052` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7113` n `146` status `ready` deltaP `-2.672` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9131` n `146` status `ready` deltaP `1.0479` edge `-0.0031` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1412` n `146` status `ready` deltaP `-2.7028` edge `-0.0061` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.4304` n `146` status `ready` deltaP `12.2979` edge `0.157` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4732` n `146` status `ready` deltaP `-7.622` edge `-0.0129` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7417` n `146` status `ready` deltaP `1.7243` edge `0.0494` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9686` n `146` status `ready` deltaP `-1.9024` edge `-0.0096` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2342` n `146` status `ready` deltaP `-16.4645` edge `-0.0058` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.602` n `146` status `ready` deltaP `-11.4716` edge `-0.0037` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.749` n `146` status `ready` deltaP `-7.3845` edge `-0.0356` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2007` n `146` status `ready` deltaP `-8.0059` edge `-0.0408` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1163` n `146` status `ready` deltaP `-14.6091` edge `-0.0102` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2558` n `146` status `ready` deltaP `-2.5748` edge `-0.017` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9907` n `146` status `ready` deltaP `21.7989` edge `0.7861` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.7333` n `146` status `ready` deltaP `-12.2495` edge `-0.0775` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.2646` n `146` status `ready` deltaP `18.8476` edge `0.636` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4764` n `146` status `ready` deltaP `-1.7499` edge `-0.1086` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2441` n `146` status `ready` deltaP `-19.9153` edge `-0.0615` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
