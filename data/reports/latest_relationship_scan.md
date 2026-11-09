# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T20:07:32.551947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `10.2719` n `44` status `ready` deltaP `18.5954` edge `1.4334` maxDD `-16.9034`
- `market_context_high->unknown_4h` score `9.4053` n `88` status `ready` deltaP `7.043` edge `0.7816` maxDD `-0.9153`
- `market_context_high->index_24h` score `1.8596` n `44` status `ready` deltaP `15.5349` edge `0.1811` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `-0.0042` n `44` status `ready` deltaP `-7.2515` edge `0.134` maxDD `-2.8958`
- `market_context_high->metal_1h` score `-0.3688` n `88` status `ready` deltaP `3.6473` edge `0.0126` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5631` n `88` status `ready` deltaP `-0.4559` edge `-0.0009` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8102` n `88` status `ready` deltaP `0.5829` edge `-0.01` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9683` n `88` status `ready` deltaP `-3.3641` edge `0.0089` maxDD `-4.182`
- `market_context_high->fx_24h` score `-0.9841` n `44` status `ready` deltaP `-3.1471` edge `-0.0344` maxDD `-1.6632`
- `market_context_high->metal_4h` score `-1.0531` n `88` status `ready` deltaP `-1.2834` edge `0.0119` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.068` n `88` status `ready` deltaP `-8.703` edge `0.0042` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3016` n `88` status `ready` deltaP `-13.9085` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->metal_24h` score `-1.7279` n `44` status `ready` deltaP `4.5178` edge `-0.1188` maxDD `-1.4245`
- `market_context_high->equity_1h` score `-1.7313` n `88` status `ready` deltaP `-8.1042` edge `0.0167` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0441` n `88` status `ready` deltaP `-0.4151` edge `-0.0614` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.082` n `88` status `ready` deltaP `-6.0727` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2438` n `88` status `ready` deltaP `-5.709` edge `-0.1155` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-5.9066` n `44` status `ready` deltaP `-5.0378` edge `0.0508` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.3717` n `88` status `ready` deltaP `-2.5114` edge `-0.2164` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3416` n `88` status `ready` deltaP `0.787` edge `-0.2719` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
