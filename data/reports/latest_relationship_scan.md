# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T12:07:28.860895+00:00`
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

- `risk_on_high->unknown_4h` score `36.1786` n `133` status `ready` deltaP `12.9619` edge `2.9903` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.1786` n `133` status `ready` deltaP `12.9619` edge `2.9903` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.9421` n `164` status `ready` deltaP `12.9573` edge `2.395` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.6382` n `133` status `ready` deltaP `2.5392` edge `1.6773` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.6382` n `133` status `ready` deltaP `2.5392` edge `1.6773` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.3452` n `171` status `ready` deltaP `1.4532` edge `1.2488` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.5236` n `107` status `ready` deltaP `18.6673` edge `0.5837` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.5236` n `107` status `ready` deltaP `18.6673` edge `0.5837` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.4936` n `131` status `ready` deltaP `21.4496` edge `0.5827` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.0542` n `64` status `ready` deltaP `21.5278` edge `0.5415` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `2.2648` n `64` status `ready` deltaP `17.1875` edge `0.6141` maxDD `-30.7329`
- `risk_on_high->crypto_alt_24h` score `1.6454` n `107` status `ready` deltaP `18.8263` edge `0.7758` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.6454` n `107` status `ready` deltaP `18.8263` edge `0.7758` maxDD `-42.8959`
- `news_risk_high->equity_24h` score `1.6067` n `64` status `ready` deltaP `8.8542` edge `0.3937` maxDD `-15.4056`
- `market_context_high->crypto_alt_24h` score `1.0445` n `131` status `ready` deltaP `18.4624` edge `0.7607` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.4431` n `107` status `ready` deltaP `19.816` edge `0.7991` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4431` n `107` status `ready` deltaP `19.816` edge `0.7991` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.3884` n `131` status `ready` deltaP `22.0062` edge `0.8495` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2253` n `67` status `ready` deltaP `5.4901` edge `0.0282` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0587` n `133` status `ready` deltaP `11.3649` edge `0.003` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
