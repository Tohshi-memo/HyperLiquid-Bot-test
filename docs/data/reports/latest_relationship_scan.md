# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T23:07:26.323898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7638`

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

- `news_risk_high->unknown_24h` score `720.3564` n `136` status `ready` deltaP `1.2153` edge `60.0216` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.5138` n `136` status `ready` deltaP `14.6446` edge `0.4237` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.4607` n `136` status `ready` deltaP `18.3824` edge `0.0687` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9143` n `136` status `ready` deltaP `20.2921` edge `0.1264` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.0571` n `139` status `ready` deltaP `16.198` edge `0.0577` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0252` n `139` status `ready` deltaP `3.3624` edge `0.0045` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0497` n `139` status `ready` deltaP `4.4727` edge `0.0571` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.185` n `139` status `ready` deltaP `3.3624` edge `0.0283` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7113` n `139` status `ready` deltaP `-0.1562` edge `0.0047` maxDD `-0.7016`
- `news_risk_high->equity_24h` score `-0.7998` n `136` status `ready` deltaP `12.4183` edge `0.1062` maxDD `-11.1179`
- `news_risk_high->fx_4h` score `-1.0365` n `139` status `ready` deltaP `13.0308` edge `0.0016` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0869` n `139` status `ready` deltaP `-7.4711` edge `-0.0015` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.0891` n `139` status `ready` deltaP `-3.4453` edge `0.0116` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.1368` n `139` status `ready` deltaP `-2.6408` edge `0.0082` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.7477` n `139` status `ready` deltaP `1.6384` edge `0.1094` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8639` n `139` status `ready` deltaP `-13.7293` edge `0.002` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.8971` n `139` status `ready` deltaP `-9.9201` edge `-0.0096` maxDD `-3.3986`
- `news_risk_high->crypto_major_24h` score `-2.3874` n `136` status `ready` deltaP `9.1197` edge `0.1837` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.4592` n `139` status `ready` deltaP `-12.2555` edge `-0.0903` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.655` n `139` status `ready` deltaP `-9.7978` edge `0.0026` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
