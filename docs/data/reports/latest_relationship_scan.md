# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T22:36:27.454180+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.3873` n `146` status `ready` deltaP `8.2192` edge `0.2585` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4441` n `146` status `ready` deltaP `2.0322` edge `0.0523` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7284` n `146` status `ready` deltaP `-2.9714` edge `-0.0035` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9011` n `146` status `ready` deltaP `1.1976` edge `-0.0031` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.117` n `146` status `ready` deltaP `-2.2537` edge `-0.006` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.458` n `146` status `ready` deltaP `12.2979` edge `0.1547` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.504` n `146` status `ready` deltaP `-8.0793` edge `-0.0138` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7363` n `146` status `ready` deltaP `1.7243` edge `0.0501` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9709` n `146` status `ready` deltaP `-1.9024` edge `-0.0099` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2427` n `146` status `ready` deltaP `-16.4645` edge `-0.0069` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.6583` n `146` status `ready` deltaP `-12.0704` edge `-0.0044` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7623` n `146` status `ready` deltaP `-7.5342` edge `-0.0363` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1851` n `146` status `ready` deltaP `-7.8562` edge `-0.0405` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1187` n `146` status `ready` deltaP `-14.6091` edge `-0.0104` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2072` n `146` status `ready` deltaP `-2.1174` edge `-0.016` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9509` n `146` status `ready` deltaP `21.7989` edge `0.7912` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.7417` n `146` status `ready` deltaP `-12.2495` edge `-0.0782` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.1362` n `146` status `ready` deltaP `18.8476` edge `0.6467` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4752` n `146` status `ready` deltaP `-1.7499` edge `-0.1085` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2285` n `146` status `ready` deltaP `-19.9153` edge `-0.0602` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
