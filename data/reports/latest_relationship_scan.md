# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T02:37:29.578497+00:00`
- Price records: `672`
- Market context records: `6043`
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

- `news_risk_high->fx_24h` score `7.994` n `30` status `ready` deltaP `71.875` edge `0.187` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2211` n `30` status `ready` deltaP `43.6585` edge `0.0653` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.3894` n `30` status `ready` deltaP `25.2084` edge `0.0516` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2969` n `30` status `ready` deltaP `27.5249` edge `0.0218` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5433` n `206` status `ready` deltaP `8.7941` edge `0.1617` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.9869` n `30` status `ready` deltaP `11.0878` edge `0.0993` maxDD `-2.0691`
- `news_risk_high->crypto_alt_24h` score `0.9441` n `30` status `ready` deltaP `25.2777` edge `-0.0751` maxDD `-0.5131`
- `market_context_high->equity_24h` score `0.8851` n `183` status `ready` deltaP `28.4836` edge `0.55` maxDD `-37.1134`
- `news_risk_high->crypto_alt_1h` score `0.3635` n `30` status `ready` deltaP `6.2176` edge `0.0513` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1351` n `30` status `ready` deltaP `9.2361` edge `0.0429` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4267` n `206` status `ready` deltaP `3.2803` edge `0.0033` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4632` n `30` status `ready` deltaP `0.7884` edge `-0.028` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.5193` n `183` status `ready` deltaP `4.5367` edge `0.0732` maxDD `-5.6021`
- `market_context_high->fx_1h` score `-0.5354` n `206` status `ready` deltaP `0.3081` edge `-0.001` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6763` n `206` status `ready` deltaP `-1.683` edge `-0.0005` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8308` n `206` status `ready` deltaP `4.5506` edge `0.0399` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8431` n `206` status `ready` deltaP `4.4053` edge `0.0378` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9781` n `206` status `ready` deltaP `1.8056` edge `0.0159` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-1.0243` n `206` status `ready` deltaP `4.3334` edge `0.0045` maxDD `-3.4996`
- `news_risk_high->index_1h` score `-1.054` n `30` status `ready` deltaP `-9.5509` edge `-0.02` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
