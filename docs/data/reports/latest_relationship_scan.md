# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T23:52:29.816257+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11523`

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

- `risk_on_high->unknown_4h` score `23.0367` n `133` status `ready` deltaP `10.5229` edge `1.9114` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `23.0367` n `133` status `ready` deltaP `10.5229` edge `1.9114` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `16.2716` n `167` status `ready` deltaP `12.1212` edge `1.3447` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.667` n `133` status `ready` deltaP `-0.0057` edge `1.28` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.667` n `133` status `ready` deltaP `-0.0057` edge `1.28` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.1872` n `167` status `ready` deltaP `0.4491` edge `0.909` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `0.3129` n `67` status `ready` deltaP `5.795` edge `0.0374` maxDD `-0.8733`
- `market_context_high->equity_24h` score `0.2433` n `127` status `ready` deltaP `15.2613` edge `0.3531` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.814` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.814` edge `0.0013` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.05` n `67` status `ready` deltaP `4.7748` edge `-0.0029` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0882` n `133` status `ready` deltaP `5.19` edge `-0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0882` n `133` status `ready` deltaP `5.19` edge `-0.0014` maxDD `-0.5605`
- `news_risk_high->fx_4h` score `-0.1124` n `67` status `ready` deltaP `7.9746` edge `0.0031` maxDD `-1.2507`
- `risk_on_high->fx_24h` score `-0.1267` n `107` status `ready` deltaP `25.7075` edge `0.0821` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.1267` n `107` status `ready` deltaP `25.7075` edge `0.0821` maxDD `-4.2453`
- `news_risk_high->commodity_24h` score `-0.1822` n `67` status `ready` deltaP `4.4517` edge `-0.0256` maxDD `-0.2074`
- `risk_on_high->crypto_alt_1h` score `-0.1922` n `133` status `ready` deltaP `4.6013` edge `0.055` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1922` n `133` status `ready` deltaP `4.6013` edge `0.055` maxDD `-5.4685`
- `news_risk_high->commodity_1h` score `-0.1993` n `67` status `ready` deltaP `4.1581` edge `0.0003` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
