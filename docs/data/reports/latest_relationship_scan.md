# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T16:52:35.208151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10024`

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

- `market_context_high->unknown_1h` score `87.4603` n `47` status `ready` deltaP `10.116` edge `7.228` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.6469` n `47` status `ready` deltaP `30.4226` edge `3.4737` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.2408` n `47` status `ready` deltaP `24.782` edge `2.3095` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.4374` n `47` status `ready` deltaP `29.2073` edge `1.8773` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8461` n `47` status `ready` deltaP `34.9364` edge `0.4339` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.4112` n `93` status `ready` deltaP `1.3217` edge `1.5892` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.7075` n `47` status `ready` deltaP `31.9334` edge `0.1199` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.3464` n `93` status `ready` deltaP `-1.0473` edge `1.1373` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.0896` n `47` status `ready` deltaP `35.2458` edge `0.0379` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.8405` n `116` status `ready` deltaP `13.5815` edge `0.1952` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.5975` n `47` status `ready` deltaP `17.7542` edge `0.1399` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.457` n `116` status `ready` deltaP `16.5394` edge `0.138` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `2.0453` n `112` status `ready` deltaP `15.6141` edge `0.2795` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `1.7781` n `112` status `ready` deltaP `8.101` edge `0.3393` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.5304` n `112` status `ready` deltaP `22.6698` edge `0.04` maxDD `-0.421`
- `news_risk_high->metal_24h` score `1.1763` n `93` status `ready` deltaP `25.2072` edge `0.1276` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.1448` n `93` status `ready` deltaP `28.1978` edge `0.1219` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.011` n `47` status `ready` deltaP `15.2089` edge `0.0107` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9139` n `47` status `ready` deltaP `11.167` edge `0.042` maxDD `-1.5564`
- `news_risk_high->commodity_24h` score `0.7649` n `93` status `ready` deltaP `14.6449` edge `0.084` maxDD `-2.431`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
