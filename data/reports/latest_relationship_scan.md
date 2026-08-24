# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T03:22:29.159799+00:00`
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

- `news_risk_high->unknown_24h` score `52.2334` n `51` status `ready` deltaP `17.1875` edge `4.2382` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.4067` n `51` status `ready` deltaP `40.237` edge `1.0254` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9917` n `51` status `ready` deltaP `23.4965` edge `0.9306` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8408` n `51` status `ready` deltaP `48.9481` edge `0.1756` maxDD `-0.2147`
- `risk_on_high->unknown_1h` score `4.5128` n `32` status `ready` deltaP `-13.6415` edge `0.7144` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.5128` n `32` status `ready` deltaP `-13.6415` edge `0.7144` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.1713` n `51` status `ready` deltaP `37.3207` edge `0.0289` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.1215` n `51` status `ready` deltaP `24.6413` edge `0.1729` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `2.9167` n `51` status `ready` deltaP `15.5864` edge `0.1696` maxDD `-0.7693`
- `news_risk_high->crypto_alt_24h` score `2.3045` n `51` status `ready` deltaP `26.7361` edge `0.0138` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.1998` n `32` status `ready` deltaP `29.1159` edge `-0.002` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.1998` n `32` status `ready` deltaP `29.1159` edge `-0.002` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.0761` n `51` status `ready` deltaP `37.1017` edge `-0.0701` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `2.0644` n `145` status `ready` deltaP `21.3194` edge `0.0436` maxDD `-0.0956`
- `risk_on_high->equity_4h` score `1.9705` n `32` status `ready` deltaP `-1.8293` edge `0.2194` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.9705` n `32` status `ready` deltaP `-1.8293` edge `0.2194` maxDD `-0.773`
- `market_context_high->unknown_1h` score `1.6727` n `157` status `ready` deltaP `10.3036` edge `0.1156` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2817` n `51` status `ready` deltaP `17.4445` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8423` n `51` status `ready` deltaP `17.1451` edge `0.0301` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.7505` n `92` status `ready` deltaP `-0.6567` edge `0.1144` maxDD `-0.7984`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
