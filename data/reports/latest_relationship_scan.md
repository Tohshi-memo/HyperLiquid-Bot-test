# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T09:52:31.893254+00:00`
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

- `market_context_high->unknown_1h` score `66.0198` n `47` status `ready` deltaP `10.5651` edge `5.4383` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.6248` n `46` status `ready` deltaP `28.9855` edge `3.2911` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `27.0555` n `46` status `ready` deltaP `23.9583` edge `2.0949` maxDD `0.0`
- `market_context_high->equity_24h` score `24.1754` n `46` status `ready` deltaP `26.3814` edge `1.8488` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.9734` n `46` status `ready` deltaP `35.4091` edge `0.4371` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `7.8836` n `103` status `ready` deltaP `1.2945` edge `1.5526` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `4.7934` n `103` status `ready` deltaP `-1.2844` edge `1.1093` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.2498` n `46` status `ready` deltaP `29.3856` edge `0.0983` maxDD `-0.2042`
- `news_risk_high->crypto_alt_4h` score `3.0257` n `109` status `ready` deltaP `10.1463` edge `0.302` maxDD `-7.4001`
- `market_context_high->index_4h` score `2.9291` n `47` status `ready` deltaP `33.569` edge `0.0357` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.9173` n `109` status `ready` deltaP `15.0271` edge `0.2466` maxDD `-6.2941`
- `news_risk_high->crypto_alt_1h` score `2.4646` n `114` status `ready` deltaP `13.2472` edge `0.1661` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.3749` n `47` status `ready` deltaP `16.3823` edge `0.1305` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0781` n `114` status `ready` deltaP `15.343` edge `0.1144` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.684` n `109` status `ready` deltaP `24.4391` edge `0.041` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.5687` n `103` status `ready` deltaP `18.8865` edge `0.1227` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.2879` n `103` status `ready` deltaP `30.1847` edge `0.127` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9715` n `47` status `ready` deltaP `14.7598` edge `0.0104` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9307` n `47` status `ready` deltaP `11.167` edge `0.0434` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7792` n `103` status `ready` deltaP `21.2598` edge `0.103` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
