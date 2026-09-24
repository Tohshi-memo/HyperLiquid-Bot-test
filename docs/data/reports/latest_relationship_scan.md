# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T13:07:31.410828+00:00`
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

- `market_context_high->unknown_1h` score `99.5347` n `47` status `ready` deltaP `10.116` edge `8.2342` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.9725` n `46` status `ready` deltaP `31.2425` edge `3.4717` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `29.936` n `46` status `ready` deltaP `26.2153` edge `2.3199` maxDD `0.0`
- `market_context_high->equity_24h` score `25.2979` n `46` status `ready` deltaP `28.6383` edge `1.9273` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `10.2314` n `103` status `ready` deltaP `3.5515` edge `1.7332` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.2436` n `46` status `ready` deltaP `36.9716` edge `0.4492` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `7.6739` n `103` status `ready` deltaP `0.9726` edge `1.3343` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.6692` n `46` status `ready` deltaP `31.6426` edge `0.1182` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.0748` n `47` status `ready` deltaP `34.941` edge `0.0387` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6877` n `47` status `ready` deltaP `17.9067` edge `0.1464` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.3549` n `119` status `ready` deltaP `12.5963` edge `0.1613` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0236` n `119` status `ready` deltaP `14.8418` edge `0.1132` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6729` n `114` status `ready` deltaP `24.5561` edge `0.0393` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.3591` n `103` status `ready` deltaP `30.8792` edge `0.1315` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.3184` n `103` status `ready` deltaP `17.4976` edge `0.1111` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.0518` n `103` status `ready` deltaP `23.5168` edge `0.1229` maxDD `-7.2536`
- `market_context_high->index_1h` score `1.0038` n `47` status `ready` deltaP `15.0592` edge `0.0111` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9499` n `47` status `ready` deltaP `11.167` edge `0.045` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.8932` n `114` status `ready` deltaP `13.2435` edge `0.1993` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.7927` n `119` status `ready` deltaP `16.3186` edge `0.0166` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
