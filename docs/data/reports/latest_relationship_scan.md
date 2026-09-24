# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T01:37:28.942539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.2165` n `47` status `ready` deltaP `11.0142` edge `5.9517` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `36.0521` n `46` status `ready` deltaP `23.2564` edge `2.8649` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.9498` n `46` status `ready` deltaP `20.6522` edge `1.6182` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `20.1951` n `46` status `ready` deltaP `18.2292` edge `1.5614` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.2081` n `99` status `ready` deltaP `-1.6887` edge `1.4084` maxDD `-48.3841`
- `market_context_high->index_24h` score `7.0411` n `46` status `ready` deltaP `29.68` edge `0.3976` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9201` n `103` status `ready` deltaP `14.5365` edge `0.4129` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5584` n `103` status `ready` deltaP `17.2804` edge `0.3224` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `4.1337` n `99` status `ready` deltaP `-3.993` edge `0.8671` maxDD `-33.347`
- `news_risk_high->crypto_alt_1h` score `2.6085` n `103` status `ready` deltaP `13.7565` edge `0.1747` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.471` n `47` status `ready` deltaP `29.1483` edge `0.027` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4029` n `99` status `ready` deltaP `23.6743` edge `0.1603` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0445` n `103` status `ready` deltaP `15.8523` edge `0.1082` maxDD `-1.8141`
- `market_context_high->metal_24h` score `2.0031` n `46` status `ready` deltaP `23.6564` edge `0.0326` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6246` n `103` status `ready` deltaP `23.6814` edge `0.0411` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.4097` n `47` status `ready` deltaP `11.3518` edge `0.0836` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1509` n `99` status `ready` deltaP `28.3302` edge `0.1218` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7678` n `47` status `ready` deltaP `12.5143` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.647` n `103` status `ready` deltaP `15.3523` edge `0.0109` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5918` n `99` status `ready` deltaP `18.2765` edge `0.0658` maxDD `-4.6087`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
