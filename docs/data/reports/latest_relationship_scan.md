# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T03:57:52.820290+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.8602` n `73` status `ready` deltaP `12.1008` edge `0.3618` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.6995` n `73` status `ready` deltaP `12.6469` edge `0.1573` maxDD `-4.666`
- `market_context_high->metal_24h` score `0.5964` n `73` status `ready` deltaP `4.8384` edge `0.0739` maxDD `-1.5165`
- `market_context_high->commodity_4h` score `0.4104` n `104` status `ready` deltaP `10.5652` edge `0.0488` maxDD `-2.4692`
- `market_context_high->index_1h` score `0.0846` n `104` status `ready` deltaP `7.4735` edge `0.003` maxDD `-0.3584`
- `market_context_high->metal_4h` score `0.0129` n `104` status `ready` deltaP `9.0056` edge `0.0047` maxDD `-1.7135`
- `market_context_high->unknown_1h` score `-0.0043` n `104` status `ready` deltaP `7.0705` edge `-0.0216` maxDD `-0.7386`
- `market_context_high->crypto_major_4h` score `-0.0615` n `104` status `ready` deltaP `5.2533` edge `0.0647` maxDD `-3.6083`
- `market_context_high->equity_1h` score `-0.1197` n `104` status `ready` deltaP `3.1956` edge `0.0236` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.1826` n `104` status `ready` deltaP `5.054` edge `0.0018` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.6163` n `104` status `ready` deltaP `-1.3243` edge `-0.0034` maxDD `-1.3425`
- `market_context_high->commodity_1h` score `-0.6896` n `104` status `ready` deltaP `-4.2953` edge `0.0015` maxDD `-1.5684`
- `market_context_high->fx_1h` score `-0.7157` n `104` status `ready` deltaP `-3.6101` edge `0.0006` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.7722` n `104` status `ready` deltaP `-4.6084` edge `-0.0014` maxDD `-0.6837`
- `market_context_high->index_24h` score `-0.8959` n `73` status `ready` deltaP `6.9253` edge `-0.0605` maxDD `-1.8262`
- `market_context_high->unknown_24h` score `-0.9579` n `73` status `ready` deltaP `3.8152` edge `-0.0836` maxDD `-1.1716`
- `market_context_high->crypto_major_1h` score `-0.993` n `104` status `ready` deltaP `-4.2953` edge `-0.0031` maxDD `-3.6463`
- `market_context_high->crypto_alt_1h` score `-1.2684` n `104` status `ready` deltaP `-3.2474` edge `0.0048` maxDD `-3.1082`
- `market_context_high->crypto_alt_4h` score `-1.3545` n `104` status `ready` deltaP `3.4944` edge `0.0415` maxDD `-10.0758`
- `market_context_high->equity_4h` score `-1.4044` n `104` status `ready` deltaP `-7.2585` edge `-0.0167` maxDD `-4.53`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
