# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T14:52:37.410370+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `34.7274` n `133` status `ready` deltaP `12.657` edge `2.8714` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `34.7274` n `133` status `ready` deltaP `12.657` edge `2.8714` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.9624` n `167` status `ready` deltaP `14.2553` edge `2.3047` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.262` n `133` status `ready` deltaP `1.3416` edge `1.5706` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.262` n `133` status `ready` deltaP `1.3416` edge `1.5706` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.7822` n `167` status `ready` deltaP `1.7964` edge `1.1996` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.4025` n `127` status `ready` deltaP `21.5113` edge `0.5747` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.3355` n `67` status `ready` deltaP `21.0873` edge `0.5805` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.9196` n `107` status `ready` deltaP `16.7575` edge `0.5461` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.9196` n `107` status `ready` deltaP `16.7575` edge `0.5461` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.8844` n `67` status `ready` deltaP `17.584` edge `0.6909` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6964` n `67` status `ready` deltaP `9.1832` edge `0.403` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.0827` n `107` status `ready` deltaP `16.9166` edge `0.7164` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.0827` n `107` status `ready` deltaP `16.9166` edge `0.7164` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `0.8037` n `127` status `ready` deltaP `18.5723` edge `0.7291` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2577` n `67` status `ready` deltaP `5.9474` edge `0.0293` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0421` n `67` status `ready` deltaP `9.6514` edge `0.0048` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0416` n `133` status `ready` deltaP `11.2152` edge `0.0018` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0416` n `133` status `ready` deltaP `11.2152` edge `0.0018` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.0015` n `133` status `ready` deltaP `5.4995` edge `0.0649` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
