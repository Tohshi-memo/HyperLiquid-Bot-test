# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T07:22:23.866783+00:00`
- Price records: `672`
- Market context records: `6368`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `news_risk_high->crypto_alt_24h` score `14.5901` n `32` status `ready` deltaP `39.5833` edge `0.9667` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3112` n `32` status `ready` deltaP `52.4306` edge `0.1764` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3816` n `32` status `ready` deltaP `17.5347` edge `0.5228` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0254` n `32` status `ready` deltaP `41.6921` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9958` n `32` status `ready` deltaP `34.5486` edge `0.1232` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3739` n `32` status `ready` deltaP `28.5928` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5505` n `32` status `ready` deltaP `15.0262` edge `0.1453` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9205` n `32` status `ready` deltaP `11.4708` edge `0.0877` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5213` n `212` status `ready` deltaP `15.6581` edge `0.0421` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2523` n `220` status `ready` deltaP `-6.6249` edge `0.166` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1267` n `212` status `ready` deltaP `8.4589` edge `0.0218` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3496` n `32` status `ready` deltaP `5.9319` edge `-0.0342` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.4113` n `220` status `ready` deltaP `3.3642` edge `0.0026` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.56` n `133` status `ready` deltaP `15.9383` edge `0.0788` maxDD `-11.8809`
- `market_context_high->commodity_24h` score `-0.5758` n `133` status `ready` deltaP `-3.9617` edge `0.139` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.6238` n `220` status `ready` deltaP `-1.6521` edge `0.003` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6621` n `220` status `ready` deltaP `-0.0436` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7144` n `32` status `ready` deltaP `0.5208` edge `-0.0079` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7177` n `32` status `ready` deltaP `-2.5449` edge `-0.0253` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.9408` n `212` status `ready` deltaP `6.5377` edge `0.0479` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
