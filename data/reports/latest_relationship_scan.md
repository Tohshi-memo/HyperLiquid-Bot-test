# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T04:22:24.530747+00:00`
- Price records: `672`
- Market context records: `6462`
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

- `news_risk_high->crypto_alt_24h` score `11.9482` n `32` status `ready` deltaP `31.25` edge `0.8021` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.3363` n `148` status `ready` deltaP `16.7981` edge `0.8294` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3118` n `32` status `ready` deltaP `52.2569` edge `0.1776` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1084` n `32` status `ready` deltaP `42.7591` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.6225` n `32` status `ready` deltaP `13.5417` edge `0.4521` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.5635` n `32` status `ready` deltaP `31.7708` edge `0.1057` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.5243` n `33` status `ready` deltaP `30.548` edge `0.0206` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6214` n `172` status `ready` deltaP `-5.337` edge `0.2608` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.4177` n `33` status `ready` deltaP `13.523` edge `0.1383` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8149` n `33` status `ready` deltaP `9.4085` edge `0.0879` maxDD `-1.6923`
- `market_context_high->commodity_24h` score `0.3394` n `148` status `ready` deltaP `6.8553` edge `0.1694` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.326` n `172` status `ready` deltaP `10.1248` edge `0.0273` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2717` n `172` status `ready` deltaP `-15.0879` edge `0.3638` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.2522` n `172` status `ready` deltaP `8.3983` edge `0.1204` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.0713` n `172` status `ready` deltaP `10.6743` edge `0.0436` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4747` n `32` status `ready` deltaP `4.5139` edge `-0.0038` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5427` n `172` status `ready` deltaP `1.0479` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5833` n `172` status `ready` deltaP `6.6151` edge `0.051` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5837` n `172` status `ready` deltaP `-0.3342` edge `-0.0043` maxDD `-2.1314`
- `news_risk_high->unknown_1h` score `-0.6027` n `33` status `ready` deltaP `3.983` edge `-0.0423` maxDD `-0.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
