# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T05:52:27.977006+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4314`

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

- `news_risk_high->crypto_alt_4h` score `-0.151` n `146` status `ready` deltaP `7.1521` edge `0.1966` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4614` n `146` status `ready` deltaP `3.8286` edge `0.0381` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6746` n `146` status `ready` deltaP `3.2934` edge `0.0018` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7378` n `146` status `ready` deltaP `-3.2708` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4741` n `146` status `ready` deltaP `-7.7744` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.4963` n `146` status `ready` deltaP `-7.6429` edge `-0.0187` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7169` n `146` status `ready` deltaP `0.5367` edge `0.0064` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.3609` n `146` status `ready` deltaP `-12.1628` edge `0.0626` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.3624` n `146` status `ready` deltaP `-5.4384` edge `0.001` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.5133` n `146` status `ready` deltaP `-11.0225` edge `0.0007` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.6817` n `146` status `ready` deltaP `-4.2634` edge `-0.0225` maxDD `-9.4709`
- `news_risk_high->fx_24h` score `-2.8897` n `146` status `ready` deltaP `-25.4112` edge `-0.0302` maxDD `-2.336`
- `news_risk_high->commodity_4h` score `-4.0073` n `146` status `ready` deltaP `-15.6762` edge `0.006` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.716` n `146` status `ready` deltaP `-8.7434` edge `-0.0161` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.7511` n `146` status `ready` deltaP `-12.9406` edge `-0.0725` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-9.1868` n `146` status `ready` deltaP `-16.9763` edge `-0.2942` maxDD `-16.6552`
- `news_risk_high->equity_24h` score `-9.8394` n `146` status `ready` deltaP `9.9778` edge `0.5639` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-9.8779` n `146` status `ready` deltaP `1.1464` edge `0.0053` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-10.0742` n `146` status `ready` deltaP `-16.7014` edge `0.0979` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.3302` n `146` status `ready` deltaP `7.2096` edge `0.0706` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
