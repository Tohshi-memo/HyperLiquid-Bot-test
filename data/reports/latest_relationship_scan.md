# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T03:52:29.603602+00:00`
- Price records: `672`
- Market context records: `6459`
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

- `news_risk_high->crypto_alt_24h` score `11.8833` n `32` status `ready` deltaP `30.9028` edge `0.799` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.396` n `147` status `ready` deltaP `16.9289` edge `0.8335` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3106` n `32` status `ready` deltaP `52.2569` edge `0.1775` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0962` n `32` status `ready` deltaP `42.6067` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.6153` n `32` status `ready` deltaP `32.1181` edge `0.1077` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.549` n `32` status `ready` deltaP `13.1944` edge `0.445` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4578` n `32` status `ready` deltaP `29.6407` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5734` n `172` status `ready` deltaP `-5.6364` edge `0.2588` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.4126` n `32` status `ready` deltaP `12.7807` edge `0.1426` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7586` n `32` status `ready` deltaP `8.4768` edge `0.0869` maxDD `-1.6923`
- `market_context_high->commodity_24h` score `0.3523` n `147` status `ready` deltaP `6.9268` edge `0.17` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.3354` n `172` status `ready` deltaP `8.7032` edge `0.1253` maxDD `-6.7632`
- `market_context_high->index_4h` score `0.3004` n `172` status `ready` deltaP `9.8199` edge `0.0272` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2983` n `172` status `ready` deltaP `-14.9355` edge `0.365` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.0713` n `172` status `ready` deltaP `10.6743` edge `0.0436` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2787` n `32` status `ready` deltaP `5.4828` edge `-0.0253` maxDD `-0.7581`
- `news_risk_high->index_24h` score `-0.4975` n `32` status `ready` deltaP `4.1667` edge `-0.0044` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.5223` n `32` status `ready` deltaP `1.0479` edge `-0.0242` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5427` n `172` status `ready` deltaP `1.0479` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5841` n `172` status `ready` deltaP `6.6151` edge `0.0509` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
