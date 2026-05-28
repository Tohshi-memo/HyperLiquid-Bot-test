# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T23:00:00.269917+00:00`
- Price records: `672`
- Market context records: `2187`
- Flow alert records: `8188`
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

- `market_context_high->crypto_alt_4h` score `12.7687` n `132` status `ready` deltaP `36.5392` edge `0.9141` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7475` n `132` status `ready` deltaP `42.1286` edge `0.7511` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4431` n `132` status `ready` deltaP `21.3738` edge `0.379` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8348` n `43` status `ready` deltaP `32.0051` edge `0.3454` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.7654` n `132` status `ready` deltaP `29.5455` edge `0.5983` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.5524` n `132` status `ready` deltaP `24.1778` edge `0.2443` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.241` n `132` status `ready` deltaP `17.7146` edge `0.1997` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.019` n `132` status `ready` deltaP `16.3582` edge `0.2289` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.8921` n `132` status `ready` deltaP `23.725` edge `0.1512` maxDD `-1.8022`
- `market_context_high->crypto_major_24h` score `2.7013` n `132` status `ready` deltaP `20.928` edge `1.035` maxDD `-60.2561`
- `market_context_high->index_24h` score `2.6108` n `132` status `ready` deltaP `10.9059` edge `0.2677` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.5495` n `132` status `ready` deltaP `18.5052` edge `0.1445` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4635` n `43` status `ready` deltaP `21.4942` edge `0.0256` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.3266` n `43` status `ready` deltaP `-2.5312` edge `0.3077` maxDD `-4.6598`
- `market_context_high->equity_24h` score `1.2868` n `132` status `ready` deltaP `22.1591` edge `0.4441` maxDD `-33.1007`
- `news_risk_high->unknown_4h` score `1.2795` n `43` status `ready` deltaP `14.4675` edge `0.0825` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `0.7471` n `43` status `ready` deltaP `10.6148` edge `0.093` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.5016` n `43` status `ready` deltaP `8.5886` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2873` n `132` status `ready` deltaP `8.8913` edge `0.0435` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
