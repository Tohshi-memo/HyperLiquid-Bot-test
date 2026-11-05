# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T20:22:31.312182+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4252`

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

- `news_risk_high->crypto_alt_4h` score `0.2078` n `146` status `ready` deltaP `8.1431` edge `0.236` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3514` n `146` status `ready` deltaP `3.2298` edge `0.0562` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6626` n `146` status `ready` deltaP `3.2934` edge `0.0028` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7292` n `146` status `ready` deltaP `-3.1211` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4728` n `146` status `ready` deltaP `-7.8387` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5407` n `146` status `ready` deltaP `-8.3914` edge `-0.0194` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6439` n `146` status `ready` deltaP `1.5221` edge `0.0092` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.261` n `146` status `ready` deltaP `-4.9893` edge `0.011` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4018` n `146` status `ready` deltaP `-9.8249` edge `0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4739` n `146` status `ready` deltaP `-19.1259` edge `-0.0188` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.7583` n `146` status `ready` deltaP `-5.461` edge `-0.0209` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.7898` n `146` status `ready` deltaP `-12.2504` edge `0.0082` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7672` n `146` status `ready` deltaP `-13.4704` edge `0.0113` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6818` n `146` status `ready` deltaP `-12.4049` edge `-0.0703` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.8676` n `146` status `ready` deltaP `-9.5891` edge `-0.0231` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.5233` n `146` status `ready` deltaP `-14.323` edge `-0.2566` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9795` n `146` status `ready` deltaP `-14.4928` edge `0.1744` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.2804` n `146` status `ready` deltaP `2.4353` edge `0.0465` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.4253` n `146` status `ready` deltaP `9.8989` edge `0.2656` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9987` n `146` status `ready` deltaP `1.9266` edge `-0.3645` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
