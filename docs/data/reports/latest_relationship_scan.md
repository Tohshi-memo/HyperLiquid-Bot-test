# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T21:07:27.949784+00:00`
- Price records: `672`
- Market context records: `6018`
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

- `news_risk_high->fx_24h` score `7.688` n `30` status `ready` deltaP `69.4444` edge `0.1777` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2175` n `30` status `ready` deltaP `43.6585` edge `0.065` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3921` n `30` status `ready` deltaP `29.0278` edge `0.1097` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.231` n `30` status `ready` deltaP `26.7764` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2791` n `210` status `ready` deltaP `8.1141` edge `0.1569` maxDD `-3.6853`
- `market_context_high->equity_24h` score `1.1026` n `184` status `ready` deltaP `28.0797` edge `0.4993` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.813` n `30` status `ready` deltaP `10.1896` edge `0.083` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2036` n `30` status `ready` deltaP `5.3194` edge `0.0368` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1366` n `30` status `ready` deltaP `9.2361` edge `0.0431` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3555` n `210` status `ready` deltaP `4.2444` edge `0.006` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4133` n `30` status `ready` deltaP `1.3872` edge `-0.0256` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.6826` n `210` status `ready` deltaP `-1.5512` edge `-0.0006` maxDD `-0.6751`
- `market_context_high->fx_1h` score `-0.6878` n `210` status `ready` deltaP `-0.8426` edge `-0.0015` maxDD `-0.6829`
- `market_context_high->index_24h` score `-0.772` n `184` status `ready` deltaP `4.2724` edge `0.0673` maxDD `-7.5805`
- `market_context_high->equity_1h` score `-0.9896` n `210` status `ready` deltaP `0.7613` edge `0.0253` maxDD `-4.3608`
- `market_context_high->crypto_alt_1h` score `-1.0426` n `210` status `ready` deltaP `2.9384` edge `0.022` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.0446` n `30` status `ready` deltaP `-9.5509` edge `-0.0188` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.0476` n `210` status `ready` deltaP `1.8278` edge `0.0162` maxDD `-2.6825`
- `market_context_high->crypto_major_1h` score `-1.0518` n `210` status `ready` deltaP `3.0468` edge `0.0216` maxDD `-9.807`
- `market_context_high->commodity_4h` score `-1.0567` n `210` status `ready` deltaP `-2.018` edge `-0.0105` maxDD `-2.9219`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
