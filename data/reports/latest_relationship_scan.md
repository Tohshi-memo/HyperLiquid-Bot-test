# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T20:07:29.071477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4876`

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

- `market_context_high->unknown_1h` score `365.6386` n `50` status `ready` deltaP `10.8743` edge `30.4023` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.8941` n `50` status `ready` deltaP `10.3659` edge `24.2554` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2476` n `73` status `ready` deltaP `41.1839` edge `1.1003` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.9222` n `50` status `ready` deltaP `17.9236` edge `0.8777` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.027` n `50` status `ready` deltaP `31.8264` edge `0.6817` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.7559` n `73` status `ready` deltaP `31.1905` edge `0.5702` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.5579` n `50` status `ready` deltaP `18.6098` edge `0.5761` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8209` n `50` status `ready` deltaP `16.7988` edge `0.502` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.6419` n `116` status `ready` deltaP `22.6609` edge `0.4535` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3944` n `50` status `ready` deltaP `15.5509` edge `0.2455` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1715` n `50` status `ready` deltaP `14.7485` edge `0.211` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7263` n `50` status `ready` deltaP `30.4024` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5253` n `116` status `ready` deltaP `22.2508` edge `0.1317` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `1.5324` n `73` status `ready` deltaP `5.9908` edge `0.4719` maxDD `-15.8971`
- `market_context_high->equity_24h` score `1.5179` n `50` status `ready` deltaP `7.4097` edge `0.3314` maxDD `-11.8957`
- `news_risk_high->crypto_major_4h` score `1.482` n `116` status `ready` deltaP `15.265` edge `0.3192` maxDD `-10.477`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3574` n `73` status `ready` deltaP `13.009` edge `0.2147` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.247` n `116` status `ready` deltaP `6.4475` edge `0.117` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8578` n `50` status `ready` deltaP `18.25` edge `0.0901` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
