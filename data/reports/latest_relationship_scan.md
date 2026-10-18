# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T19:37:27.701761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9318`

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

- `market_context_high->crypto_major_4h` score `1.9137` n `113` status `ready` deltaP `20.729` edge `0.4476` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.8971` n `113` status `ready` deltaP `18.0808` edge `0.1227` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.6483` n `80` status `ready` deltaP `19.6848` edge `0.0859` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.6483` n `80` status `ready` deltaP `19.6848` edge `0.0859` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.5747` n `80` status `ready` deltaP `22.0122` edge `0.3032` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5747` n `80` status `ready` deltaP `22.0122` edge `0.3032` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.5612` n `113` status `ready` deltaP `6.7869` edge `0.1156` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1275` n `80` status `ready` deltaP `7.3574` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1275` n `80` status `ready` deltaP `7.3574` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.2055` n `80` status `ready` deltaP `11.1111` edge `0.0292` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2055` n `80` status `ready` deltaP `11.1111` edge `0.0292` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3847` n `113` status `ready` deltaP `1.4069` edge `0.0913` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.4618` n `80` status `ready` deltaP `-2.6502` edge `-0.0035` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.4618` n `80` status `ready` deltaP `-2.6502` edge `-0.0035` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.6075` n `113` status `ready` deltaP `3.3751` edge `0.0017` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.6564` n `80` status `ready` deltaP `1.3997` edge `0.0279` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6564` n `80` status `ready` deltaP `1.3997` edge `0.0279` maxDD `-4.6876`
- `risk_on_high->metal_1h` score `-0.6588` n `80` status `ready` deltaP `-2.2081` edge `0.0034` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.6588` n `80` status `ready` deltaP `-2.2081` edge `0.0034` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.6885` n `113` status `ready` deltaP `-5.0175` edge `-0.0027` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
