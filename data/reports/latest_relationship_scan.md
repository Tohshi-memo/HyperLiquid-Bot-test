# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T13:52:33.483717+00:00`
- Price records: `672`
- Market context records: `5987`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.4539` n `30` status `ready` deltaP `68.2292` edge `0.1663` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.5677` n `30` status `ready` deltaP `34.0625` edge `0.1741` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1141` n `30` status `ready` deltaP `42.5915` edge `0.0635` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2023` n `30` status `ready` deltaP `26.477` edge `0.0209` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0207` n `234` status `ready` deltaP `7.605` edge `0.1438` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.799` n `30` status `ready` deltaP `9.8902` edge `0.0832` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1756` n `30` status `ready` deltaP `5.1697` edge `0.0342` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0657` n `30` status `ready` deltaP `9.2361` edge `0.034` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4196` n `30` status `ready` deltaP `1.3872` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4381` n `234` status `ready` deltaP `-1.0889` edge `0.0029` maxDD `-1.1447`
- `market_context_high->equity_1h` score `-0.5005` n `234` status `ready` deltaP `3.2666` edge `0.0269` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5768` n `234` status `ready` deltaP `1.4727` edge `-0.0039` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.7592` n `234` status `ready` deltaP `-1.5572` edge `-0.0012` maxDD `-0.8015`
- `market_context_high->equity_24h` score `-0.9115` n `207` status `ready` deltaP `21.724` edge `0.316` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.068` n `30` status `ready` deltaP `-9.8503` edge `-0.0198` maxDD `-1.1161`
- `market_context_high->index_1h` score `-1.1556` n `234` status `ready` deltaP `-1.1324` edge `0.0026` maxDD `-1.3078`
- `market_context_high->crypto_major_1h` score `-1.1799` n `234` status `ready` deltaP `2.1125` edge `0.0114` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.1823` n `234` status `ready` deltaP `0.3075` edge `0.0151` maxDD `-3.165`
- `market_context_high->commodity_4h` score `-1.2506` n `234` status `ready` deltaP `-0.4652` edge `-0.0021` maxDD `-5.0774`
- `market_context_high->crypto_alt_1h` score `-1.2709` n `234` status `ready` deltaP `1.0671` edge `0.0052` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
