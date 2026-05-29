# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T01:52:18.412403+00:00`
- Price records: `672`
- Market context records: `2200`
- Flow alert records: `8224`
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

- `market_context_high->crypto_alt_4h` score `12.6639` n `132` status `ready` deltaP `36.2343` edge `0.9074` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6726` n `132` status `ready` deltaP `41.6713` edge `0.7479` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4575` n `132` status `ready` deltaP `21.3738` edge `0.3802` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8127` n `43` status `ready` deltaP `31.7002` edge `0.3446` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3904` n `132` status `ready` deltaP `23.2631` edge `0.2369` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.3584` n `132` status `ready` deltaP `27.983` edge `0.5748` maxDD `-32.8525`
- `market_context_high->crypto_major_1h` score `3.2398` n `132` status `ready` deltaP `17.7146` edge `0.1996` maxDD `-1.817`
- `market_context_high->index_4h` score `3.0678` n `132` status `ready` deltaP `25.097` edge `0.1567` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9303` n `132` status `ready` deltaP `15.9091` edge `0.2245` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.516` n `132` status `ready` deltaP `10.9059` edge `0.2598` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.2221` n `132` status `ready` deltaP `19.0183` edge `0.9863` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1964` n `43` status `ready` deltaP `27.8892` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.4048` n `43` status `ready` deltaP `21.1948` edge `0.0227` maxDD `-1.7548`
- `market_context_high->metal_4h` score `1.3461` n `132` status `ready` deltaP `17.1332` edge `0.1367` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.2939` n `43` status `ready` deltaP `14.4675` edge `0.0837` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2213` n `43` status `ready` deltaP `-3.4459` edge `0.3003` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.744` n `43` status `ready` deltaP `10.6148` edge `0.0926` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4106` n `43` status `ready` deltaP `7.5407` edge `0.0096` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3352` n `132` status `ready` deltaP `9.3404` edge `0.0445` maxDD `-2.6402`
- `market_context_high->equity_24h` score `0.2676` n `132` status `ready` deltaP `20.2493` edge `0.3719` maxDD `-33.1007`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
