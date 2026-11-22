# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T08:52:37.045102+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4522`

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

- `market_context_high->unknown_1h` score `11798.1006` n `108` status `ready` deltaP `0.4158` edge `983.1921` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7352.5898` n `108` status `ready` deltaP `-1.9422` edge `612.7593` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2622` n `108` status `ready` deltaP `3.4154` edge `0.0101` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3212` n `108` status `ready` deltaP `2.8998` edge `0.0026` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1734` n `108` status `ready` deltaP `-7.9951` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->crypto_major_1h` score `-1.5232` n `108` status `ready` deltaP `3.676` edge `-0.0088` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.5564` n `108` status `ready` deltaP `-0.7452` edge `0.0033` maxDD `-1.4967`
- `market_context_high->equity_1h` score `-1.7886` n `108` status `ready` deltaP `7.1745` edge `0.0007` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-1.9548` n `108` status `ready` deltaP `2.6423` edge `0.0001` maxDD `-10.1161`
- `market_context_high->crypto_alt_1h` score `-2.1975` n `108` status `ready` deltaP `-4.4799` edge `-0.0408` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.5245` n `108` status `ready` deltaP `-10.8672` edge `-0.0262` maxDD `-4.2715`
- `market_context_high->index_4h` score `-3.3057` n `108` status `ready` deltaP `-12.387` edge `-0.0296` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-4.9756` n `108` status `ready` deltaP `-7.9283` edge `-0.0027` maxDD `-6.0598`
- `market_context_high->commodity_4h` score `-6.7602` n `108` status `ready` deltaP `-17.2482` edge `-0.0883` maxDD `-14.8047`
- `market_context_high->metal_24h` score `-10.0153` n `108` status `ready` deltaP `-7.6967` edge `0.0263` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-10.7288` n `108` status `ready` deltaP `-7.7801` edge `-0.1493` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-11.0292` n `108` status `ready` deltaP `-8.3898` edge `-0.1819` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.7732` n `108` status `ready` deltaP `-27.4884` edge `-0.3507` maxDD `-62.9569`
- `market_context_high->crypto_major_24h` score `-15.3377` n `108` status `ready` deltaP `7.9861` edge `0.0404` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.8949` n `108` status `ready` deltaP `-31.4814` edge `-0.1751` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
