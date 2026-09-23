# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T09:52:27.933346+00:00`
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

- `market_context_high->unknown_4h` score `46.7956` n `46` status `ready` deltaP `7.7744` edge `3.8478` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4526` n `46` status `ready` deltaP `13.7078` edge `2.3786` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6357` n `46` status `ready` deltaP `12.1453` edge `1.3154` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.3108` n `46` status `ready` deltaP `10.5903` edge `0.9553` maxDD `0.0`
- `market_context_high->index_24h` score `5.632` n `46` status `ready` deltaP `20.8258` edge `0.3392` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.759` n `96` status `ready` deltaP `-9.0277` edge `1.1426` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.1236` n `96` status `ready` deltaP `33.3333` edge `0.2393` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9501` n `103` status `ready` deltaP `14.2316` edge `0.2087` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3091` n `103` status `ready` deltaP `9.0487` edge `0.2319` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.2706` n `46` status `ready` deltaP `26.5177` edge `0.0258` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8781` n `103` status `ready` deltaP `11.0618` edge `0.1318` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.602` n `103` status `ready` deltaP `14.0559` edge `0.0833` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2811` n `103` status `ready` deltaP `19.7179` edge `0.0389` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1006` n `96` status `ready` deltaP `27.0833` edge `0.1195` maxDD `-1.7159`
- `market_context_high->equity_4h` score `0.9166` n `46` status `ready` deltaP `7.0719` edge `0.0599` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8832` n `46` status `ready` deltaP `7.6608` edge `0.0468` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.7441` n `46` status `ready` deltaP `11.4033` edge `0.0113` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5595` n `103` status `ready` deltaP `14.3044` edge `0.0106` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2495` n `103` status `ready` deltaP `8.2568` edge `0.0101` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.1821` n `103` status `ready` deltaP `12.1359` edge `0.0382` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
