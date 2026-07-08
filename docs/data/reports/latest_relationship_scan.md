# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T08:22:26.287227+00:00`
- Price records: `672`
- Market context records: `6068`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11112`

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

- `news_risk_high->fx_24h` score `8.1522` n `30` status `ready` deltaP `72.7431` edge `0.1944` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.434` n `30` status `ready` deltaP `45.9451` edge `0.0678` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.3839` n `30` status `ready` deltaP `29.2708` edge `0.1016` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4207` n `32` status `ready` deltaP `29.0419` edge `0.022` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5269` n `206` status `ready` deltaP `9.0989` edge `0.1583` maxDD `-2.671`
- `news_risk_high->commodity_24h` score `1.3583` n `30` status `ready` deltaP `21.2153` edge `-0.0077` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.1606` n `32` status `ready` deltaP `13.6789` edge `0.1043` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5838` n `32` status `ready` deltaP `8.9259` edge `0.0615` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0766` n `30` status `ready` deltaP `9.2361` edge `0.0354` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4469` n `206` status `ready` deltaP `2.9809` edge `0.0027` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5462` n `206` status `ready` deltaP `0.1584` edge `-0.0009` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.7709` n `206` status `ready` deltaP `-2.4315` edge `-0.0034` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8262` n `206` status `ready` deltaP `4.85` edge `0.0385` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8329` n `206` status `ready` deltaP `4.4053` edge `0.0391` maxDD `-9.3536`
- `news_risk_high->metal_1h` score `-0.8432` n `32` status `ready` deltaP `-2.8443` edge `-0.0394` maxDD `-1.6464`
- `market_context_high->index_4h` score `-0.9192` n `206` status `ready` deltaP `2.2629` edge `0.0204` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0065` n `32` status `ready` deltaP `-8.1774` edge `-0.0182` maxDD `-1.1725`
- `market_context_high->equity_1h` score `-1.0397` n `206` status `ready` deltaP `0.9302` edge `0.02` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.0705` n `206` status `ready` deltaP `3.8761` edge `0.0037` maxDD `-3.4996`
- `market_context_high->index_1h` score `-1.2655` n `206` status `ready` deltaP `-2.6859` edge `0.0023` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
