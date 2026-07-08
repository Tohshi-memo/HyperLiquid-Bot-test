# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T07:37:31.343539+00:00`
- Price records: `672`
- Market context records: `6065`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11108`

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

- `news_risk_high->fx_24h` score `8.145` n `30` status `ready` deltaP `72.7431` edge `0.1938` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3938` n `30` status `ready` deltaP `45.4878` edge `0.0675` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.0158` n `30` status `ready` deltaP `28.75` edge `0.0744` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.447` n `32` status `ready` deltaP `29.3413` edge `0.0222` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.484` n `30` status `ready` deltaP `21.7361` edge `-0.0007` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.4483` n `206` status `ready` deltaP `8.6416` edge `0.1548` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1528` n `32` status `ready` deltaP `13.6789` edge `0.1033` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5488` n `32` status `ready` deltaP `8.6265` edge `0.059` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0828` n `30` status `ready` deltaP `9.2361` edge `0.0362` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4687` n `206` status `ready` deltaP `2.6815` edge `0.0019` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5198` n `206` status `ready` deltaP `0.4578` edge `-0.0007` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.7422` n `206` status `ready` deltaP `-2.2818` edge `-0.002` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.834` n `206` status `ready` deltaP `4.85` edge `0.0375` maxDD `-9.807`
- `news_risk_high->metal_1h` score `-0.8651` n `32` status `ready` deltaP `-3.1437` edge `-0.0402` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.868` n `206` status `ready` deltaP `4.1059` edge `0.0366` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9531` n `206` status `ready` deltaP `1.8056` edge `0.0191` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0158` n `32` status `ready` deltaP `-8.3271` edge `-0.0184` maxDD `-1.1725`
- `market_context_high->equity_1h` score `-1.0505` n `206` status `ready` deltaP `0.7805` edge `0.0201` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.1442` n `206` status `ready` deltaP `3.4188` edge `0.0006` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2757` n `206` status `ready` deltaP `-4.9506` edge `-0.0236` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
