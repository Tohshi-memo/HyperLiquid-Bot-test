# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T23:37:25.305852+00:00`
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

- `market_context_high->unknown_24h` score `909.2217` n `44` status `ready` deltaP `3.9861` edge `75.7419` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.7937` n `50` status `ready` deltaP `50.565` edge `3.633` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `45.6583` n `64` status `ready` deltaP `8.9939` edge `3.7449` maxDD `0.0`
- `market_context_high->equity_24h` score `37.6321` n `44` status `ready` deltaP `39.8377` edge `3.0246` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.4299` n `44` status `ready` deltaP `58.4213` edge `2.4207` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.9857` n `50` status `ready` deltaP `43.7886` edge `2.6411` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `13.4241` n `44` status `ready` deltaP `15.3341` edge `1.4619` maxDD `-30.9696`
- `news_risk_high->equity_4h` score `11.7008` n `50` status `ready` deltaP `36.628` edge `0.8439` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1813` n `50` status `ready` deltaP `20.6031` edge `1.4903` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5557` n `44` status `ready` deltaP `47.4279` edge `0.3221` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7523` n `50` status `ready` deltaP `42.2461` edge `0.3114` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.28` n `50` status `ready` deltaP `41.0745` edge `0.2495` maxDD `0.0`
- `market_context_high->metal_24h` score `5.3496` n `44` status `ready` deltaP `58.0353` edge `0.3881` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.907` n `50` status `ready` deltaP `43.9268` edge `0.1537` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3624` n `50` status `ready` deltaP `20.5366` edge `0.3642` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.025` n `50` status `ready` deltaP `25.3171` edge `0.3102` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.7442` n `50` status `ready` deltaP `19.8503` edge `0.2427` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6282` n `50` status `ready` deltaP `33.5244` edge `0.1042` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4042` n `50` status `ready` deltaP `23.122` edge `0.0812` maxDD `-0.7999`
- `market_context_high->fx_24h` score `2.3866` n `44` status `ready` deltaP `26.0438` edge `0.0694` maxDD `-0.5313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
