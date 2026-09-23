# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T12:37:31.987986+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_4h` score `47.7305` n `46` status `ready` deltaP `7.9268` edge `3.9247` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6994` n `46` status `ready` deltaP `14.2286` edge `2.3957` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.8385` n `46` status `ready` deltaP `12.1453` edge `1.3323` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.228` n `46` status `ready` deltaP `10.5903` edge `0.9484` maxDD `0.0`
- `market_context_high->index_24h` score `5.6747` n `46` status `ready` deltaP `20.9994` edge `0.3416` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.0059` n `96` status `ready` deltaP `-8.5069` edge `1.1597` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.6504` n `96` status `ready` deltaP `31.4236` edge `0.2126` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.0869` n `103` status `ready` deltaP `14.2316` edge `0.2201` maxDD `-2.619`
- `market_context_high->index_4h` score `2.4288` n `46` status `ready` deltaP `28.1945` edge `0.0278` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.2827` n `103` status `ready` deltaP `9.0487` edge `0.2297` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9609` n `103` status `ready` deltaP `11.511` edge `0.1357` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6703` n `103` status `ready` deltaP `14.505` edge `0.086` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2677` n `103` status `ready` deltaP `19.5655` edge `0.0388` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.2032` n `46` status `ready` deltaP `8.7487` edge `0.0726` maxDD `-0.4529`
- `news_risk_high->fx_24h` score `1.119` n `96` status `ready` deltaP `27.2569` edge `0.1207` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.9791` n `46` status `ready` deltaP `8.2596` edge `0.0508` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.8244` n `46` status `ready` deltaP `12.3015` edge `0.012` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.617` n `103` status `ready` deltaP `14.9032` edge `0.0114` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.2357` n `103` status `ready` deltaP `12.7457` edge `0.041` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.2244` n `103` status `ready` deltaP `7.9574` edge `0.01` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
