# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T03:07:21.814268+00:00`
- Price records: `512`
- Market context records: `607`
- Flow alert records: `1715`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.8458` n `146` status `ready` deltaP `7.0074` edge `0.3619` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.1343` n `146` status `ready` deltaP `12.2135` edge `0.2965` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0078` n `146` status `ready` deltaP `10.2517` edge `0.0178` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3246` n `146` status `ready` deltaP `1.889` edge `0.0036` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6017` n `146` status `ready` deltaP `1.5166` edge `0.0372` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6638` n `146` status `ready` deltaP `0.443` edge `-0.0027` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.0536` n `146` status `ready` deltaP `6.1159` edge `0.0029` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.0605` n `146` status `ready` deltaP `-3.4408` edge `-0.0051` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2013` n `146` status `ready` deltaP `-1.5411` edge `-0.0088` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6573` n `146` status `ready` deltaP `5.8488` edge `-0.0048` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6998` n `146` status `ready` deltaP `4.5791` edge `0.0848` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2378` n `146` status `ready` deltaP `0.0278` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4461` n `146` status `ready` deltaP `13.8533` edge `0.0744` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.5868` n `146` status `ready` deltaP `-7.2084` edge `0.032` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.204` n `146` status `ready` deltaP `-3.2242` edge `-0.0303` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.305` n `146` status `ready` deltaP `-4.5438` edge `-0.0492` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7686` n `146` status `ready` deltaP `-7.0136` edge `0.0828` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2834` n `146` status `ready` deltaP `-2.7863` edge `-0.0134` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6311` n `146` status `ready` deltaP `-10.8225` edge `-0.0533` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8653` n `146` status `ready` deltaP `1.6018` edge `-0.2283` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
