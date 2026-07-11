# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T21:07:24.578920+00:00`
- Price records: `672`
- Market context records: `6430`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.9793` n `32` status `ready` deltaP `30.9028` edge `0.807` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.7971` n `146` status `ready` deltaP `20.3078` edge `0.8444` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5369` n `32` status `ready` deltaP `54.8611` edge `0.179` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1339` n `32` status `ready` deltaP `43.064` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1125` n `32` status `ready` deltaP `35.2431` edge `0.1283` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.4193` n `32` status `ready` deltaP `12.5` edge `0.433` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.459` n `32` status `ready` deltaP `29.6407` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4835` n `32` status `ready` deltaP `13.9783` edge `0.1437` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.0757` n `197` status `ready` deltaP `-6.0526` edge `0.2201` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8287` n `32` status `ready` deltaP `9.6744` edge `0.0879` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.1627` n `193` status `ready` deltaP `8.6985` edge `0.0232` maxDD `-0.4108`
- `market_context_high->metal_4h` score `0.1335` n `193` status `ready` deltaP `9.3414` edge `0.041` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2058` n `32` status `ready` deltaP `7.1295` edge `-0.0302` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3774` n `146` status `ready` deltaP `17.0638` edge `0.0947` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5398` n `197` status `ready` deltaP `0.9696` edge `0.0021` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5963` n `32` status `ready` deltaP `-0.2994` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.5965` n `193` status `ready` deltaP `-14.766` edge `0.2893` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-0.6138` n `193` status `ready` deltaP `6.6584` edge `0.0468` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6254` n `197` status `ready` deltaP `-1.4514` edge `-0.0022` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6817` n `197` status `ready` deltaP `-2.766` edge `0.003` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
