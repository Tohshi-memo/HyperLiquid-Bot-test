# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T02:52:26.195734+00:00`
- Price records: `672`
- Market context records: `6044`
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

- `news_risk_high->fx_24h` score `7.9988` n `30` status `ready` deltaP `71.875` edge `0.1874` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2211` n `30` status `ready` deltaP `43.6585` edge `0.0653` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.3443` n `30` status `ready` deltaP `25.0348` edge `0.049` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3089` n `30` status `ready` deltaP `27.6746` edge `0.0218` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5313` n `206` status `ready` deltaP `8.7941` edge `0.1607` maxDD `-2.671`
- `news_risk_high->crypto_alt_24h` score `1.0563` n `30` status `ready` deltaP `25.4514` edge `-0.0669` maxDD `-0.5131`
- `news_risk_high->crypto_major_1h` score `1.004` n `30` status `ready` deltaP `11.2375` edge `0.1005` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.6301` n `184` status `ready` deltaP `28.0797` edge `0.543` maxDD `-38.6198`
- `news_risk_high->crypto_alt_1h` score `0.3822` n `30` status `ready` deltaP `6.3673` edge `0.0527` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1343` n `30` status `ready` deltaP `9.2361` edge `0.0428` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4275` n `206` status `ready` deltaP `3.2803` edge `0.0032` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.464` n `30` status `ready` deltaP `0.7884` edge `-0.0281` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5234` n `206` status `ready` deltaP `0.4578` edge `-0.001` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6763` n `206` status `ready` deltaP `-1.683` edge `-0.0005` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8137` n `206` status `ready` deltaP `4.7003` edge `0.0411` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8244` n `206` status `ready` deltaP `4.555` edge `0.0392` maxDD `-9.3536`
- `market_context_high->index_24h` score `-0.8333` n `184` status `ready` deltaP `4.2724` edge `0.0721` maxDD `-5.6021`
- `market_context_high->index_4h` score `-0.9868` n `206` status `ready` deltaP `1.6532` edge `0.0158` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-1.0413` n `206` status `ready` deltaP `4.181` edge `0.0041` maxDD `-3.4996`
- `news_risk_high->index_1h` score `-1.0446` n `30` status `ready` deltaP `-9.4012` edge `-0.0198` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
