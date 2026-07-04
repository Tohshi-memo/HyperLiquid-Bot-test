# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T08:52:30.807841+00:00`
- Price records: `672`
- Market context records: `5646`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.6482` n `178` status `ready` deltaP `14.2322` edge `0.6337` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.1902` n `178` status `ready` deltaP `20.531` edge `0.0613` maxDD `-1.5856`
- `market_context_high->crypto_major_4h` score `0.63` n `237` status `ready` deltaP `9.9374` edge `0.2155` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4515` n `237` status `ready` deltaP `7.229` edge `0.1533` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1836` n `237` status `ready` deltaP `5.612` edge `0.1322` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.284` n `238` status `ready` deltaP `1.531` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3621` n `238` status `ready` deltaP `5.4773` edge `0.034` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5703` n `238` status `ready` deltaP `-0.8403` edge `0.0` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.618` n `238` status `ready` deltaP `1.4781` edge `0.0348` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6687` n `238` status `ready` deltaP `3.8733` edge `0.043` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9614` n `238` status `ready` deltaP `0.1837` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.046` n `238` status `ready` deltaP `-0.7825` edge `-0.0054` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3098` n `237` status `ready` deltaP `1.3706` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0221` n `237` status `ready` deltaP `-1.5366` edge `0.0089` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3061` n `178` status `ready` deltaP `10.3698` edge `0.0339` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0441` n `237` status `ready` deltaP `-14.5216` edge `-0.0551` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8068` n `237` status `ready` deltaP `-2.1875` edge `-0.0351` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.511` n `178` status `ready` deltaP `4.2018` edge `0.0501` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3186` n `178` status `ready` deltaP `-11.8485` edge `-0.2514` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.0915` n `178` status `ready` deltaP `-16.8851` edge `-0.1175` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
