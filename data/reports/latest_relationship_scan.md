# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T01:22:23.780292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `49.1309` n `50` status `ready` deltaP `11.5717` edge `4.0171` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.9415` n `50` status `ready` deltaP `36.5872` edge `0.962` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2753` n `50` status `ready` deltaP `25.5549` edge `0.8625` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `6.5879` n `50` status `ready` deltaP `30.114` edge `0.442` maxDD `-4.8351`
- `news_risk_high->fx_4h` score `3.757` n `50` status `ready` deltaP `43.9817` edge `0.0289` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.6368` n `50` status `ready` deltaP `36.8774` edge `0.0724` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.13` n `137` status `ready` deltaP `24.2556` edge `0.1398` maxDD `-0.5871`
- `news_risk_high->metal_24h` score `2.7324` n `50` status `ready` deltaP `36.5147` edge `-0.0115` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.7002` n `50` status `ready` deltaP `15.479` edge `0.1574` maxDD `-0.8463`
- `news_risk_high->fx_1h` score `1.4438` n `50` status `ready` deltaP `19.4551` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3735` n `50` status `ready` deltaP `17.7126` edge `0.0243` maxDD `-0.2338`
- `market_context_high->unknown_1h` score `1.3336` n `137` status `ready` deltaP `12.8513` edge `0.0704` maxDD `-1.5954`
- `news_risk_high->equity_4h` score `1.2288` n `50` status `ready` deltaP `19.4451` edge `0.0495` maxDD `-2.1389`
- `market_context_high->unknown_24h` score `0.6464` n `133` status `ready` deltaP `5.5567` edge `0.0899` maxDD `-3.1794`
- `news_risk_high->commodity_1h` score `0.5339` n `50` status `ready` deltaP `14.5988` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1443` n `50` status `ready` deltaP `7.509` edge `0.0024` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.1028` n `50` status `ready` deltaP `6.7805` edge `0.0031` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0228` n `50` status `ready` deltaP `4.2036` edge `-0.0025` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.2261` n `50` status `ready` deltaP `6.7012` edge `-0.0104` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3406` n `137` status `ready` deltaP `4.3894` edge `0.0003` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
