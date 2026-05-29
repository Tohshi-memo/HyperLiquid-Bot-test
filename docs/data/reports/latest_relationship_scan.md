# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T04:07:19.565913+00:00`
- Price records: `672`
- Market context records: `2209`
- Flow alert records: `8251`
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

- `market_context_high->crypto_alt_4h` score `12.8401` n `132` status `ready` deltaP `36.9965` edge `0.917` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8007` n `132` status `ready` deltaP `42.4335` edge `0.7535` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4599` n `132` status `ready` deltaP `21.3738` edge `0.3804` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8166` n `43` status `ready` deltaP `31.7002` edge `0.3451` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4206` n `132` status `ready` deltaP `23.4156` edge `0.2384` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2218` n `132` status `ready` deltaP `17.5649` edge `0.1991` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2148` n `132` status `ready` deltaP `26.4689` edge `0.1598` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9722` n `132` status `ready` deltaP `16.0588` edge `0.227` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.8741` n `132` status `ready` deltaP `26.5941` edge `0.5437` maxDD `-32.8525`
- `market_context_high->index_24h` score `2.2697` n `132` status `ready` deltaP `10.2114` edge `0.2439` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.2024` n `43` status `ready` deltaP `27.8892` edge `0.016` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.7498` n `132` status `ready` deltaP `17.6294` edge `0.935` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4623` n `43` status `ready` deltaP `21.4942` edge `0.0255` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2963` n `43` status `ready` deltaP `14.4675` edge `0.0839` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2905` n `132` status `ready` deltaP `16.8283` edge `0.1341` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.241` n `43` status `ready` deltaP `-3.2934` edge `0.3018` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7635` n `43` status `ready` deltaP `10.9142` edge `0.0931` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.5016` n `43` status `ready` deltaP `8.5886` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2884` n `132` status `ready` deltaP `9.041` edge `0.0426` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.1746` n `132` status `ready` deltaP `7.7164` edge `0.0301` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
