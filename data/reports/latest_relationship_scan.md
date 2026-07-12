# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T04:52:33.270173+00:00`
- Price records: `672`
- Market context records: `6464`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5907`

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

- `news_risk_high->crypto_alt_24h` score `12.024` n `32` status `ready` deltaP `31.5972` edge `0.8061` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.1702` n `150` status `ready` deltaP `16.7014` edge `0.8162` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.313` n `32` status `ready` deltaP `52.2569` edge `0.1777` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1084` n `32` status `ready` deltaP `42.7591` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.7029` n `32` status `ready` deltaP `13.8889` edge `0.4601` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.507` n `32` status `ready` deltaP `31.4236` edge `0.1033` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.1624` n `35` status `ready` deltaP `26.219` edge `0.0193` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5938` n `172` status `ready` deltaP `-5.4867` edge `0.2595` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.048` n `35` status `ready` deltaP `9.7134` edge `0.1163` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.4913` n `35` status `ready` deltaP `5.9453` edge `0.0695` maxDD `-1.6923`
- `market_context_high->commodity_24h` score `0.368` n `150` status `ready` deltaP `7.0486` edge `0.1705` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.3406` n `172` status `ready` deltaP `10.2773` edge `0.0275` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2439` n `172` status `ready` deltaP `-15.2404` edge `0.3625` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.181` n `172` status `ready` deltaP `8.0934` edge `0.1165` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.0579` n `172` status `ready` deltaP `10.5218` edge `0.0435` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4626` n `32` status `ready` deltaP `4.6875` edge `-0.0034` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5435` n `172` status `ready` deltaP `1.0479` edge `0.0011` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.581` n `172` status `ready` deltaP `6.6151` edge `0.0513` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5837` n `172` status `ready` deltaP `-0.3342` edge `-0.0043` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7022` n `172` status `ready` deltaP `-3.2064` edge `0.0033` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
