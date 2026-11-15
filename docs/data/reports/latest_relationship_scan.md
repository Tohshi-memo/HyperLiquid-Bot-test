# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T18:37:27.585973+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8262`

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

- `market_context_high->unknown_24h` score `536.1429` n `64` status `ready` deltaP `3.9861` edge `44.652` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.5889` n `50` status `ready` deltaP `50.565` edge `3.5326` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.9063` n `64` status `ready` deltaP `46.94` edge `3.2501` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.8771` n `64` status `ready` deltaP `63.2366` edge `2.5092` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.2624` n `50` status `ready` deltaP `46.2149` edge `2.7886` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2607` n `50` status `ready` deltaP `39.0671` edge `0.8743` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4046` n `50` status `ready` deltaP `19.7366` edge `1.5247` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1797` n `64` status `ready` deltaP `49.5586` edge `0.3599` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.7564` n `64` status `ready` deltaP `63.9244` edge `0.5292` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.6061` n `50` status `ready` deltaP `43.5009` edge `0.2605` maxDD `0.0`
- `news_risk_high->index_24h` score `6.5855` n `50` status `ready` deltaP `42.2461` edge `0.2975` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.3951` n `50` status `ready` deltaP `22.9756` edge `0.434` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9466` n `50` status `ready` deltaP `44.8415` edge `0.1509` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7372` n `50` status `ready` deltaP `27.6037` edge `0.3543` maxDD `-9.4848`
- `market_context_high->crypto_major_24h` score `4.4883` n `64` status `ready` deltaP `13.2149` edge `1.2197` maxDD `-69.0352`
- `news_risk_high->equity_1h` score `4.0163` n `50` status `ready` deltaP `21.497` edge `0.2544` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6942` n `50` status `ready` deltaP `34.439` edge `0.1036` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5951` n `50` status `ready` deltaP `25.1037` edge `0.0839` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1861` n `50` status `ready` deltaP `24.994` edge `0.041` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2939` n `50` status `ready` deltaP `17.1976` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
