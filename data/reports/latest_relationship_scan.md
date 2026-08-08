# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T22:22:31.092376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.9988` n `103` status `ready` deltaP `4.5729` edge `0.5254` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4434` n `103` status `ready` deltaP `12.2118` edge `0.1798` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6914` n `112` status `ready` deltaP `16.507` edge `0.0982` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9965` n `119` status `ready` deltaP `11.8855` edge `0.0381` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8783` n `103` status `ready` deltaP `22.2694` edge `0.0508` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4378` n `103` status `ready` deltaP `9.1002` edge `0.1486` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5046` n `119` status `ready` deltaP `1.8593` edge `-0.0049` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5792` n `119` status `ready` deltaP `-4.2784` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6152` n `119` status `ready` deltaP `-3.4041` edge `-0.0066` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6336` n `112` status `ready` deltaP `-1.2631` edge `-0.0123` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.6462` n `119` status `ready` deltaP `2.2808` edge `0.0138` maxDD `-4.6286`
- `market_context_high->fx_4h` score `-0.7013` n `112` status `ready` deltaP `3.223` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.145` n `112` status `ready` deltaP `-4.486` edge `-0.016` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0694` n `119` status `ready` deltaP `-12.049` edge `-0.0292` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2426` n `112` status `ready` deltaP `1.1324` edge `-0.0607` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.78` n `119` status `ready` deltaP `-9.2965` edge `-0.059` maxDD `-5.522`
- `market_context_high->crypto_major_24h` score `-3.7603` n `103` status `ready` deltaP `6.2197` edge `-0.1054` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.2766` n `103` status `ready` deltaP `-12.4461` edge `-0.1291` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7018` n `112` status `ready` deltaP `-12.9791` edge `-0.1401` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.4132` n `119` status `ready` deltaP `-5.5779` edge `-0.6192` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
