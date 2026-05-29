# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T01:37:19.740929+00:00`
- Price records: `672`
- Market context records: `2199`
- Flow alert records: `8221`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.6433` n `132` status `ready` deltaP `36.0819` edge `0.9067` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6496` n `132` status `ready` deltaP `41.5189` edge `0.747` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4515` n `132` status `ready` deltaP `21.3738` edge `0.3797` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8151` n `43` status `ready` deltaP `31.7002` edge `0.3449` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4074` n `132` status `ready` deltaP `23.4156` edge `0.2373` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.3903` n `132` status `ready` deltaP `28.1566` edge `0.5763` maxDD `-32.8525`
- `market_context_high->crypto_major_1h` score `3.2146` n `132` status `ready` deltaP `17.5649` edge `0.1985` maxDD `-1.817`
- `market_context_high->index_4h` score `3.052` n `132` status `ready` deltaP `24.9446` edge `0.1564` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9087` n `132` status `ready` deltaP `15.7594` edge `0.2237` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.5244` n `132` status `ready` deltaP `10.9059` edge `0.2605` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.2655` n `132` status `ready` deltaP `19.1919` edge `0.9907` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.388` n `43` status `ready` deltaP `21.0451` edge `0.0223` maxDD `-1.7548`
- `market_context_high->metal_4h` score `1.3703` n `132` status `ready` deltaP `17.2856` edge `0.1377` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.2879` n `43` status `ready` deltaP `14.4675` edge `0.0832` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2324` n `43` status `ready` deltaP `-3.2934` edge `0.3007` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7541` n `43` status `ready` deltaP `10.7645` edge `0.0929` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4118` n `43` status `ready` deltaP `7.5407` edge `0.0097` maxDD `-0.0524`
- `market_context_high->equity_24h` score `0.3655` n `132` status `ready` deltaP `20.423` edge `0.3789` maxDD `-33.1007`
- `market_context_high->equity_1h` score `0.3196` n `132` status `ready` deltaP `9.1907` edge `0.0442` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
