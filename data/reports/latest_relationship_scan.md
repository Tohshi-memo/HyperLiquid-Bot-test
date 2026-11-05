# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T14:07:33.665083+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3783`

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

- `news_risk_high->crypto_alt_4h` score `0.2328` n `146` status `ready` deltaP `8.2192` edge `0.2387` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4255` n `146` status `ready` deltaP `3.5292` edge `0.0447` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7066` n `146` status `ready` deltaP `-2.672` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7669` n `146` status `ready` deltaP `2.5449` edge `-0.0009` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4458` n `146` status `ready` deltaP `-7.4695` edge `-0.0104` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.589` n `146` status `ready` deltaP `-9.1399` edge `-0.0206` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7513` n `146` status `ready` deltaP `1.4513` edge `-0.0041` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2268` n `146` status `ready` deltaP `-15.4229` edge `-0.0118` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3599` n `146` status `ready` deltaP `-9.3758` edge `0.0025` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.428` n `146` status `ready` deltaP `-4.6899` edge `-0.0124` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9464` n `146` status `ready` deltaP `-12.3382` edge `-0.0113` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-2.9971` n `146` status `ready` deltaP `-5.461` edge `-0.0408` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6883` n `146` status `ready` deltaP `-13.0847` edge `0.0153` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7071` n `146` status `ready` deltaP `-12.3309` edge `-0.0729` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.4197` n `146` status `ready` deltaP `-10.1153` edge `-0.0656` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.5013` n `146` status `ready` deltaP `-10.098` edge `-0.1996` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.1947` n `146` status `ready` deltaP `-15.9223` edge `0.166` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.3343` n `146` status `ready` deltaP `2.6708` edge `-0.0429` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.3352` n `146` status `ready` deltaP `9.8198` edge `0.1903` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9173` n `146` status `ready` deltaP `2.0073` edge `-0.3546` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
