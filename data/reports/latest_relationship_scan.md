# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T08:37:26.874341+00:00`
- Price records: `672`
- Market context records: `8179`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8708.8251` n `42` status `ready` deltaP `36.9792` edge `725.4889` maxDD `0.0`
- `market_context_high->equity_24h` score `19.1679` n `52` status `ready` deltaP `43.6432` edge `1.3974` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.4679` n `53` status `ready` deltaP `37.9745` edge `0.5593` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.3591` n `52` status `ready` deltaP `43.2292` edge `0.4084` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.2096` n `47` status `ready` deltaP `30.3872` edge `0.5109` maxDD `-1.3479`
- `market_context_high->index_4h` score `4.0876` n `53` status `ready` deltaP `36.8126` edge `0.0995` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.4299` n `50` status `ready` deltaP `25.6048` edge `0.146` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.2648` n `47` status `ready` deltaP `17.6408` edge `0.3625` maxDD `-2.2569`
- `market_context_high->equity_1h` score `3.1583` n `53` status `ready` deltaP `17.4161` edge `0.1674` maxDD `-0.6254`
- `news_risk_high->index_4h` score `2.7544` n `47` status `ready` deltaP `23.0832` edge `0.0947` maxDD `-0.191`
- `market_context_high->crypto_alt_24h` score `2.661` n `52` status `ready` deltaP `6.3702` edge `0.6352` maxDD `-16.9208`
- `market_context_high->metal_4h` score `2.2476` n `53` status `ready` deltaP `24.4622` edge `0.0656` maxDD `-0.6441`
- `market_context_high->index_24h` score `1.9374` n `52` status `ready` deltaP `17.2143` edge `0.2004` maxDD `-1.342`
- `market_context_high->index_1h` score `1.9333` n `53` status `ready` deltaP `22.2969` edge `0.0263` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.8942` n `50` status `ready` deltaP `12.0419` edge `0.1173` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.6448` n `47` status `ready` deltaP `15.1888` edge `0.0826` maxDD `-0.7433`
- `news_risk_high->crypto_alt_1h` score `1.6269` n `50` status `ready` deltaP `12.1916` edge `0.0977` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3828` n `47` status `ready` deltaP `15.9704` edge `0.21` maxDD `-5.8012`
- `market_context_high->fx_24h` score `0.9389` n `52` status `ready` deltaP `19.6047` edge `0.0557` maxDD `-0.6156`
- `market_context_high->crypto_alt_4h` score `0.6718` n `53` status `ready` deltaP `3.3249` edge `0.1643` maxDD `-3.0268`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
