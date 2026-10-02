# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T19:07:27.937180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4890`

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

- `market_context_high->unknown_1h` score `364.1854` n `50` status `ready` deltaP `10.8743` edge `30.2812` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.3717` n `50` status `ready` deltaP `10.3659` edge `24.2952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9352` n `73` status `ready` deltaP `40.4895` edge `1.0789` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.6099` n `50` status `ready` deltaP `17.2292` edge `0.8563` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `8.9922` n `50` status `ready` deltaP `31.8264` edge `0.6788` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.8473` n `73` status `ready` deltaP `31.5377` edge `0.5755` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.3519` n `50` status `ready` deltaP `18.0` edge `0.563` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4553` n `50` status `ready` deltaP `16.189` edge `0.4756` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.2764` n `116` status `ready` deltaP `22.0511` edge `0.4271` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.2973` n `50` status `ready` deltaP `15.1018` edge `0.2404` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1343` n `50` status `ready` deltaP `14.5988` edge `0.2089` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7641` n `50` status `ready` deltaP `30.8598` edge `0.0381` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5095` n `116` status `ready` deltaP `22.0984` edge `0.1314` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.5773` n `50` status `ready` deltaP `7.7569` edge `0.3367` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5098` n `73` status `ready` deltaP `5.9908` edge `0.469` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4591` n `50` status `ready` deltaP `20.491` edge `0.0114` maxDD `-0.113`
- `news_risk_high->crypto_major_4h` score `1.3481` n `116` status `ready` deltaP `14.6552` edge `0.3061` maxDD `-10.477`
- `news_risk_high->metal_24h` score `1.348` n `73` status `ready` deltaP `13.009` edge `0.2135` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.1499` n `116` status `ready` deltaP `5.9984` edge `0.1119` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8139` n `50` status `ready` deltaP `17.5556` edge `0.0891` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
