# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T06:37:29.024616+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3914`

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

- `news_risk_high->crypto_alt_4h` score `-0.5817` n `146` status `ready` deltaP `5.1704` edge `0.1546` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6266` n `146` status `ready` deltaP `1.8825` edge `0.0299` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.7022` n `146` status `ready` deltaP `3.2934` edge `-0.0005` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7417` n `146` status `ready` deltaP `-3.2708` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->metal_1h` score `-1.515` n `146` status `ready` deltaP `-8.092` edge `-0.0181` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.6229` n `146` status `ready` deltaP `-10.3659` edge `-0.0138` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7766` n `146` status `ready` deltaP `0.994` edge `-0.0043` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1394` n `146` status `ready` deltaP `-7.5794` edge `0.0089` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4351` n `146` status `ready` deltaP `-18.6638` edge `-0.0169` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5324` n `146` status `ready` deltaP `-5.7378` edge `-0.0188` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8632` n `146` status `ready` deltaP `-12.1628` edge `-0.0018` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.0945` n `146` status `ready` deltaP `-9.4262` edge `0.0404` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3712` n `146` status `ready` deltaP `-7.4071` edge `-0.059` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4884` n `146` status `ready` deltaP `-10.1967` edge `-0.0689` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.2482` n `146` status `ready` deltaP `-5.0386` edge `-0.1289` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6937` n `146` status `ready` deltaP `-12.5543` edge `-0.1555` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.4686` n `146` status `ready` deltaP `-20.1616` edge `0.0881` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8447` n `146` status `ready` deltaP `0.5367` edge `-0.0712` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.7502` n `146` status `ready` deltaP `9.9778` edge `0.238` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.074` n `146` status `ready` deltaP `6.6906` edge `-0.1495` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
