# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T16:22:27.609470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8898`

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

- `market_context_high->unknown_4h` score `40.1602` n `91` status `ready` deltaP `-2.2246` edge `3.4154` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.6068` n `49` status `ready` deltaP `43.1402` edge `0.8463` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.3394` n `49` status `ready` deltaP `44.5464` edge `0.8214` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.5825` n `49` status `ready` deltaP `22.4595` edge `0.4921` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.3692` n `90` status `ready` deltaP `19.0426` edge `1.1152` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.7892` n `49` status `ready` deltaP `42.5606` edge `0.1987` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.1496` n `49` status `ready` deltaP `30.0989` edge `0.249` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.9141` n `90` status `ready` deltaP `21.7339` edge `0.3075` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.3101` n `49` status `ready` deltaP `43.5385` edge `0.0734` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1769` n `49` status `ready` deltaP `12.6115` edge `0.2162` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `3.166` n `49` status `ready` deltaP `33.8077` edge `0.0469` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.685` n `49` status `ready` deltaP `6.6388` edge `0.2112` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.3834` n `49` status `ready` deltaP `29.6866` edge `0.0147` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `1.4713` n `91` status `ready` deltaP `17.8588` edge `0.2026` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4617` n `90` status `ready` deltaP `24.0599` edge `0.1755` maxDD `-3.5466`
- `market_context_high->crypto_alt_24h` score `1.3754` n `90` status `ready` deltaP `10.7459` edge `0.6985` maxDD `-34.5048`
- `news_risk_high->metal_4h` score `1.1864` n `49` status `ready` deltaP `18.4482` edge `0.0707` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5721` n `91` status `ready` deltaP `16.4484` edge `0.0127` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5314` n `91` status `ready` deltaP `9.8408` edge `0.0029` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3535` n `91` status `ready` deltaP `11.0417` edge `0.0606` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
