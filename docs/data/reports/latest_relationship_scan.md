# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T20:38:19.385078+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4492`

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

- `news_risk_high->crypto_alt_4h` score `0.3449` n `146` status `ready` deltaP `7.9143` edge `0.2551` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4215` n `146` status `ready` deltaP `2.1819` edge `0.0542` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7207` n `146` status `ready` deltaP `-2.8217` edge `-0.0035` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8819` n `146` status `ready` deltaP `1.3473` edge `-0.0025` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1155` n `146` status `ready` deltaP `-2.2537` edge `-0.0058` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.5192` n `146` status `ready` deltaP `12.2979` edge `0.1496` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.5356` n `146` status `ready` deltaP `-8.5366` edge `-0.0148` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7277` n `146` status `ready` deltaP `1.7243` edge `0.0512` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9961` n `146` status `ready` deltaP `-2.2072` edge `-0.0111` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2615` n `146` status `ready` deltaP `-16.4645` edge `-0.0093` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.6152` n `146` status `ready` deltaP `-11.6213` edge `-0.0038` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7015` n `146` status `ready` deltaP `-7.2348` edge `-0.0305` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1743` n `146` status `ready` deltaP `-7.8562` edge `-0.0396` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1091` n `146` status `ready` deltaP `-14.6091` edge `-0.0096` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2182` n `146` status `ready` deltaP `-2.2699` edge `-0.0159` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9275` n `146` status `ready` deltaP `21.7989` edge `0.7942` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8446` n `146` status `ready` deltaP `-13.0116` edge `-0.0817` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-7.8998` n `146` status `ready` deltaP `18.8476` edge `0.6664` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.492` n `146` status `ready` deltaP `-1.7499` edge `-0.1099` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.1829` n `146` status `ready` deltaP `-19.9153` edge `-0.0564` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
