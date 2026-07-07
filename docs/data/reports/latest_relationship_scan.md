# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T20:22:37.140833+00:00`
- Price records: `672`
- Market context records: `6014`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11126`

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

- `news_risk_high->fx_24h` score `7.6446` n `30` status `ready` deltaP `69.0972` edge `0.1764` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2017` n `30` status `ready` deltaP `43.5061` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.531` n `30` status `ready` deltaP `29.5486` edge `0.1178` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2562` n `30` status `ready` deltaP `27.0758` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.1995` n `187` status `ready` deltaP `26.894` edge `0.4658` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.1085` n `213` status `ready` deltaP `7.2892` edge `0.1528` maxDD `-4.055`
- `news_risk_high->crypto_major_1h` score `0.8107` n `30` status `ready` deltaP `10.1896` edge `0.0827` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1873` n `30` status `ready` deltaP `5.1697` edge `0.0357` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1335` n `30` status `ready` deltaP `9.2361` edge `0.0427` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3831` n `213` status `ready` deltaP `3.7727` edge `0.0056` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4234` n `30` status `ready` deltaP `1.2375` edge `-0.0259` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.5978` n `213` status `ready` deltaP `1.4253` edge `0.0267` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.649` n `213` status `ready` deltaP `-1.1533` edge `0.0` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6766` n `213` status `ready` deltaP `-0.7176` edge `-0.0014` maxDD `-0.6829`
- `market_context_high->index_24h` score `-1.033` n `187` status `ready` deltaP `3.4964` edge `0.0589` maxDD `-9.1714`
- `news_risk_high->index_1h` score `-1.0516` n `30` status `ready` deltaP `-9.7006` edge `-0.0187` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.068` n `213` status `ready` deltaP `2.4936` edge `0.0217` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.0849` n `213` status `ready` deltaP `2.7248` edge `0.0195` maxDD `-9.807`
- `market_context_high->commodity_4h` score `-1.0911` n `213` status `ready` deltaP `-2.1979` edge `-0.0087` maxDD `-2.9891`
- `market_context_high->index_4h` score `-1.1046` n `213` status `ready` deltaP `1.0699` edge `0.0156` maxDD `-2.8149`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
