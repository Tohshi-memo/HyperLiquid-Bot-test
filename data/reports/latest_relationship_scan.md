# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T18:22:32.256445+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->unknown_1h` score `32461.4521` n `45` status `ready` deltaP `2.7644` edge `2705.112` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22296.909` n `45` status `ready` deltaP `3.4824` edge `1858.0664` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1251.9227` n `31` status `ready` deltaP `2.9795` edge `104.3246` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1061.5558` n `31` status `ready` deltaP `4.701` edge `88.4373` maxDD `-0.119`
- `news_risk_high->equity_24h` score `41.396` n `31` status `ready` deltaP `46.1806` edge `3.1418` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.6733` n `31` status `ready` deltaP `47.3958` edge `2.6568` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.5952` n `31` status `ready` deltaP `47.5694` edge `2.3158` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.7648` n `31` status `ready` deltaP `47.3119` edge `0.7758` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.675` n `31` status `ready` deltaP `21.8823` edge `0.7474` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5625` n `31` status `ready` deltaP `30.6698` edge `0.5573` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.4464` n `31` status `ready` deltaP `44.4444` edge `0.2409` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2288` n `31` status `ready` deltaP `52.649` edge `0.1809` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.806` n `31` status `ready` deltaP `11.4427` edge `0.8098` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2217` n `31` status `ready` deltaP `17.8916` edge `0.1679` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1528` n `45` status `ready` deltaP `37.71` edge `0.0398` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9235` n `31` status `ready` deltaP `32.3466` edge `0.054` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3565` n `31` status `ready` deltaP `10.1603` edge `0.2805` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9753` n `31` status `ready` deltaP `9.1124` edge `0.2282` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.8765` n `38` status `ready` deltaP `4.3677` edge `0.2935` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
