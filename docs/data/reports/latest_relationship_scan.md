# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T02:52:25.144680+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `49.4357` n `50` status `ready` deltaP `11.5717` edge `4.0425` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.4972` n `50` status `ready` deltaP `36.9326` edge `1.006` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2547` n `50` status `ready` deltaP `25.4024` edge `0.8618` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `6.1676` n `50` status `ready` deltaP `29.0777` edge `0.4134` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8409` n `50` status `ready` deltaP `44.8963` edge `0.0298` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.5011` n `50` status `ready` deltaP `35.8411` edge `0.068` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.0973` n `137` status `ready` deltaP `24.1031` edge `0.1381` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `2.8921` n `50` status `ready` deltaP `37.5509` edge `-0.0051` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.6988` n `50` status `ready` deltaP `15.7784` edge `0.1553` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4318` n `50` status `ready` deltaP `19.3054` edge `0.0076` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3308` n `137` status `ready` deltaP `13.1507` edge `0.0682` maxDD `-1.5974`
- `news_risk_high->equity_1h` score `1.2803` n `50` status `ready` deltaP `16.9641` edge `0.0215` maxDD `-0.2319`
- `news_risk_high->equity_4h` score `1.2689` n `50` status `ready` deltaP `19.75` edge `0.0506` maxDD `-2.1218`
- `market_context_high->unknown_24h` score `0.761` n `134` status `ready` deltaP `5.6016` edge `0.0992` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5347` n `50` status `ready` deltaP `14.5988` edge `0.0025` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1478` n `50` status `ready` deltaP `7.2378` edge `0.0038` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1264` n `50` status `ready` deltaP `7.2096` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0174` n `50` status `ready` deltaP `4.2036` edge `-0.0032` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.3098` n `50` status `ready` deltaP `5.939` edge `-0.0123` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3484` n `137` status `ready` deltaP `4.2397` edge `0.0003` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
