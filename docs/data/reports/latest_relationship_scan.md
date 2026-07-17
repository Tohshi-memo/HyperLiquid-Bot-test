# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T22:07:33.051224+00:00`
- Price records: `672`
- Market context records: `7073`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7313` n `178` status `ready` deltaP `17.7514` edge `0.0126` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1011` n `178` status `ready` deltaP `0.9352` edge `0.0412` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1465` n `178` status `ready` deltaP `4.5314` edge `0.0027` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3681` n `178` status `ready` deltaP `1.312` edge `0.0305` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.6182` n `178` status `ready` deltaP `3.4465` edge `0.033` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.6441` n `178` status `ready` deltaP `-0.6039` edge `-0.0041` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8469` n `178` status `ready` deltaP `-4.1176` edge `-0.0195` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-0.8621` n `178` status `ready` deltaP `-5.4604` edge `0.128` maxDD `-4.742`
- `market_context_high->metal_1h` score `-1.3432` n `178` status `ready` deltaP `-4.7619` edge `-0.0034` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.688` n `178` status `ready` deltaP `-8.1272` edge `-0.0462` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9028` n `178` status `ready` deltaP `4.1159` edge `-0.0291` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2389` n `178` status `ready` deltaP `2.5743` edge `-0.0343` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4555` n `178` status `ready` deltaP `-2.6315` edge `-0.0562` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0004` n `178` status `ready` deltaP `-0.1696` edge `-0.005` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1048` n `178` status `ready` deltaP `2.2952` edge `0.0151` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.6739` n `178` status `ready` deltaP `-1.5215` edge `-0.0133` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.6768` n `178` status `ready` deltaP `-0.5515` edge `-0.0044` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.5102` n `178` status `ready` deltaP `-17.1524` edge `0.0508` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9487` n `178` status `ready` deltaP `3.8504` edge `-0.1577` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.6289` n `178` status `ready` deltaP `-22.0778` edge `-0.1051` maxDD `-44.343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
