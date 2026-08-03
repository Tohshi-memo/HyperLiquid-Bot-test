# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T02:37:36.751482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4174.3498` n `52` status `ready` deltaP `22.6896` edge `347.7533` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.1855` n `40` status `ready` deltaP `51.4583` edge `0.8788` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.211` n `40` status `ready` deltaP `51.3194` edge `0.6049` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `3.5576` n `52` status `ready` deltaP `8.7946` edge `0.3142` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.459` n `52` status `ready` deltaP `14.1065` edge `0.0656` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.7205` n `43` status `ready` deltaP `9.586` edge `0.1131` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.5424` n `52` status `ready` deltaP `11.6322` edge `0.0271` maxDD `-0.8085`
- `market_context_high->fx_4h` score `0.424` n `43` status `ready` deltaP `17.6652` edge `0.0162` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.3767` n `47` status `ready` deltaP `7.7143` edge `0.0343` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.3745` n `43` status `ready` deltaP `6.0408` edge `0.0983` maxDD `-4.9116`
- `news_risk_high->equity_1h` score `0.3012` n `52` status `ready` deltaP `6.8978` edge `0.0614` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.0001` n `47` status `ready` deltaP `7.1155` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->metal_1h` score `-0.0627` n `52` status `ready` deltaP `2.4989` edge `0.0073` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.1178` n `52` status `ready` deltaP `8.4076` edge `0.0246` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.1188` n `52` status `ready` deltaP `1.6007` edge `0.0064` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.199` n `52` status `ready` deltaP `1.7964` edge `0.0037` maxDD `-0.2475`
- `news_risk_high->crypto_major_1h` score `-0.234` n `52` status `ready` deltaP `5.0438` edge `0.0084` maxDD `-3.762`
- `news_risk_high->crypto_alt_1h` score `-0.3151` n `52` status `ready` deltaP `2.971` edge `0.008` maxDD `-3.1233`
- `news_risk_high->commodity_1h` score `-0.4888` n `52` status `ready` deltaP `2.3952` edge `-0.0205` maxDD `-1.9837`
- `market_context_high->fx_24h` score `-0.7139` n `40` status `ready` deltaP `0.6597` edge `0.0341` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
