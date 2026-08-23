# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T23:37:27.197808+00:00`
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

- `news_risk_high->unknown_24h` score `55.741` n `36` status `ready` deltaP `17.1875` edge `4.5305` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.7774` n `36` status `ready` deltaP `52.9514` edge `1.2433` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0385` n `51` status `ready` deltaP `23.4965` edge `0.9345` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.8826` n `36` status `ready` deltaP `57.4652` edge `0.1989` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `6.2952` n `36` status `ready` deltaP `28.125` edge `0.3371` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.9029` n `37` status `ready` deltaP `-9.4109` edge `0.608` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.9029` n `37` status `ready` deltaP `-9.4109` edge `0.608` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0313` n `51` status `ready` deltaP `35.7963` edge `0.0274` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0198` n `51` status `ready` deltaP `16.1852` edge `0.1742` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.8443` n `37` status `ready` deltaP `2.7934` edge `0.2614` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8443` n `37` status `ready` deltaP `2.7934` edge `0.2614` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.5824` n `51` status `ready` deltaP `22.5072` edge `0.1422` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.3947` n `36` status `ready` deltaP `40.1042` edge `-0.0678` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.3139` n `37` status `ready` deltaP `30.3477` edge `-0.0007` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3139` n `37` status `ready` deltaP `30.3477` edge `-0.0007` maxDD `-0.0367`
- `market_context_high->unknown_4h` score `1.6386` n `141` status `ready` deltaP `21.202` edge `0.0089` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.3418` n `153` status `ready` deltaP `8.3421` edge `0.1011` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.241` n `51` status `ready` deltaP `16.9954` edge `0.0071` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.0044` n `37` status `ready` deltaP `13.0768` edge `0.0445` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.0044` n `37` status `ready` deltaP `13.0768` edge `0.0445` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
