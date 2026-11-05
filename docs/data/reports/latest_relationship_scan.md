# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T19:52:37.147190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4232`

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

- `news_risk_high->crypto_alt_4h` score `0.3586` n `146` status `ready` deltaP `8.4475` edge `0.2533` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2851` n `146` status `ready` deltaP `3.5292` edge `0.0627` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6459` n `146` status `ready` deltaP `3.4431` edge `0.0032` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7292` n `146` status `ready` deltaP `-3.1211` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4728` n `146` status `ready` deltaP `-7.8387` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5493` n `146` status `ready` deltaP `-8.5411` edge `-0.0195` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6423` n `146` status `ready` deltaP `1.5221` edge `0.0094` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2096` n `146` status `ready` deltaP `-4.6899` edge `0.0156` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4006` n `146` status `ready` deltaP `-9.8249` edge `0.0021` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4512` n `146` status `ready` deltaP `-18.7792` edge `-0.0182` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.6768` n `146` status `ready` deltaP `-5.1616` edge `-0.0161` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.803` n `146` status `ready` deltaP `-12.2504` edge `0.0065` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7648` n `146` status `ready` deltaP `-13.4704` edge `0.0115` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6685` n `146` status `ready` deltaP `-12.2527` edge `-0.0702` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.774` n `146` status `ready` deltaP `-9.5891` edge `-0.0153` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.444` n `146` status `ready` deltaP `-13.9764` edge `-0.2523` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9627` n `146` status `ready` deltaP `-14.4928` edge `0.1758` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.1722` n `146` status `ready` deltaP `2.5875` edge `0.0545` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.4913` n `146` status `ready` deltaP `9.8989` edge `0.2601` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9753` n `146` status `ready` deltaP `1.9266` edge `-0.3615` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
