# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T00:07:25.795043+00:00`
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

- `news_risk_high->unknown_24h` score `55.123` n `38` status `ready` deltaP `17.1875` edge `4.479` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.8821` n `38` status `ready` deltaP `53.39` edge `1.2491` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0253` n `51` status `ready` deltaP `23.4965` edge `0.9334` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.9108` n `38` status `ready` deltaP `57.7576` edge `0.1993` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `6.144` n `38` status `ready` deltaP `28.125` edge `0.3245` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.8693` n `37` status `ready` deltaP `-9.7103` edge `0.6057` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8693` n `37` status `ready` deltaP `-9.7103` edge `0.6057` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0325` n `51` status `ready` deltaP `35.7963` edge `0.0275` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.9683` n `51` status `ready` deltaP `15.8858` edge `0.1719` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.8757` n `37` status `ready` deltaP `2.9458` edge `0.263` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8757` n `37` status `ready` deltaP `2.9458` edge `0.263` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.6138` n `51` status `ready` deltaP `22.6596` edge `0.1438` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4463` n `38` status `ready` deltaP `40.1042` edge `-0.0635` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.3187` n `37` status `ready` deltaP `30.3477` edge `-0.0003` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3187` n `37` status `ready` deltaP `30.3477` edge `-0.0003` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.6866` n `141` status `ready` deltaP `21.202` edge `0.0129` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.5137` n `153` status `ready` deltaP `9.3499` edge `0.1087` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.229` n `51` status `ready` deltaP `16.8457` edge `0.0071` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.03` n `37` status `ready` deltaP `13.3817` edge `0.0446` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.03` n `37` status `ready` deltaP `13.3817` edge `0.0446` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
