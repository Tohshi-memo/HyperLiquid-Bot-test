# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T06:37:28.271973+00:00`
- Price records: `672`
- Market context records: `6060`
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

- `news_risk_high->fx_24h` score `8.1282` n `30` status `ready` deltaP `72.7431` edge `0.1924` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3379` n `30` status `ready` deltaP `44.878` edge `0.0669` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `2.5523` n `30` status `ready` deltaP `28.0555` edge `0.0404` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.3232` n `30` status `ready` deltaP `27.8243` edge `0.022` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.6523` n `30` status `ready` deltaP `22.4306` edge `0.0087` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.3299` n `206` status `ready` deltaP `8.0319` edge `0.149` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.9931` n `30` status `ready` deltaP `11.3872` edge `0.0981` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3487` n `30` status `ready` deltaP `6.0679` edge `0.0504` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0922` n `30` status `ready` deltaP `9.2361` edge `0.0374` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5007` n `206` status `ready` deltaP `2.2324` edge `0.0008` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5091` n `206` status `ready` deltaP `0.6075` edge `-0.0008` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.5372` n `30` status `ready` deltaP `-0.2595` edge `-0.0305` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.7529` n `206` status `ready` deltaP `-2.4315` edge `-0.0019` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8246` n `206` status `ready` deltaP `4.85` edge `0.0387` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8579` n `206` status `ready` deltaP `4.2556` edge `0.0369` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.0004` n `206` status `ready` deltaP `1.1959` edge `0.0171` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0314` n `30` status `ready` deltaP `-9.2515` edge `-0.0191` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0709` n `206` status `ready` deltaP `0.6308` edge `0.0194` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.2156` n `206` status `ready` deltaP `2.9615` edge `-0.0023` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2425` n `206` status `ready` deltaP `-4.4933` edge `-0.0224` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
