# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T12:37:27.814230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11581`

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

- `risk_on_high->unknown_4h` score `36.1038` n `133` status `ready` deltaP `12.657` edge `2.9861` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.1038` n `133` status `ready` deltaP `12.657` edge `2.9861` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `29.1653` n `164` status `ready` deltaP `13.8719` edge `2.4075` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.5603` n `133` status `ready` deltaP `2.2398` edge `1.6728` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.5603` n `133` status `ready` deltaP `2.2398` edge `1.6728` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.6701` n `169` status `ready` deltaP `1.9151` edge `1.2728` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.6466` n `129` status `ready` deltaP `22.0728` edge `0.5913` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `3.413` n `107` status `ready` deltaP `18.32` edge `0.5768` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.413` n `107` status `ready` deltaP `18.32` edge `0.5768` maxDD `-19.828`
- `news_risk_high->crypto_alt_24h` score `3.1857` n `65` status `ready` deltaP `21.6854` edge `0.5573` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `2.4592` n `65` status `ready` deltaP `17.687` edge `0.6357` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6848` n `65` status `ready` deltaP `9.2761` edge `0.4009` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.5626` n `107` status `ready` deltaP `18.4791` edge `0.7675` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.5626` n `107` status `ready` deltaP `18.4791` edge `0.7675` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.114` n `129` status `ready` deltaP `19.1094` edge `0.7653` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.3771` n `107` status `ready` deltaP `19.6424` edge `0.7918` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.3771` n `107` status `ready` deltaP `19.6424` edge `0.7918` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.3485` n `129` status `ready` deltaP `22.0042` edge `0.8444` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2191` n `67` status `ready` deltaP `5.4901` edge `0.0274` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0385` n `133` status `ready` deltaP `11.0655` edge `0.0024` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
