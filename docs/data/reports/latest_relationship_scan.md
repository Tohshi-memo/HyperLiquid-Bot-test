# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T12:36:57.498761+00:00`
- Price records: `672`
- Market context records: `6182`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `12.644` n `32` status `ready` deltaP `42.302` edge `0.7864` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.0656` n `32` status `ready` deltaP `62.0102` edge `0.1754` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0252` n `32` status `ready` deltaP `41.9148` edge `0.0606` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3268` n `32` status `ready` deltaP `28.0643` edge `0.0207` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.9139` n `32` status `ready` deltaP `15.7102` edge `0.2186` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8859` n `192` status `ready` deltaP `1.4504` edge `0.2483` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.302` n `32` status `ready` deltaP `13.4576` edge `0.1239` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6806` n `32` status `ready` deltaP `8.7024` edge `0.0754` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.5104` n `192` status `ready` deltaP `-0.8307` edge `0.3013` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0486` n `192` status `ready` deltaP `19.9008` edge `0.1304` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1244` n `32` status `ready` deltaP `9.572` edge `0.0074` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1254` n `192` status `ready` deltaP `2.4706` edge `0.0648` maxDD `-2.671`
- `news_risk_high->commodity_24h` score `-0.2762` n `32` status `ready` deltaP `14.869` edge `-0.1016` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.3045` n `192` status `ready` deltaP `0.981` edge `-0.001` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6851` n `192` status `ready` deltaP `3.4673` edge `0.0078` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.8001` n `192` status `ready` deltaP `-2.6158` edge `-0.0046` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8195` n `32` status `ready` deltaP `-3.6622` edge `-0.0309` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.92` n `192` status `ready` deltaP `1.5461` edge `-0.0071` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.983` n `192` status `ready` deltaP `2.9732` edge `0.0294` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9977` n `192` status `ready` deltaP `3.5618` edge `0.0251` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
