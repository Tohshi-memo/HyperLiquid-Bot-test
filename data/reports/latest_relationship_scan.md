# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T13:37:35.804236+00:00`
- Price records: `672`
- Market context records: `6092`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->fx_24h` score `8.163` n `30` status `ready` deltaP `72.7431` edge `0.1953` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.6216` n `30` status `ready` deltaP `32.9166` edge `0.3471` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.2883` n `32` status `ready` deltaP `44.5884` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4183` n `32` status `ready` deltaP `29.0419` edge `0.0218` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.7774` n `195` status `ready` deltaP `9.6951` edge `0.1752` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2254` n `32` status `ready` deltaP `13.5292` edge `0.1136` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6829` n `32` status `ready` deltaP `9.2253` edge `0.0722` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.2938` n `30` status `ready` deltaP `17.5695` edge `-0.0721` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1195` n `30` status `ready` deltaP `9.2361` edge `0.0409` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2583` n `195` status `ready` deltaP `1.7342` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.5469` n `195` status `ready` deltaP `1.986` edge `0.0282` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.5479` n `195` status `ready` deltaP `4.3043` edge `0.0198` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.6614` n `195` status `ready` deltaP `4.595` edge `0.031` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.684` n `195` status `ready` deltaP `-1.3903` edge `-0.0031` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.692` n `32` status `ready` deltaP `-1.7964` edge `-0.027` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.699` n `195` status `ready` deltaP `3.5882` edge `-0.0023` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.893` n `195` status `ready` deltaP `4.2093` edge `0.0327` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9726` n `195` status `ready` deltaP `4.3145` edge `0.0233` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0376` n `32` status `ready` deltaP `-8.7762` edge `-0.0182` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1233` n `195` status `ready` deltaP `-1.7089` edge `0.0047` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
