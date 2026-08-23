# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T22:36:06.735986+00:00`
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

- `news_risk_high->unknown_24h` score `57.0886` n `32` status `ready` deltaP `17.1875` edge `4.6428` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.4301` n `32` status `ready` deltaP `51.9097` edge `1.2213` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0577` n `51` status `ready` deltaP `23.4965` edge `0.9361` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.7934` n `32` status `ready` deltaP `56.7708` edge `0.1961` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `5.904` n `32` status `ready` deltaP `28.125` edge `0.3045` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.9013` n `37` status `ready` deltaP `-9.4109` edge `0.6078` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.9013` n `37` status `ready` deltaP `-9.4109` edge `0.6078` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0277` n `51` status `ready` deltaP `35.7963` edge `0.0271` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0174` n `51` status `ready` deltaP `16.1852` edge `0.174` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.8155` n `37` status `ready` deltaP `2.7934` edge `0.259` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8155` n `37` status `ready` deltaP `2.7934` edge `0.259` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.5536` n `51` status `ready` deltaP `22.5072` edge `0.1398` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4415` n `32` status `ready` deltaP `40.1042` edge `-0.0639` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.2653` n `37` status `ready` deltaP `29.8904` edge `-0.0017` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2653` n `37` status `ready` deltaP `29.8904` edge `-0.0017` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.4573` n `139` status `ready` deltaP `21.1408` edge `-0.0058` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.3616` n `151` status `ready` deltaP `8.0045` edge `0.105` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.217` n `51` status `ready` deltaP `16.696` edge `0.0071` maxDD `-0.0257`
- `market_context_high->crypto_alt_4h` score `1.1115` n `139` status `ready` deltaP `11.2585` edge `0.164` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.9654` n `37` status `ready` deltaP `12.6195` edge `0.0443` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
