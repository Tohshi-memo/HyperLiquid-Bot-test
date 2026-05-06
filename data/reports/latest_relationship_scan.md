# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T17:37:21.239620+00:00`
- Price records: `474`
- Market context records: `566`
- Flow alert records: `1596`
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

- `market_context_high->crypto_alt_24h` score `4.9021` n `143` status `ready` deltaP `7.5018` edge `0.3633` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9743` n `143` status `ready` deltaP `9.8624` edge `0.2155` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0039` n `146` status `ready` deltaP `9.9813` edge `0.0201` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3178` n `146` status `ready` deltaP `1.9137` edge `0.0043` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5676` n `146` status `ready` deltaP `1.8079` edge `0.0381` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6352` n `146` status `ready` deltaP `0.8731` edge `-0.0019` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1781` n `146` status `ready` deltaP `-3.8764` edge `-0.012` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2066` n `146` status `ready` deltaP `-1.4875` edge `-0.0096` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3894` n `146` status `ready` deltaP `3.9581` edge `-0.0107` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7923` n `143` status `ready` deltaP `-5.6766` edge `0.088` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9847` n `146` status `ready` deltaP `3.6316` edge `-0.0173` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0455` n `146` status `ready` deltaP `1.4121` edge `-0.0276` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2103` n `146` status `ready` deltaP `2.9222` edge `0.0533` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0699` n `146` status `ready` deltaP `-2.5526` edge `-0.0236` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.1882` n `146` status `ready` deltaP `10.1274` edge `0.0374` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2541` n `146` status `ready` deltaP `-4.2816` edge `-0.0467` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5617` n `146` status `ready` deltaP `-6.0618` edge `0.0937` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.6504` n `143` status `ready` deltaP `-9.9342` edge `0.0225` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.492` n `143` status `ready` deltaP `-5.3888` edge `-0.0405` maxDD `-19.6244`
- `market_context_high->unknown_4h` score `-5.3592` n `146` status `ready` deltaP `-0.0569` edge `-0.2584` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
