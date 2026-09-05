# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T12:37:28.129047+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11019`

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

- `risk_on_high->unknown_4h` score `22.8126` n `140` status `ready` deltaP `6.507` edge `1.9195` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.8126` n `140` status `ready` deltaP `6.507` edge `1.9195` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.8041` n `228` status `ready` deltaP `6.6699` edge `0.9289` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.5287` n `37` status `ready` deltaP `25.1783` edge `0.4865` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9794` n `37` status `ready` deltaP `21.5278` edge `0.1881` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6462` n `37` status `ready` deltaP `17.1803` edge `0.2306` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.2578` n `37` status `ready` deltaP `22.7794` edge `0.0584` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.969` n `37` status `ready` deltaP `12.191` edge `0.1029` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5835` n `37` status `ready` deltaP `13.0847` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2083` n `37` status `ready` deltaP `14.4158` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1799` n `37` status `ready` deltaP `6.1661` edge `0.0755` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `1.0335` n `37` status `ready` deltaP `16.5776` edge `0.2996` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.9081` n `37` status `ready` deltaP `8.8769` edge `0.043` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6191` n `37` status `ready` deltaP `6.3983` edge `0.0418` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.5037` n `37` status `ready` deltaP `15.0947` edge `0.0429` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.2883` n `121` status `ready` deltaP `20.7545` edge `0.773` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.2883` n `121` status `ready` deltaP `20.7545` edge `0.773` maxDD `-56.9519`
- `market_context_high->equity_24h` score `0.2415` n `192` status `ready` deltaP `15.7986` edge `0.3602` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.0811` n `152` status `ready` deltaP `12.0509` edge `0.0013` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
