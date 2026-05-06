# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T16:22:15.524703+00:00`
- Price records: `469`
- Market context records: `560`
- Flow alert records: `1581`
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

- `market_context_high->crypto_alt_24h` score `4.8221` n `140` status `ready` deltaP `7.5967` edge `0.356` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0179` n `140` status `ready` deltaP `9.9273` edge `0.2187` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0071` n `146` status `ready` deltaP `9.8896` edge `0.0203` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3262` n `146` status `ready` deltaP `1.7517` edge `0.0043` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5363` n `146` status `ready` deltaP `1.9582` edge `0.0397` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6095` n `146` status `ready` deltaP `1.306` edge `-0.0015` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1632` n `146` status `ready` deltaP `-1.0801` edge `-0.0087` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2303` n `146` status `ready` deltaP `-4.0182` edge `-0.0154` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3433` n `146` status `ready` deltaP `4.3836` edge `-0.0097` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.9149` n `140` status `ready` deltaP `-5.9795` edge `0.0798` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.0044` n `146` status `ready` deltaP `3.46` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0177` n `146` status `ready` deltaP `1.5941` edge `-0.0265` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.3565` n `146` status `ready` deltaP `2.1606` edge `0.0462` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0289` n `146` status `ready` deltaP `-2.4148` edge `-0.0211` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3247` n `146` status `ready` deltaP `-4.8947` edge `-0.0485` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.406` n `146` status `ready` deltaP `9.4454` edge `0.0238` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.58` n `146` status `ready` deltaP `-6.0652` edge `0.0922` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.8235` n `140` status `ready` deltaP `-10.2671` edge `0.0103` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.3402` n `140` status `ready` deltaP `-5.2304` edge `-0.0386` maxDD `-18.3035`
- `market_context_high->unknown_4h` score `-4.9476` n `146` status `ready` deltaP `0.1224` edge `-0.2253` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
