# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T05:22:29.776419+00:00`
- Price records: `672`
- Market context records: `6055`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11127`

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

- `news_risk_high->fx_24h` score `8.0729` n `30` status `ready` deltaP `72.3958` edge `0.1901` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2661` n `30` status `ready` deltaP `44.1159` edge `0.066` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2837` n `30` status `ready` deltaP `27.3752` edge `0.0217` maxDD `-0.1113`
- `news_risk_high->crypto_alt_24h` score `2.0304` n `30` status `ready` deltaP `27.1875` edge `0.0027` maxDD `-0.5131`
- `news_risk_high->commodity_24h` score `1.873` n `30` status `ready` deltaP `23.2986` edge `0.0213` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.2863` n `206` status `ready` deltaP `7.727` edge `0.1474` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0087` n `30` status `ready` deltaP `11.3872` edge `0.1001` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3876` n `30` status `ready` deltaP `6.3673` edge `0.0534` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1031` n `30` status `ready` deltaP `9.2361` edge `0.0388` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.489` n `206` status `ready` deltaP `2.3821` edge `0.0013` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.5255` n `30` status `ready` deltaP `-0.1098` edge `-0.03` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5486` n `206` status `ready` deltaP `0.1584` edge `-0.0011` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.723` n `206` status `ready` deltaP `-2.1321` edge `-0.0014` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.809` n `206` status `ready` deltaP `4.85` edge `0.0407` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8189` n `206` status `ready` deltaP `4.555` edge `0.0399` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.028` n `206` status `ready` deltaP `0.891` edge `0.0156` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0322` n `30` status `ready` deltaP `-9.2515` edge `-0.0192` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0685` n `206` status `ready` deltaP `0.6308` edge `0.0196` maxDD `-4.3608`
- `market_context_high->commodity_4h` score `-1.1834` n `206` status `ready` deltaP `-3.7311` edge `-0.0199` maxDD `-2.5555`
- `market_context_high->metal_4h` score `-1.2048` n `206` status `ready` deltaP `2.9615` edge `-0.0014` maxDD `-3.4996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
