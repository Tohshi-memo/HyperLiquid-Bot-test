# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T13:07:25.771378+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11565`

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

- `risk_on_high->unknown_4h` score `36.0246` n `133` status `ready` deltaP `12.657` edge `2.9795` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.0246` n `133` status `ready` deltaP `12.657` edge `2.9795` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `29.4029` n `164` status `ready` deltaP `13.8719` edge `2.4273` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.2603` n `133` status `ready` deltaP `1.9404` edge `1.6498` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.2603` n `133` status `ready` deltaP `1.9404` edge `1.6498` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.7805` n `167` status `ready` deltaP `2.3952` edge `1.2788` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.7709` n `127` status `ready` deltaP `22.7266` edge `0.5973` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `3.288` n `107` status `ready` deltaP `17.9728` edge `0.5687` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.288` n `107` status `ready` deltaP `17.9728` edge `0.5687` maxDD `-19.828`
- `news_risk_high->crypto_alt_24h` score `3.0896` n `65` status `ready` deltaP `21.3381` edge `0.5473` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `2.3686` n `65` status `ready` deltaP `17.3398` edge `0.6264` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6036` n `65` status `ready` deltaP `8.9289` edge `0.3928` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.4665` n `107` status `ready` deltaP `18.1318` edge `0.7575` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.4665` n `107` status `ready` deltaP `18.1318` edge `0.7575` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.1875` n `127` status `ready` deltaP `19.7875` edge `0.7702` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.333` n `127` status `ready` deltaP `22.6214` edge `0.8383` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.2865` n `107` status `ready` deltaP `19.2952` edge `0.7825` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.2865` n `107` status `ready` deltaP `19.2952` edge `0.7825` maxDD `-56.9519`
- `news_risk_high->commodity_4h` score `0.2198` n `67` status `ready` deltaP `5.4901` edge `0.0275` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0229` n `133` status `ready` deltaP `10.9158` edge `0.0014` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
