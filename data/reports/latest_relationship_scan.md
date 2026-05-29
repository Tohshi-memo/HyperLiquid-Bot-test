# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T04:22:20.331827+00:00`
- Price records: `672`
- Market context records: `2210`
- Flow alert records: `8254`
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

- `market_context_high->crypto_alt_4h` score `12.8847` n `132` status `ready` deltaP `37.149` edge `0.9197` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8357` n `132` status `ready` deltaP `42.5859` edge `0.7554` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4599` n `132` status `ready` deltaP `21.3738` edge `0.3804` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8174` n `43` status `ready` deltaP `31.7002` edge `0.3452` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4266` n `132` status `ready` deltaP `23.4156` edge `0.2389` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.247` n `132` status `ready` deltaP `17.7146` edge `0.2002` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2282` n `132` status `ready` deltaP `26.6214` edge `0.1599` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9986` n `132` status `ready` deltaP `16.2085` edge `0.2282` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.8062` n `132` status `ready` deltaP `26.4205` edge `0.5392` maxDD `-32.8525`
- `market_context_high->index_24h` score `2.2186` n `132` status `ready` deltaP `10.0378` edge `0.2408` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.2036` n `43` status `ready` deltaP `27.8892` edge `0.0161` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.6838` n `132` status `ready` deltaP `17.4558` edge `0.9277` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4863` n `43` status `ready` deltaP `21.6439` edge `0.0265` maxDD `-1.7548`
- `market_context_high->metal_4h` score `1.3063` n `132` status `ready` deltaP `16.9808` edge `0.1344` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.2963` n `43` status `ready` deltaP `14.4675` edge `0.0839` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2449` n `43` status `ready` deltaP `-3.2934` edge `0.3023` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7541` n `43` status `ready` deltaP `10.7645` edge `0.0929` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.5016` n `43` status `ready` deltaP `8.5886` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2741` n `132` status `ready` deltaP `8.8913` edge `0.0424` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.159` n `132` status `ready` deltaP `7.5667` edge `0.0298` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
