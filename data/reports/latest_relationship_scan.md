# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T04:52:33.412593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9666`

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

- `market_context_high->unknown_4h` score `33.7469` n `119` status `ready` deltaP `-7.066` edge `2.9299` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.0996` n `54` status `ready` deltaP `25.1158` edge `0.5768` maxDD `-2.2085`
- `market_context_high->crypto_major_24h` score `6.6394` n `54` status `ready` deltaP `8.7963` edge `1.0825` maxDD `-15.8614`
- `market_context_high->index_24h` score `5.7557` n `54` status `ready` deltaP `49.0741` edge `0.1568` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.5425` n `45` status `ready` deltaP `33.2012` edge `0.3258` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.5425` n `45` status `ready` deltaP `33.2012` edge `0.3258` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.4898` n `45` status `ready` deltaP `20.3727` edge `0.2831` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.4898` n `45` status `ready` deltaP `20.3727` edge `0.2831` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `2.7907` n `45` status `ready` deltaP `25.6437` edge `0.0848` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.7907` n `45` status `ready` deltaP `25.6437` edge `0.0848` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.4601` n `57` status `ready` deltaP `9.2657` edge `0.1196` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.4601` n `57` status `ready` deltaP `9.2657` edge `0.1196` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.1549` n `57` status `ready` deltaP `9.3497` edge `0.0992` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.1549` n `57` status `ready` deltaP `9.3497` edge `0.0992` maxDD `-3.2233`
- `market_context_high->crypto_major_4h` score `0.7324` n `119` status `ready` deltaP `10.3441` edge `0.2355` maxDD `-11.1784`
- `market_context_high->metal_4h` score `0.6029` n `119` status `ready` deltaP `13.4121` edge `0.0331` maxDD `-1.1153`
- `risk_on_high->metal_1h` score `0.5099` n `57` status `ready` deltaP `9.3077` edge `0.0173` maxDD `-0.2823`
- `risk_on_and_context->metal_1h` score `0.5099` n `57` status `ready` deltaP `9.3077` edge `0.0173` maxDD `-0.2823`
- `market_context_high->crypto_alt_1h` score `0.4162` n `131` status `ready` deltaP `5.6498` edge `0.0921` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.2392` n `119` status `ready` deltaP `4.481` edge `0.2459` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
