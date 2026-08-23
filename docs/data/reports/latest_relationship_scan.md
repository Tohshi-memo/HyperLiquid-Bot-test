# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T23:07:26.991828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `56.341` n `34` status `ready` deltaP `17.1875` edge `4.5805` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.575` n `34` status `ready` deltaP `52.4612` edge `1.2297` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0637` n `51` status `ready` deltaP `23.4965` edge `0.9366` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8348` n `34` status `ready` deltaP `57.1384` edge `0.1971` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `6.0984` n `34` status `ready` deltaP `28.125` edge `0.3207` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.9138` n `37` status `ready` deltaP `-9.2612` edge `0.6084` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.9138` n `37` status `ready` deltaP `-9.2612` edge `0.6084` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.0366` n `51` status `ready` deltaP `16.3349` edge `0.1746` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0301` n `51` status `ready` deltaP `35.7963` edge `0.0273` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `2.8299` n `37` status `ready` deltaP `2.7934` edge `0.2602` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8299` n `37` status `ready` deltaP `2.7934` edge `0.2602` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.568` n `51` status `ready` deltaP `22.5072` edge `0.141` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4055` n `34` status `ready` deltaP `40.1042` edge `-0.0669` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.2969` n `37` status `ready` deltaP `30.1953` edge `-0.0011` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2969` n `37` status `ready` deltaP `30.1953` edge `-0.0011` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.5438` n `141` status `ready` deltaP `21.202` edge `0.001` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.2859` n `153` status `ready` deltaP `7.8382` edge `0.0998` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.229` n `51` status `ready` deltaP `16.8457` edge `0.0071` maxDD `-0.0257`
- `market_context_high->crypto_alt_4h` score `1.0816` n `141` status `ready` deltaP `11.5442` edge `0.1596` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.991` n `37` status `ready` deltaP `12.9244` edge `0.0444` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
