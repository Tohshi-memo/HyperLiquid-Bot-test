# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T13:37:38.066662+00:00`
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

- `risk_on_high->unknown_4h` score `35.9154` n `133` status `ready` deltaP `12.657` edge `2.9704` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `35.9154` n `133` status `ready` deltaP `12.657` edge `2.9704` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `29.2255` n `166` status `ready` deltaP `14.1291` edge `2.4108` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.9664` n `133` status `ready` deltaP `1.7907` edge `1.6263` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.9664` n `133` status `ready` deltaP `1.7907` edge `1.6263` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.4866` n `167` status `ready` deltaP `2.2455` edge `1.2553` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.6591` n `127` status `ready` deltaP `22.3794` edge `0.5903` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.2569` n `66` status `ready` deltaP `21.4804` edge `0.5678` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `3.1762` n `107` status `ready` deltaP `17.6256` edge `0.5617` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.1762` n `107` status `ready` deltaP `17.6256` edge `0.5617` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.6489` n `66` status `ready` deltaP `17.6452` edge `0.6603` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6992` n `66` status `ready` deltaP `9.3277` edge `0.4024` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.3619` n `107` status `ready` deltaP `17.7846` edge `0.7464` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.3619` n `107` status `ready` deltaP `17.7846` edge `0.7464` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.0828` n `127` status `ready` deltaP `19.4403` edge `0.7591` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.2378` n `127` status `ready` deltaP `22.2741` edge `0.8284` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2222` n `67` status `ready` deltaP `5.4901` edge `0.0278` maxDD `-0.8733`
- `risk_on_high->crypto_major_24h` score `0.1913` n `107` status `ready` deltaP `18.9479` edge `0.7726` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.1913` n `107` status `ready` deltaP `18.9479` edge `0.7726` maxDD `-56.9519`
- `news_risk_high->fx_4h` score `0.0263` n `67` status `ready` deltaP `9.499` edge `0.0045` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
