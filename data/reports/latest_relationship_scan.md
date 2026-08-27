# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T04:07:27.983363+00:00`
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

- `news_risk_high->unknown_24h` score `49.6649` n `50` status `ready` deltaP `11.5717` edge `4.0616` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.0396` n `50` status `ready` deltaP `36.9326` edge `1.0512` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2669` n `50` status `ready` deltaP `25.5549` edge `0.8618` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `5.9389` n `50` status `ready` deltaP `28.2142` edge `0.4001` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8823` n `50` status `ready` deltaP `45.3537` edge `0.0302` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.4068` n `50` status `ready` deltaP `34.9775` edge `0.0659` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1095` n `137` status `ready` deltaP `24.2556` edge `0.1381` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `3.038` n `50` status `ready` deltaP `38.4145` edge `0.0013` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.664` n `50` status `ready` deltaP `15.479` edge `0.1544` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4438` n `50` status `ready` deltaP `19.4551` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.3671` n `50` status `ready` deltaP `20.5122` edge `0.0537` maxDD `-2.1218`
- `market_context_high->unknown_1h` score `1.2961` n `137` status `ready` deltaP `12.8513` edge `0.0673` maxDD `-1.5974`
- `news_risk_high->equity_1h` score `1.2779` n `50` status `ready` deltaP `16.9641` edge `0.0213` maxDD `-0.2319`
- `market_context_high->unknown_24h` score `0.8245` n `135` status `ready` deltaP `5.6458` edge `0.1042` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2208` n `50` status `ready` deltaP `8.0` edge `0.0048` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1349` n `50` status `ready` deltaP `7.3593` edge `0.0022` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0516` n `50` status `ready` deltaP `4.8024` edge `-0.0028` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.3406` n `137` status `ready` deltaP `4.3894` edge `0.0003` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.3572` n `50` status `ready` deltaP `5.4817` edge `-0.0132` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
