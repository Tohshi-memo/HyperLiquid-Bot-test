# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T22:07:25.775807+00:00`
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

- `news_risk_high->unknown_24h` score `57.8194` n `30` status `ready` deltaP `17.1875` edge `4.7037` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.3069` n `30` status `ready` deltaP `51.2847` edge `1.2152` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0937` n `51` status `ready` deltaP `23.4965` edge `0.9391` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.7661` n `30` status `ready` deltaP `56.3541` edge `0.1966` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `5.508` n `30` status `ready` deltaP `28.125` edge `0.2715` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.9029` n `37` status `ready` deltaP `-9.4109` edge `0.608` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.9029` n `37` status `ready` deltaP `-9.4109` edge `0.608` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0253` n `51` status `ready` deltaP `35.7963` edge `0.0269` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0198` n `51` status `ready` deltaP `16.1852` edge `0.1742` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.8107` n `37` status `ready` deltaP `2.7934` edge `0.2586` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8107` n `37` status `ready` deltaP `2.7934` edge `0.2586` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.5488` n `51` status `ready` deltaP `22.5072` edge `0.1394` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4415` n `30` status `ready` deltaP `40.1042` edge `-0.0639` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.2569` n `37` status `ready` deltaP `29.8904` edge `-0.0024` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2569` n `37` status `ready` deltaP `29.8904` edge `-0.0024` maxDD `-0.0367`
- `market_context_high->unknown_1h` score `1.4428` n `149` status `ready` deltaP `8.3289` edge `0.1096` maxDD `-1.5916`
- `market_context_high->unknown_4h` score `1.3899` n `137` status `ready` deltaP `21.0777` edge `-0.011` maxDD `-0.0956`
- `news_risk_high->fx_1h` score `1.2302` n `51` status `ready` deltaP `16.8457` edge `0.0072` maxDD `-0.0257`
- `market_context_high->crypto_alt_4h` score `1.148` n `137` status `ready` deltaP `10.9644` edge `0.169` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.952` n `37` status `ready` deltaP `12.4671` edge `0.0442` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
