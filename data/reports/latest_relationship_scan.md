# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T04:07:25.940456+00:00`
- Price records: `672`
- Market context records: `6049`
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

- `news_risk_high->fx_24h` score `8.012` n `30` status `ready` deltaP `71.875` edge `0.1885` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2223` n `30` status `ready` deltaP `43.6585` edge `0.0654` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2837` n `30` status `ready` deltaP `27.3752` edge `0.0217` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `2.108` n `30` status `ready` deltaP `24.1667` edge `0.0351` maxDD `-0.3101`
- `news_risk_high->crypto_alt_24h` score `1.5734` n `30` status `ready` deltaP `26.3194` edge `-0.0296` maxDD `-0.5131`
- `market_context_high->equity_4h` score `1.3311` n `206` status `ready` deltaP `8.0319` edge `0.1491` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0289` n `30` status `ready` deltaP `11.5369` edge `0.1017` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.418` n `30` status `ready` deltaP `6.6667` edge `0.0553` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1195` n `30` status `ready` deltaP `9.2361` edge `0.0409` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.3307` n `189` status `ready` deltaP `26.1244` edge `0.5155` maxDD `-43.5652`
- `market_context_high->metal_1h` score `-0.4695` n `206` status `ready` deltaP `2.6815` edge `0.0018` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.506` n `30` status `ready` deltaP `0.1896` edge `-0.0295` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5486` n `206` status `ready` deltaP `0.1584` edge `-0.0011` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6894` n `206` status `ready` deltaP `-1.8327` edge `-0.0006` maxDD `-0.5708`
- `market_context_high->crypto_alt_1h` score `-0.7885` n `206` status `ready` deltaP `4.8544` edge `0.0418` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.7888` n `206` status `ready` deltaP `4.9997` edge `0.0423` maxDD `-9.807`
- `market_context_high->index_24h` score `-0.9885` n `189` status `ready` deltaP `2.9927` edge `0.0677` maxDD `-5.6021`
- `market_context_high->index_4h` score `-1.0366` n `206` status `ready` deltaP `0.891` edge `0.0145` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0384` n `30` status `ready` deltaP `-9.2515` edge `-0.02` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0925` n `206` status `ready` deltaP `0.6308` edge `0.0176` maxDD `-4.3608`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
