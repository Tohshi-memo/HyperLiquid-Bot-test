# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T15:23:18.192154+00:00`
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

- `news_risk_high->unknown_24h` score `43.9904` n `51` status `ready` deltaP `3.8194` edge `3.6404` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.506` n `53` status `ready` deltaP `23.7603` edge `0.8937` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.5753` n `51` status `ready` deltaP `33.1189` edge `0.5869` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2854` n `51` status `ready` deltaP `42.5245` edge `0.0888` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1633` n `53` status `ready` deltaP `16.3117` edge `0.1904` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0258` n `53` status `ready` deltaP `35.8779` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5474` n `133` status `ready` deltaP `21.9019` edge `0.1071` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.9925` n `53` status `ready` deltaP `21.7183` edge `0.0983` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1872` n `53` status `ready` deltaP `16.3682` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5354` n `53` status `ready` deltaP `14.5718` edge `0.0079` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.384` n `53` status `ready` deltaP `10.3774` edge `-0.0059` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2438` n `53` status `ready` deltaP `8.0333` edge `0.0065` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1458` n `133` status `ready` deltaP `11.8713` edge `-0.0221` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0386` n `53` status `ready` deltaP `4.4487` edge `0.0007` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3402` n `53` status `ready` deltaP `6.3391` edge `-0.0175` maxDD `-0.249`
- `news_risk_high->metal_24h` score `-0.3831` n `51` status `ready` deltaP `23.3864` edge `-0.1836` maxDD `-0.0053`
- `news_risk_high->metal_1h` score `-0.4079` n `53` status `ready` deltaP `-0.1638` edge `-0.0103` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4195` n `133` status `ready` deltaP `2.9479` edge `-0.0002` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8406` n `133` status `ready` deltaP `5.3319` edge `-0.0419` maxDD `-2.4293`
- `news_risk_high->crypto_alt_24h` score `-1.1302` n `51` status `ready` deltaP `20.3125` edge `-0.2296` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
