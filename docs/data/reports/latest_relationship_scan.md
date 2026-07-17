# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T22:52:33.157376+00:00`
- Price records: `672`
- Market context records: `7077`
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

- `market_context_high->fx_4h` score `0.7561` n `175` status `ready` deltaP `18.0018` edge `0.013` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0598` n `175` status `ready` deltaP `0.9119` edge `0.0448` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.0689` n `175` status `ready` deltaP `5.4559` edge `0.003` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4024` n `175` status `ready` deltaP `0.8024` edge `0.0295` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5096` n `175` status `ready` deltaP `0.1377` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6315` n `175` status `ready` deltaP `3.1155` edge `0.0335` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8729` n `175` status `ready` deltaP `-4.5723` edge `-0.0198` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-1.3175` n `175` status `ready` deltaP `-6.2631` edge `0.0954` maxDD `-4.742`
- `market_context_high->metal_1h` score `-1.364` n `175` status `ready` deltaP `-4.9778` edge `-0.0037` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6267` n `175` status `ready` deltaP `-8.1368` edge `-0.0466` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8983` n `175` status `ready` deltaP `4.3824` edge `-0.0303` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2005` n `175` status `ready` deltaP `3.3737` edge `-0.0347` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4699` n `175` status `ready` deltaP `-2.8115` edge `-0.0562` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0383` n `175` status `ready` deltaP `-0.6272` edge `-0.0068` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1078` n `175` status `ready` deltaP `2.3432` edge `0.0144` maxDD `-24.6094`
- `market_context_high->metal_4h` score `-3.7323` n `175` status `ready` deltaP `-1.1551` edge `-0.005` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.7489` n `175` status `ready` deltaP `-2.369` edge `-0.0139` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-4.7989` n `175` status `ready` deltaP `-18.1439` edge `0.0204` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9786` n `175` status `ready` deltaP `3.831` edge `-0.1614` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.5477` n `175` status `ready` deltaP `-22.4832` edge `-0.1093` maxDD `-44.2499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
