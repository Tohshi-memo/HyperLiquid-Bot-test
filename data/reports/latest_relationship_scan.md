# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T11:52:35.202058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11584`

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

- `risk_on_high->unknown_4h` score `36.1846` n `133` status `ready` deltaP `12.9619` edge `2.9908` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.1846` n `133` status `ready` deltaP `12.9619` edge `2.9908` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.9217` n `164` status `ready` deltaP `12.9573` edge `2.3933` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.6742` n `133` status `ready` deltaP `2.5392` edge `1.6803` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.6742` n `133` status `ready` deltaP `2.5392` edge `1.6803` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.237` n `172` status `ready` deltaP `1.6606` edge `1.2384` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.5783` n `107` status `ready` deltaP `18.8409` edge `0.5871` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.5783` n `107` status `ready` deltaP `18.8409` edge `0.5871` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.4263` n `132` status `ready` deltaP `21.149` edge `0.5791` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.8318` n `63` status `ready` deltaP `21.1806` edge `0.5153` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.9853` n `63` status `ready` deltaP `16.4931` edge `0.5829` maxDD `-30.7329`
- `risk_on_high->crypto_alt_24h` score `1.6856` n `107` status `ready` deltaP `18.9999` edge `0.7798` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.6856` n `107` status `ready` deltaP `18.9999` edge `0.7798` maxDD `-42.8959`
- `news_risk_high->equity_24h` score `1.4528` n `63` status `ready` deltaP `8.2341` edge `0.3781` maxDD `-15.4056`
- `market_context_high->crypto_alt_24h` score `1.0243` n `132` status `ready` deltaP `18.1503` edge `0.7602` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.4688` n `107` status `ready` deltaP `19.816` edge `0.8024` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4688` n `107` status `ready` deltaP `19.816` edge `0.8024` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.4318` n `132` status `ready` deltaP `22.3011` edge `0.8531` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.241` n `67` status `ready` deltaP `5.6425` edge `0.0292` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.5146` edge `0.0033` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
