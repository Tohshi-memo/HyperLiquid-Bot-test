# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T07:07:26.896627+00:00`
- Price records: `672`
- Market context records: `6062`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11073`

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

- `news_risk_high->fx_24h` score `8.1378` n `30` status `ready` deltaP `72.7431` edge `0.1932` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3659` n `30` status `ready` deltaP `45.1829` edge `0.0672` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `2.7949` n `30` status `ready` deltaP `28.4027` edge `0.0583` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.3376` n `30` status `ready` deltaP `27.974` edge `0.0222` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.5646` n `30` status `ready` deltaP `22.0834` edge `0.0037` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.3855` n `206` status `ready` deltaP `8.3367` edge `0.1516` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0172` n `30` status `ready` deltaP `11.6866` edge `0.0992` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3642` n `30` status `ready` deltaP `6.2176` edge `0.0514` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0883` n `30` status `ready` deltaP `9.2361` edge `0.0369` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4905` n `206` status `ready` deltaP `2.3821` edge `0.0011` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4947` n `206` status `ready` deltaP `0.7572` edge `-0.0006` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.527` n `30` status `ready` deltaP `-0.1098` edge `-0.0302` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.7529` n `206` status `ready` deltaP `-2.4315` edge `-0.0019` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8005` n `206` status `ready` deltaP `5.1494` edge `0.0398` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8423` n `206` status `ready` deltaP `4.4053` edge `0.0379` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9776` n `206` status `ready` deltaP `1.5007` edge `0.018` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.022` n `30` status `ready` deltaP `-9.1018` edge `-0.0189` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0505` n `206` status `ready` deltaP `0.7805` edge `0.0201` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.195` n `206` status `ready` deltaP `3.1139` edge `-0.0016` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2638` n `206` status `ready` deltaP `-4.7981` edge `-0.0231` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
