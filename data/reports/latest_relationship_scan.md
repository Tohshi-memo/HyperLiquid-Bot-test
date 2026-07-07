# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T07:56:24.482354+00:00`
- Price records: `672`
- Market context records: `5961`
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

- `news_risk_high->fx_24h` score `7.003` n `30` status `ready` deltaP `64.0625` edge `0.1565` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.3162` n `30` status `ready` deltaP `38.2292` edge `0.2087` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8442` n `30` status `ready` deltaP `39.8476` edge `0.0593` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1208` n `30` status `ready` deltaP `25.5788` edge `0.0201` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4672` n `229` status `ready` deltaP `9.4665` edge `0.1686` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8349` n `30` status `ready` deltaP `10.1896` edge `0.0858` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2029` n `30` status `ready` deltaP `5.3194` edge `0.0367` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1671` n `30` status `ready` deltaP `6.9791` edge `0.0192` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3395` n `239` status `ready` deltaP `4.9232` edge `0.0365` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.3658` n `30` status `ready` deltaP `2.2854` edge `-0.0255` maxDD `-1.2643`
- `market_context_high->equity_24h` score `-0.4353` n `213` status `ready` deltaP `21.1366` edge `0.3109` maxDD `-31.2762`
- `market_context_high->metal_1h` score `-0.4754` n `239` status `ready` deltaP `2.5086` edge `0.0022` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5784` n `239` status `ready` deltaP `-2.689` edge `-0.0005` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6215` n `239` status `ready` deltaP `-0.0558` edge `-0.0003` maxDD `-0.756`
- `market_context_high->index_1h` score `-0.6293` n `239` status `ready` deltaP `0.8656` edge `0.0049` maxDD `-1.3078`
- `market_context_high->crypto_major_1h` score `-1.0884` n `239` status `ready` deltaP `2.0864` edge `0.0233` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.0984` n `239` status `ready` deltaP `2.2092` edge `0.0197` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.117` n `30` status `ready` deltaP `-10.5988` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.5467` n `229` status `ready` deltaP `-2.4384` edge `-0.0107` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5785` n `229` status `ready` deltaP `-2.1508` edge `-0.0248` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
