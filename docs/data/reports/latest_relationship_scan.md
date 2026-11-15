# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T23:52:28.458887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_24h` score `937.9593` n `43` status `ready` deltaP `3.9861` edge `78.1367` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.8561` n `50` status `ready` deltaP `50.565` edge `3.6382` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `45.4543` n `64` status `ready` deltaP `8.9939` edge `3.7279` maxDD `0.0`
- `market_context_high->equity_24h` score `37.0343` n `43` status `ready` deltaP `39.3092` edge `2.9783` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.8945` n `43` status `ready` deltaP `57.9984` edge `2.3789` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.9452` n `50` status `ready` deltaP `43.7886` edge `2.6359` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `12.8562` n `43` status `ready` deltaP `13.6956` edge `1.4255` maxDD `-30.9696`
- `news_risk_high->equity_4h` score `11.7068` n `50` status `ready` deltaP `36.628` edge `0.8444` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1821` n `50` status `ready` deltaP `20.6031` edge `1.4904` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.4566` n `43` status `ready` deltaP `47.2694` edge `0.3149` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7607` n `50` status `ready` deltaP `42.2461` edge `0.3121` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2764` n `50` status `ready` deltaP `41.0745` edge `0.2492` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2012` n `43` status `ready` deltaP `57.5068` edge `0.3726` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.9106` n `50` status `ready` deltaP `43.9268` edge `0.154` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3636` n `50` status `ready` deltaP `20.5366` edge `0.3643` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0442` n `50` status `ready` deltaP `25.3171` edge `0.3118` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.713` n `50` status `ready` deltaP `19.7006` edge `0.2411` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6342` n `50` status `ready` deltaP `33.5244` edge `0.1047` maxDD `-0.3611`
- `market_context_high->fx_24h` score `2.4948` n `43` status `ready` deltaP `26.9275` edge `0.0713` maxDD `-0.4333`
- `news_risk_high->index_4h` score `2.4042` n `50` status `ready` deltaP `23.122` edge `0.0812` maxDD `-0.7999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
