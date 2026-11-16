# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T00:07:29.333374+00:00`
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

- `market_context_high->unknown_24h` score `968.3505` n `42` status `ready` deltaP `3.9861` edge `80.6693` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.9113` n `50` status `ready` deltaP `50.565` edge `3.6428` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `45.2047` n `64` status `ready` deltaP `8.9939` edge `3.7071` maxDD `0.0`
- `market_context_high->equity_24h` score `36.5304` n `42` status `ready` deltaP `38.7555` edge `2.94` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.6226` n `42` status `ready` deltaP `57.5555` edge `2.3592` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.88` n `50` status `ready` deltaP `43.6153` edge `2.6287` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `12.7986` n `42` status `ready` deltaP `14.1867` edge `1.4118` maxDD `-30.5193`
- `news_risk_high->equity_4h` score `11.7044` n `50` status `ready` deltaP `36.628` edge `0.8442` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1665` n `50` status `ready` deltaP `20.6031` edge `1.4884` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.3845` n `42` status `ready` deltaP `47.1032` edge `0.31` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7679` n `50` status `ready` deltaP `42.2461` edge `0.3127` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2728` n `50` status `ready` deltaP `41.0745` edge `0.2489` maxDD `0.0`
- `market_context_high->metal_24h` score `5.0788` n `42` status `ready` deltaP `56.9531` edge `0.3606` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.9106` n `50` status `ready` deltaP `43.9268` edge `0.154` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3274` n `50` status `ready` deltaP `20.3841` edge `0.3623` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0406` n `50` status `ready` deltaP `25.3171` edge `0.3115` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.6842` n `50` status `ready` deltaP `19.5509` edge `0.2397` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6548` n `50` status `ready` deltaP `33.6768` edge `0.1054` maxDD `-0.3611`
- `market_context_high->fx_24h` score `2.6056` n `42` status `ready` deltaP `27.8616` edge `0.0731` maxDD `-0.3367`
- `news_risk_high->index_4h` score `2.403` n `50` status `ready` deltaP `23.122` edge `0.0811` maxDD `-0.7999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
