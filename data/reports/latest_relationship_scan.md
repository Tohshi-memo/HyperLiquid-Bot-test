# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T05:37:30.639321+00:00`
- Price records: `672`
- Market context records: `5115`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10328`

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

- `market_context_high->unknown_24h` score `22.8926` n `72` status `ready` deltaP `28.6458` edge `1.751` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.083` n `126` status `ready` deltaP `6.0498` edge `0.6974` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.516` n `114` status `ready` deltaP `20.483` edge `0.592` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.3471` n `114` status `ready` deltaP `15.5568` edge `0.5018` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4839` n `114` status `ready` deltaP `13.2301` edge `0.4595` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.7041` n `126` status `ready` deltaP `5.9144` edge `0.1154` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3853` n `126` status `ready` deltaP `7.5468` edge `0.0584` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.2907` n `126` status `ready` deltaP `6.8268` edge `0.1163` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1261` n `114` status `ready` deltaP `6.2153` edge `0.1386` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1042` n `126` status `ready` deltaP `6.7223` edge `0.02` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.0361` n `126` status `ready` deltaP `5.0613` edge `0.012` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.5287` n `114` status `ready` deltaP `3.0086` edge `0.0239` maxDD `-2.9391`
- `market_context_high->commodity_24h` score `-0.5382` n `72` status `ready` deltaP `12.5` edge `0.0681` maxDD `-11.3014`
- `market_context_high->metal_4h` score `-0.564` n `114` status `ready` deltaP `1.9389` edge `0.0558` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6347` n `126` status `ready` deltaP `-2.4713` edge `-0.0008` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.8099` n `126` status `ready` deltaP `1.3473` edge `-0.0007` maxDD `-2.062`
- `market_context_high->fx_4h` score `-0.9835` n `114` status `ready` deltaP `-3.0889` edge `0.0018` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.3864` n `72` status `ready` deltaP `-1.5625` edge `-0.0077` maxDD `-1.4601`
- `market_context_high->commodity_4h` score `-2.3084` n `114` status `ready` deltaP `0.7943` edge `-0.0267` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-3.3642` n `72` status `ready` deltaP `-3.8195` edge `0.0408` maxDD `-27.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
