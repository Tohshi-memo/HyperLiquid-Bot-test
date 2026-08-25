# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T14:22:35.693446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `43.8364` n `51` status `ready` deltaP `3.125` edge `3.6322` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.7344` n `52` status `ready` deltaP `24.9648` edge `0.8998` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `8.848` n `51` status `ready` deltaP `33.8133` edge `0.605` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.3323` n `51` status `ready` deltaP `42.8717` edge `0.0904` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0842` n `53` status `ready` deltaP `16.162` edge `0.1848` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0457` n `52` status `ready` deltaP `36.0812` edge `0.0267` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.2419` n `133` status `ready` deltaP `21.2922` edge `0.0857` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `2.0556` n `52` status `ready` deltaP `21.8926` edge `0.1024` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1752` n `53` status `ready` deltaP `16.2185` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5533` n `53` status `ready` deltaP `14.7215` edge `0.0092` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3673` n `53` status `ready` deltaP `10.2277` edge `-0.0063` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.3554` n `52` status `ready` deltaP `9.1581` edge `0.0083` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.0666` n `133` status `ready` deltaP `11.7216` edge `-0.0277` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0386` n `53` status `ready` deltaP `4.4487` edge `0.0007` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3506` n `52` status `ready` deltaP `6.1797` edge `-0.0173` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3552` n `53` status `ready` deltaP `0.2853` edge `-0.0089` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4273` n `133` status `ready` deltaP `2.7982` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.519` n `51` status `ready` deltaP `22.692` edge `-0.1903` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7909` n `133` status `ready` deltaP `5.7893` edge `-0.0408` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.2023` n `133` status `ready` deltaP `-5.9216` edge `-0.0069` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
