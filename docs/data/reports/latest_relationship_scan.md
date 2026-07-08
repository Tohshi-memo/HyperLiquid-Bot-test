# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T00:22:25.638260+00:00`
- Price records: `672`
- Market context records: `6033`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.9465` n `30` status `ready` deltaP `71.7014` edge `0.1842` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3063` n `30` status `ready` deltaP `44.5732` edge `0.0663` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.7868` n `30` status `ready` deltaP `26.7709` edge `0.0743` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2562` n `30` status `ready` deltaP `27.0758` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.7278` n `180` status `ready` deltaP `29.7223` edge `0.5685` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.6481` n `206` status `ready` deltaP `9.0989` edge `0.1684` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.8271` n `30` status `ready` deltaP `10.1896` edge `0.0848` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2449` n `30` status `ready` deltaP `5.7685` edge `0.0391` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1483` n `30` status `ready` deltaP `9.2361` edge `0.0446` maxDD `-2.3058`
- `news_risk_high->crypto_alt_24h` score `-0.1145` n `30` status `ready` deltaP `23.7152` edge `-0.1529` maxDD `-0.5131`
- `market_context_high->metal_1h` score `-0.3963` n `206` status `ready` deltaP `3.5797` edge `0.0052` maxDD `-2.0564`
- `market_context_high->index_24h` score `-0.4312` n `180` status `ready` deltaP `5.3472` edge `0.0791` maxDD `-5.6021`
- `news_risk_high->metal_1h` score `-0.4328` n `30` status `ready` deltaP `1.0878` edge `-0.0261` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5762` n `206` status `ready` deltaP `-0.141` edge `-0.0014` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6787` n `206` status `ready` deltaP `-1.683` edge `-0.0007` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.9321` n `206` status `ready` deltaP `5.0956` edge `0.0071` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.9339` n `206` status `ready` deltaP `2.4154` edge `0.0175` maxDD `-1.9335`
- `market_context_high->crypto_alt_1h` score `-0.9616` n `206` status `ready` deltaP `3.9562` edge `0.0256` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-0.9833` n `206` status `ready` deltaP `0.9302` edge `0.0247` maxDD `-4.3608`
- `market_context_high->crypto_major_1h` score `-0.9906` n `206` status `ready` deltaP `3.6524` edge `0.0254` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
