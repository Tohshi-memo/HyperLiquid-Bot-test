# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T10:52:29.209248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `65.9766` n `47` status `ready` deltaP `10.4154` edge `5.4357` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.4411` n `46` status `ready` deltaP `29.68` edge `3.3545` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `28.0674` n `46` status `ready` deltaP `24.6528` edge `2.1746` maxDD `0.0`
- `market_context_high->equity_24h` score `24.5861` n `46` status `ready` deltaP `27.0758` edge `1.8784` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.7` n `103` status `ready` deltaP `1.989` edge `1.616` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.0866` n `46` status `ready` deltaP `36.1036` edge `0.4419` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.8053` n `103` status `ready` deltaP `-0.5899` edge `1.189` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.4038` n `46` status `ready` deltaP `30.0801` edge `0.1065` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.9959` n `47` status `ready` deltaP `34.1788` edge `0.0372` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.5065` n `114` status `ready` deltaP `13.3969` edge `0.1686` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.5029` n `47` status `ready` deltaP `16.992` edge `0.1371` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0997` n `114` status `ready` deltaP `15.343` edge `0.1162` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7181` n `113` status `ready` deltaP `25.031` edge `0.0399` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.4471` n `103` status `ready` deltaP `18.1921` edge `0.1172` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.2965` n `103` status `ready` deltaP `30.1847` edge `0.1281` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9954` n `47` status `ready` deltaP `15.0592` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_major_4h` score `0.9372` n `113` status `ready` deltaP `12.844` edge `0.1886` maxDD `-12.6904`
- `market_context_high->equity_1h` score `0.8923` n `47` status `ready` deltaP `10.8676` edge `0.0422` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8793` n `103` status `ready` deltaP `21.9543` edge `0.1112` maxDD `-7.2536`
- `news_risk_high->metal_1h` score `0.7079` n `114` status `ready` deltaP `15.5741` edge `0.0145` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
