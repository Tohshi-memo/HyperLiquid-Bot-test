# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T16:37:22.973707+00:00`
- Price records: `470`
- Market context records: `561`
- Flow alert records: `1584`
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

- `market_context_high->crypto_alt_24h` score `4.7819` n `140` status `ready` deltaP `7.5745` edge `0.3528` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0199` n `140` status `ready` deltaP `9.8778` edge `0.2192` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0139` n `146` status `ready` deltaP `9.7748` edge `0.0202` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3321` n `146` status `ready` deltaP `1.6545` edge `0.0042` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5272` n `146` status `ready` deltaP `2.0578` edge `0.0398` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6141` n `146` status `ready` deltaP `1.2186` edge `-0.0015` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1734` n `146` status `ready` deltaP `-1.1623` edge `-0.009` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2359` n `146` status `ready` deltaP `-4.1184` edge `-0.0152` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.355` n `146` status `ready` deltaP `4.2978` edge `-0.0101` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.9583` n `140` status `ready` deltaP `-6.0425` edge `0.0766` maxDD `-5.9609`
- `market_context_high->index_4h` score `-1.9968` n `146` status `ready` deltaP `1.7352` edge `-0.0257` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-2.012` n `146` status `ready` deltaP `3.3658` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.3106` n `146` status `ready` deltaP `2.3143` edge `0.049` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0109` n `146` status `ready` deltaP `-2.2648` edge `-0.0206` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3124` n `146` status `ready` deltaP `-4.771` edge `-0.0483` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.3422` n `146` status `ready` deltaP `9.583` edge `0.0282` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.5656` n `146` status `ready` deltaP `-5.9756` edge `0.0928` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.8736` n `140` status `ready` deltaP `-10.3089` edge `0.0064` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.3274` n `140` status `ready` deltaP `-5.1351` edge `-0.0376` maxDD `-18.3035`
- `market_context_high->unknown_4h` score `-5.1508` n `146` status `ready` deltaP `0.0422` edge `-0.2417` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
