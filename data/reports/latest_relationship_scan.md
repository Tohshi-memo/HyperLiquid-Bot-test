# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T05:22:28.239915+00:00`
- Price records: `672`
- Market context records: `8271`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7118.8358` n `47` status `ready` deltaP `39.0625` edge `592.9759` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2779` n `54` status `ready` deltaP `26.3832` edge `0.4903` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1853` n `54` status `ready` deltaP `22.2777` edge `0.1478` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7595` n `54` status `ready` deltaP `22.8771` edge `0.0965` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1481` n `54` status `ready` deltaP `10.6313` edge `0.2739` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9083` n `54` status `ready` deltaP `14.8536` edge `0.1034` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6378` n `54` status `ready` deltaP `10.7563` edge `0.1045` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4401` n `54` status `ready` deltaP `16.6215` edge `0.213` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0938` n `54` status `ready` deltaP `9.8916` edge `0.072` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5226` n `54` status `ready` deltaP `7.352` edge `0.0234` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2366` n `54` status `ready` deltaP `8.1947` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0604` n `54` status `ready` deltaP `3.4043` edge `0.0126` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4112` n `54` status `ready` deltaP `5.3748` edge `0.0072` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1671` n `54` status `ready` deltaP `-8.9599` edge `-0.0423` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.4574` n `47` status `ready` deltaP `-19.4408` edge `-0.0468` maxDD `-4.6039`
- `news_risk_high->metal_24h` score `-5.9079` n `47` status `ready` deltaP `-21.3874` edge `-0.0751` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.9592` n `54` status `ready` deltaP `-32.1816` edge `-0.2013` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.0662` n `47` status `ready` deltaP `-25.2992` edge `-0.3385` maxDD `-26.2018`
- `news_risk_high->commodity_24h` score `-12.7251` n `47` status `ready` deltaP `-13.9295` edge `-0.3821` maxDD `-33.1706`
- `news_risk_high->equity_24h` score `-35.4804` n `47` status `ready` deltaP `-24.4311` edge `-1.1709` maxDD `-116.1673`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
