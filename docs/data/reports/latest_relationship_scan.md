# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T00:37:16.971986+00:00`
- Price records: `672`
- Market context records: `1067`
- Flow alert records: `4975`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.5136` n `170` status `ready` deltaP `34.5378` edge `1.1089` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.2372` n `170` status `ready` deltaP `11.8703` edge `0.4807` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.4058` n `170` status `ready` deltaP `13.1718` edge `0.329` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.8211` n `170` status `ready` deltaP `13.6838` edge `0.258` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.3572` n `170` status `ready` deltaP `-4.5027` edge `0.4765` maxDD `-6.3373`
- `market_context_high->equity_4h` score `0.762` n `172` status `ready` deltaP `4.7469` edge `0.1117` maxDD `-3.7208`
- `market_context_high->index_4h` score `0.2051` n `172` status `ready` deltaP `3.336` edge `0.065` maxDD `-2.2786`
- `market_context_high->fx_1h` score `-0.0407` n `172` status `ready` deltaP `6.0089` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.1197` n `172` status `ready` deltaP `8.2196` edge `0.0276` maxDD `-5.3898`
- `market_context_high->index_1h` score `-0.146` n `172` status `ready` deltaP `4.9644` edge `0.0168` maxDD `-1.9652`
- `market_context_high->equity_1h` score `-0.2573` n `172` status `ready` deltaP `1.4239` edge `0.0356` maxDD `-3.656`
- `market_context_high->metal_1h` score `-0.436` n `172` status `ready` deltaP `5.7722` edge `-0.0184` maxDD `-3.4119`
- `market_context_high->crypto_major_4h` score `-0.4669` n `172` status `ready` deltaP `9.8376` edge `0.1134` maxDD `-10.4317`
- `market_context_high->fx_4h` score `-0.696` n `172` status `ready` deltaP `1.2018` edge `0.0024` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-0.8336` n `172` status `ready` deltaP `2.4335` edge `0.0229` maxDD `-5.3538`
- `market_context_high->commodity_1h` score `-1.053` n `172` status `ready` deltaP `-1.6746` edge `0.0042` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.6132` n `172` status `ready` deltaP `3.5699` edge `0.0922` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.3124` n `172` status `ready` deltaP `1.5669` edge `-0.1115` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-2.7115` n `172` status `ready` deltaP `-8.1998` edge `0.0238` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.0474` n `170` status `ready` deltaP `5.6322` edge `-0.0206` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
