# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T12:52:29.734902+00:00`
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

- `market_context_high->unknown_4h` score `47.9753` n `46` status `ready` deltaP `7.9268` edge `3.9451` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.7601` n `46` status `ready` deltaP `14.4022` edge `2.3996` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.8649` n `46` status `ready` deltaP `12.1453` edge `1.3345` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2508` n `46` status `ready` deltaP `10.5903` edge `0.9503` maxDD `0.0`
- `market_context_high->index_24h` score `5.6807` n `46` status `ready` deltaP `20.9994` edge `0.3421` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.0666` n `96` status `ready` deltaP `-8.3333` edge `1.1636` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.6042` n `96` status `ready` deltaP `31.25` edge `0.2099` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.0917` n `103` status `ready` deltaP `14.2316` edge `0.2205` maxDD `-2.619`
- `market_context_high->index_4h` score `2.4434` n `46` status `ready` deltaP `28.347` edge `0.028` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.2755` n `103` status `ready` deltaP `9.0487` edge `0.2291` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9776` n `103` status `ready` deltaP `11.6607` edge `0.1361` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6715` n `103` status `ready` deltaP `14.505` edge `0.0861` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2677` n `103` status `ready` deltaP `19.5655` edge `0.0388` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.2262` n `46` status `ready` deltaP `8.9011` edge `0.0735` maxDD `-0.4529`
- `news_risk_high->fx_24h` score `1.1288` n `96` status `ready` deltaP `27.4306` edge `0.1208` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.9839` n `46` status `ready` deltaP `8.2596` edge `0.0512` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.8364` n `46` status `ready` deltaP `12.4512` edge `0.012` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.617` n `103` status `ready` deltaP `14.9032` edge `0.0114` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.238` n `103` status `ready` deltaP `12.7457` edge `0.0413` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.2256` n `103` status `ready` deltaP `7.9574` edge `0.0101` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
