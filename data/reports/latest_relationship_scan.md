# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T09:22:32.709349+00:00`
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

- `market_context_high->unknown_1h` score `65.997` n `47` status `ready` deltaP `10.4154` edge `5.4374` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.2574` n `46` status `ready` deltaP `28.6383` edge `3.2628` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `26.5825` n `46` status `ready` deltaP `23.6111` edge `2.0578` maxDD `0.0`
- `market_context_high->equity_24h` score `23.9604` n `46` status `ready` deltaP `26.0341` edge `1.8332` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.9145` n `46` status `ready` deltaP `35.0619` edge `0.4345` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `7.5162` n `103` status `ready` deltaP `0.9473` edge `1.5243` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `4.3204` n `103` status `ready` deltaP `-1.6316` edge `1.0722` maxDD `-49.7699`
- `news_risk_high->crypto_major_4h` score `3.8623` n `107` status `ready` deltaP `16.3494` edge `0.2792` maxDD `-3.3073`
- `news_risk_high->crypto_alt_4h` score `3.8082` n `107` status `ready` deltaP `11.4515` edge `0.3408` maxDD `-5.9838`
- `market_context_high->metal_24h` score `3.1716` n `46` status `ready` deltaP `29.0384` edge `0.0941` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.8915` n `47` status `ready` deltaP `33.2641` edge `0.0346` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.4454` n `114` status `ready` deltaP `13.2472` edge `0.1645` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.2845` n `47` status `ready` deltaP `16.0774` edge `0.125` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0685` n `114` status `ready` deltaP `15.343` edge `0.1136` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.66` n `107` status `ready` deltaP `24.1096` edge `0.0412` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.6348` n `103` status `ready` deltaP `19.2337` edge `0.1259` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.2832` n `103` status `ready` deltaP `30.1847` edge `0.1264` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9463` n `47` status `ready` deltaP `14.4604` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9019` n `47` status `ready` deltaP `10.8676` edge `0.043` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7284` n `103` status `ready` deltaP `20.9126` edge `0.0988` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
