# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T05:52:29.500051+00:00`
- Price records: `672`
- Market context records: `6057`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11103`

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

- `news_risk_high->fx_24h` score `8.1114` n `30` status `ready` deltaP `72.7431` edge `0.191` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2953` n `30` status `ready` deltaP `44.4207` edge `0.0664` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3101` n `30` status `ready` deltaP `27.6746` edge `0.0219` maxDD `-0.1113`
- `news_risk_high->crypto_alt_24h` score `2.2274` n `30` status `ready` deltaP `27.5347` edge `0.0168` maxDD `-0.5131`
- `news_risk_high->commodity_24h` score `1.7804` n `30` status `ready` deltaP `22.9514` edge `0.0159` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.2899` n `206` status `ready` deltaP `7.727` edge `0.1477` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.9814` n `30` status `ready` deltaP `11.2375` edge `0.0976` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3518` n `30` status `ready` deltaP `6.0679` edge `0.0508` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0992` n `30` status `ready` deltaP `9.2361` edge `0.0383` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5085` n `206` status `ready` deltaP `2.0827` edge `0.0008` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5222` n `206` status `ready` deltaP `0.4578` edge `-0.0009` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.5449` n `30` status `ready` deltaP `-0.4092` edge `-0.0305` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.7529` n `206` status `ready` deltaP `-2.4315` edge `-0.0019` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8363` n `206` status `ready` deltaP `4.7003` edge `0.0382` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8547` n `206` status `ready` deltaP `4.2556` edge `0.0373` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.0225` n `206` status `ready` deltaP `0.891` edge `0.0163` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0322` n `30` status `ready` deltaP `-9.2515` edge `-0.0192` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0709` n `206` status `ready` deltaP `0.6308` edge `0.0194` maxDD `-4.3608`
- `market_context_high->commodity_4h` score `-1.2086` n `206` status `ready` deltaP `-4.0359` edge `-0.0211` maxDD `-2.5555`
- `market_context_high->metal_4h` score `-1.2156` n `206` status `ready` deltaP `2.9615` edge `-0.0023` maxDD `-3.4996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
