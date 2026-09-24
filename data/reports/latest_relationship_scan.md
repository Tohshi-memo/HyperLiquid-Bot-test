# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T10:07:37.894219+00:00`
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

- `market_context_high->unknown_1h` score `66.0126` n `47` status `ready` deltaP `10.5651` edge `5.4377` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.8247` n `46` status `ready` deltaP `29.1591` edge `3.3066` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `27.3094` n `46` status `ready` deltaP `24.1319` edge `2.1149` maxDD `0.0`
- `market_context_high->equity_24h` score `24.2805` n `46` status `ready` deltaP `26.555` edge `1.8564` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.0835` n `103` status `ready` deltaP `1.4681` edge `1.5681` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.0017` n `46` status `ready` deltaP `35.5828` edge `0.4383` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.0473` n `103` status `ready` deltaP `-1.1108` edge `1.1293` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.2901` n `46` status `ready` deltaP `29.5592` edge `0.1005` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.9461` n `47` status `ready` deltaP `33.7215` edge `0.0361` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.4945` n `114` status `ready` deltaP `13.3969` edge `0.1676` maxDD `-1.5895`
- `news_risk_high->crypto_major_4h` score `2.4382` n `110` status `ready` deltaP `14.4623` edge `0.2306` maxDD `-7.9065`
- `news_risk_high->crypto_alt_4h` score `2.4265` n `110` status `ready` deltaP `9.5898` edge `0.2828` maxDD `-9.2287`
- `market_context_high->equity_4h` score `2.4063` n `47` status `ready` deltaP `16.5347` edge `0.1321` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0913` n `114` status `ready` deltaP `15.343` edge `0.1155` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6953` n `110` status `ready` deltaP `24.5953` edge `0.0409` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.5368` n `103` status `ready` deltaP `18.7129` edge `0.1212` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.2902` n `103` status `ready` deltaP `30.1847` edge `0.1273` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9846` n `47` status `ready` deltaP `14.9095` edge `0.0105` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9451` n `47` status `ready` deltaP `11.3167` edge `0.0436` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8054` n `103` status `ready` deltaP `21.4334` edge `0.1052` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
