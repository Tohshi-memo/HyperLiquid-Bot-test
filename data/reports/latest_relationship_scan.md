# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T20:52:25.901215+00:00`
- Price records: `487`
- Market context records: `580`
- Flow alert records: `1637`
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

- `market_context_high->crypto_alt_24h` score `4.7327` n `146` status `ready` deltaP `7.2435` edge `0.3509` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0212` n `146` status `ready` deltaP `9.6836` edge `0.2206` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0563` n `146` status `ready` deltaP `11.11` edge `0.0203` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2938` n `146` status `ready` deltaP `2.3608` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5772` n `146` status `ready` deltaP `1.8074` edge `0.0373` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6994` n `146` status `ready` deltaP `-0.0014` edge `-0.0043` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1755` n `146` status `ready` deltaP `-4.3081` edge `-0.0089` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2871` n `146` status `ready` deltaP `4.7563` edge `-0.0075` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3254` n `146` status `ready` deltaP `-2.2979` edge `-0.0141` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.9372` n `146` status `ready` deltaP `3.8954` edge `-0.0151` maxDD `-11.4508`
- `market_context_high->index_24h` score `-2.0217` n `146` status `ready` deltaP `-5.86` edge `0.0701` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.1519` n `146` status `ready` deltaP `3.128` edge `0.0568` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2332` n `146` status `ready` deltaP `0.4004` edge `-0.0365` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9825` n `146` status `ready` deltaP `11.4082` edge `0.046` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.3044` n `146` status `ready` deltaP `-4.6102` edge `-0.0487` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.352` n `146` status `ready` deltaP `-3.454` edge `-0.0411` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.5449` n `146` status `ready` deltaP `-5.5821` edge `0.0919` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.9704` n `146` status `ready` deltaP `-9.9288` edge `-0.0042` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5493` n `146` status `ready` deltaP `-4.8246` edge `-0.0339` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0784` n `146` status `ready` deltaP `1.2782` edge `-0.2439` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
