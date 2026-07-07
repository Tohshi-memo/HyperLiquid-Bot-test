# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T07:37:25.692871+00:00`
- Price records: `672`
- Market context records: `5959`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.9855` n `30` status `ready` deltaP `63.8889` edge `0.1562` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.3445` n `30` status `ready` deltaP `38.4028` edge `0.2099` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8442` n `30` status `ready` deltaP `39.8476` edge `0.0593` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1208` n `30` status `ready` deltaP `25.5788` edge `0.0201` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4475` n `228` status `ready` deltaP `9.3095` edge `0.168` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8364` n `30` status `ready` deltaP `10.1896` edge `0.086` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2044` n `30` status `ready` deltaP `5.3194` edge `0.0369` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1718` n `30` status `ready` deltaP `6.9791` edge `0.0186` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3371` n `239` status `ready` deltaP `4.9232` edge `0.0368` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.3635` n `30` status `ready` deltaP `2.2854` edge `-0.0252` maxDD `-1.2643`
- `market_context_high->equity_24h` score `-0.4677` n `213` status `ready` deltaP `20.9629` edge `0.3079` maxDD `-31.2762`
- `market_context_high->metal_1h` score `-0.4731` n `239` status `ready` deltaP `2.5086` edge `0.0025` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5784` n `239` status `ready` deltaP `-2.689` edge `-0.0005` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6215` n `239` status `ready` deltaP `-0.0558` edge `-0.0003` maxDD `-0.756`
- `market_context_high->index_1h` score `-0.6293` n `239` status `ready` deltaP `0.8656` edge `0.0049` maxDD `-1.3078`
- `market_context_high->crypto_major_1h` score `-1.0869` n `239` status `ready` deltaP `2.0864` edge `0.0235` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.0969` n `239` status `ready` deltaP `2.2092` edge `0.0199` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.117` n `30` status `ready` deltaP `-10.5988` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.57` n `228` status `ready` deltaP `-2.6931` edge `-0.012` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5761` n `228` status `ready` deltaP `-2.0753` edge `-0.025` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
