# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T23:22:36.950165+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_4h` score `45.6178` n `46` status `ready` deltaP `6.4024` edge `3.7588` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6559` n `46` status `ready` deltaP `13.5341` edge `2.3967` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2517` n `46` status `ready` deltaP `12.1453` edge `1.2834` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.2684` n `46` status `ready` deltaP `10.5903` edge `1.0351` maxDD `0.0`
- `market_context_high->index_24h` score `5.5035` n `46` status `ready` deltaP `19.6105` edge `0.3366` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9623` n `96` status `ready` deltaP `-9.2014` edge `1.1607` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.8658` n `96` status `ready` deltaP `36.8056` edge `0.278` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9085` n `96` status `ready` deltaP `14.1768` edge `0.2056` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.4965` n `96` status `ready` deltaP `9.7561` edge `0.2428` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9026` n `97` status `ready` deltaP `10.9205` edge `0.1253` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.823` n `46` status `ready` deltaP `21.7921` edge `0.02` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.3876` n `97` status `ready` deltaP `12.7169` edge `0.0702` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.384` n `96` status `ready` deltaP `20.5539` edge `0.0419` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.7645` n `96` status `ready` deltaP `22.5694` edge `0.1065` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.6624` n `46` status `ready` deltaP `19.6634` edge `-0.0525` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.6399` n `46` status `ready` deltaP `5.7147` edge `0.0395` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6229` n `97` status `ready` deltaP `15.0812` edge `0.0107` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6076` n `46` status `ready` deltaP `9.9063` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->crypto_alt_24h` score `0.3775` n `96` status `ready` deltaP `-9.2014` edge `0.5809` maxDD `-32.7147`
- `market_context_high->equity_4h` score `0.2649` n `46` status `ready` deltaP `3.2609` edge `0.031` maxDD `-0.4529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
