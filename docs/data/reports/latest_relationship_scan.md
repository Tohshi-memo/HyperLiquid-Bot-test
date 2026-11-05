# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T19:37:36.271917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4234`

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

- `news_risk_high->crypto_alt_4h` score `0.4531` n `146` status `ready` deltaP `8.5997` edge `0.2644` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2516` n `146` status `ready` deltaP `3.6789` edge `0.066` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6291` n `146` status `ready` deltaP `3.5928` edge `0.0036` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7292` n `146` status `ready` deltaP `-3.1211` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4815` n `146` status `ready` deltaP `-7.9909` edge `-0.0115` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5485` n `146` status `ready` deltaP `-8.5411` edge `-0.0194` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6305` n `146` status `ready` deltaP `1.6743` edge `0.0099` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.1659` n `146` status `ready` deltaP `-4.5402` edge `0.0202` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.3994` n `146` status `ready` deltaP `-9.8249` edge `0.0022` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4399` n `146` status `ready` deltaP `-18.6059` edge `-0.0179` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.6372` n `146` status `ready` deltaP `-5.0119` edge `-0.0138` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.8085` n `146` status `ready` deltaP `-12.2504` edge `0.0058` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7612` n `146` status `ready` deltaP `-13.4704` edge `0.0118` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6515` n `146` status `ready` deltaP `-12.1005` edge `-0.0698` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.6899` n `146` status `ready` deltaP `-9.4369` edge `-0.0093` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.4001` n `146` status `ready` deltaP `-13.8031` edge `-0.2498` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9555` n `146` status `ready` deltaP `-14.4928` edge `0.1764` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.0628` n `146` status `ready` deltaP `2.7397` edge `0.0626` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.5021` n `146` status `ready` deltaP `9.8989` edge `0.2592` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.955` n `146` status `ready` deltaP `1.9266` edge `-0.3589` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
