# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T06:52:33.556067+00:00`
- Price records: `672`
- Market context records: `6061`
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

- `news_risk_high->fx_24h` score `8.1318` n `30` status `ready` deltaP `72.7431` edge `0.1927` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3525` n `30` status `ready` deltaP `45.0305` edge `0.0671` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `2.667` n `30` status `ready` deltaP `28.2291` edge `0.0488` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.3244` n `30` status `ready` deltaP `27.8243` edge `0.0221` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.6096` n `30` status `ready` deltaP `22.257` edge `0.0063` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.3517` n `206` status `ready` deltaP `8.1843` edge `0.1498` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0024` n `30` status `ready` deltaP `11.5369` edge `0.0983` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3487` n `30` status `ready` deltaP `6.0679` edge `0.0504` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0898` n `30` status `ready` deltaP `9.2361` edge `0.0371` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5007` n `206` status `ready` deltaP `2.2324` edge `0.0008` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5079` n `206` status `ready` deltaP `0.6075` edge `-0.0007` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.5372` n `30` status `ready` deltaP `-0.2595` edge `-0.0305` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.741` n `206` status `ready` deltaP `-2.2818` edge `-0.0019` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8153` n `206` status `ready` deltaP `4.9997` edge `0.0389` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8579` n `206` status `ready` deltaP `4.2556` edge `0.0369` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9902` n `206` status `ready` deltaP `1.3483` edge `0.0174` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0306` n `30` status `ready` deltaP `-9.2515` edge `-0.019` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0709` n `206` status `ready` deltaP `0.6308` edge `0.0194` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.2156` n `206` status `ready` deltaP `2.9615` edge `-0.0023` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2528` n `206` status `ready` deltaP `-4.6457` edge `-0.0227` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
