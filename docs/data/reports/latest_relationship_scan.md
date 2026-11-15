# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T23:07:30.636357+00:00`
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

- `market_context_high->unknown_24h` score `855.4173` n `46` status `ready` deltaP `3.9861` edge `71.2582` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.6713` n `50` status `ready` deltaP `50.565` edge `3.6228` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.7084` n `46` status `ready` deltaP `40.8259` edge `3.1077` maxDD `-9.0005`
- `market_context_high->unknown_4h` score `35.1571` n `66` status `ready` deltaP `8.9939` edge `2.8698` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `33.5383` n `46` status `ready` deltaP `59.2118` edge `2.5078` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.0942` n `50` status `ready` deltaP `43.7886` edge `2.655` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.4743` n `46` status `ready` deltaP `18.3973` edge `1.529` maxDD `-30.9696`
- `news_risk_high->equity_4h` score `11.6792` n `50` status `ready` deltaP `36.628` edge `0.8421` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2055` n `50` status `ready` deltaP `20.6031` edge `1.4934` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.7246` n `46` status `ready` deltaP `47.7244` edge `0.3342` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7367` n `50` status `ready` deltaP `42.2461` edge `0.3101` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2896` n `50` status `ready` deltaP `41.0745` edge `0.2503` maxDD `0.0`
- `market_context_high->metal_24h` score `5.6256` n `46` status `ready` deltaP `59.0235` edge `0.4169` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8962` n `50` status `ready` deltaP `43.9268` edge `0.1528` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3492` n `50` status `ready` deltaP `20.5366` edge `0.3631` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `3.9806` n `50` status `ready` deltaP `25.3171` edge `0.3065` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.755` n `50` status `ready` deltaP `19.8503` edge `0.2436` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6234` n `50` status `ready` deltaP `33.5244` edge `0.1038` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4018` n `50` status `ready` deltaP `23.122` edge `0.081` maxDD `-0.7999`
- `market_context_high->fx_24h` score `2.1713` n `46` status `ready` deltaP `24.4142` edge `0.0652` maxDD `-0.7618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
