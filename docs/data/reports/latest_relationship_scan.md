# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T01:07:31.926617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8188` n `91` status `ready` deltaP `-3.5965` edge `3.3961` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.1376` n `49` status `ready` deltaP `43.4451` edge `0.8885` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6426` n `49` status `ready` deltaP `44.2416` edge `0.8487` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.9369` n `49` status `ready` deltaP `28.4052` edge `0.732` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.3678` n `90` status `ready` deltaP `21.9122` edge `1.3523` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.2685` n `90` status `ready` deltaP `27.6796` edge `0.5474` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8066` n `49` status `ready` deltaP `48.5269` edge `0.2437` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8591` n `49` status `ready` deltaP `32.233` edge `0.2939` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5429` n `49` status `ready` deltaP `45.3677` edge `0.0806` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.1719` n `90` status `ready` deltaP `13.6145` edge `0.9097` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.0654` n `49` status `ready` deltaP `12.0127` edge `0.2109` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.5771` n `49` status `ready` deltaP `6.04` edge `0.2062` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4146` n `49` status `ready` deltaP `29.8363` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.1489` n `49` status `ready` deltaP `29.194` edge `-0.0071` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6684` n `91` status `ready` deltaP `17.554` edge `0.2299` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.2447` n `90` status `ready` deltaP `21.5655` edge `0.1643` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1447` n `49` status `ready` deltaP `17.9909` edge `0.0684` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5137` n `91` status `ready` deltaP `15.8386` edge `0.0119` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.3889` n `91` status `ready` deltaP `8.1941` edge `0.002` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.281` n `91` status `ready` deltaP `10.4429` edge `0.0553` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
