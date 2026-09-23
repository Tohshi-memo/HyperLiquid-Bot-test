# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T05:37:26.629021+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9818`

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

- `market_context_high->unknown_4h` score `46.7765` n `46` status `ready` deltaP `7.9268` edge `3.8452` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.3655` n `46` status `ready` deltaP `13.5341` edge `2.3725` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6693` n `46` status `ready` deltaP `12.1453` edge `1.3182` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.4764` n `46` status `ready` deltaP `10.5903` edge `0.9691` maxDD `0.0`
- `market_context_high->index_24h` score `5.6524` n `46` status `ready` deltaP `20.8258` edge `0.3409` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.6719` n `96` status `ready` deltaP `-9.2014` edge `1.1365` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4682` n `96` status `ready` deltaP `34.8958` edge `0.2576` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6216` n `99` status `ready` deltaP `12.9158` edge `0.1901` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1611` n `46` status `ready` deltaP `25.2982` edge `0.0248` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.0098` n `99` status `ready` deltaP `8.0377` edge `0.2137` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8254` n `103` status `ready` deltaP `10.6127` edge `0.1304` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4017` n `103` status `ready` deltaP `12.8583` edge `0.0746` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3717` n `99` status `ready` deltaP `20.4007` edge `0.0419` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9823` n `96` status `ready` deltaP `25.3472` edge `0.1159` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7921` n `46` status `ready` deltaP `6.7626` edge `0.0452` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7531` n `46` status `ready` deltaP `5.8524` edge `0.0544` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6806` n `46` status `ready` deltaP `10.6548` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4182` n `103` status `ready` deltaP `12.8074` edge `0.0088` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.307` n `103` status `ready` deltaP `8.8556` edge `0.0109` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.2825` n `99` status `ready` deltaP `12.3599` edge `0.0369` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
