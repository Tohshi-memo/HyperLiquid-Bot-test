# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T02:37:29.395721+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4836`

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

- `news_risk_high->crypto_alt_24h` score `0.1474` n `126` status `ready` deltaP `22.0982` edge `0.8221` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.0102` n `146` status `ready` deltaP `4.1033` edge `0.2376` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4963` n `146` status `ready` deltaP `1.2837` edge `0.0506` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5626` n `146` status `ready` deltaP `0.0226` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8609` n `126` status `ready` deltaP `12.5744` edge `0.1314` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.973` n `146` status `ready` deltaP `0.4491` edge `-0.0041` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2293` n `146` status `ready` deltaP `-3.2012` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3242` n `146` status `ready` deltaP `-5.5471` edge `-0.0106` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.131` n `146` status `ready` deltaP `-4.0365` edge `-0.0162` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1619` n `126` status `ready` deltaP `-2.9514` edge `0.0267` maxDD `-7.402`
- `news_risk_high->equity_24h` score `-2.2026` n `126` status `ready` deltaP `17.2371` edge `0.6122` maxDD `-67.0937`
- `news_risk_high->commodity_1h` score `-2.3349` n `146` status `ready` deltaP `-8.4776` edge `-0.0014` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5441` n `126` status `ready` deltaP `-20.6102` edge `-0.0179` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7031` n `146` status `ready` deltaP `-6.9354` edge `-0.0327` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2379` n `146` status `ready` deltaP `-8.1556` edge `-0.0429` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8132` n `146` status `ready` deltaP `-12.1701` edge `-0.0012` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9117` n `146` status `ready` deltaP `-7.7577` edge `-0.0371` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1458` n `146` status `ready` deltaP `-14.8409` edge `-0.0946` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.9389` n `126` status `ready` deltaP `-13.8889` edge `0.0287` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.3208` n `126` status `ready` deltaP `-25.4464` edge `-0.0849` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
