# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T14:37:25.718919+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `43.8719` n `51` status `ready` deltaP `3.2986` edge `3.634` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.269` n `53` status `ready` deltaP `23.303` edge `0.877` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.7682` n `51` status `ready` deltaP `33.6397` edge `0.5995` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.3124` n `51` status `ready` deltaP `42.6981` edge `0.0899` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1153` n `53` status `ready` deltaP `16.3117` edge `0.1864` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0648` n `53` status `ready` deltaP `36.3352` edge `0.0266` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.3105` n `133` status `ready` deltaP `21.4446` edge `0.0904` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `2.0542` n `53` status `ready` deltaP `22.1756` edge `0.1004` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1872` n `53` status `ready` deltaP `16.3682` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5354` n `53` status `ready` deltaP `14.5718` edge `0.0079` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3697` n `53` status `ready` deltaP `10.2277` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2414` n `53` status `ready` deltaP `8.0333` edge `0.0063` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.0978` n `133` status `ready` deltaP `11.8713` edge `-0.0261` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0394` n `53` status `ready` deltaP `4.4487` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3074` n `53` status `ready` deltaP `6.644` edge `-0.0168` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3743` n `53` status `ready` deltaP `0.1356` edge `-0.0095` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4195` n `133` status `ready` deltaP `2.9479` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.4871` n `51` status `ready` deltaP `22.8656` edge `-0.1888` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.8079` n `133` status `ready` deltaP `5.6368` edge `-0.0412` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.2035` n `133` status `ready` deltaP `-5.9216` edge `-0.007` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
