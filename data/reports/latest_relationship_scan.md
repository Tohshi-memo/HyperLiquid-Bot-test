# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T11:07:26.749240+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.056` n `143` status `ready` deltaP `7.6526` edge `0.0597` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3223` n `133` status `ready` deltaP `18.9563` edge `-0.0556` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0702` n `133` status `ready` deltaP `7.4478` edge `0.0096` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0068` n `143` status `ready` deltaP `7.1438` edge `0.0046` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0406` n `143` status `ready` deltaP `3.8975` edge `0.0047` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2507` n `143` status `ready` deltaP `2.1482` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2804` n `133` status `ready` deltaP `6.4712` edge `-0.0175` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3442` n `143` status `ready` deltaP `4.4492` edge `0.0332` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.569` n `133` status `ready` deltaP `2.9262` edge `0.0111` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.649` n `133` status `ready` deltaP `-0.5513` edge `0.0055` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8162` n `143` status `ready` deltaP `-6.3419` edge `-0.0016` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4595` n `133` status `ready` deltaP `5.5749` edge `-0.0318` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6582` n `133` status `ready` deltaP `-0.2957` edge `0.0699` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.8498` n `117` status `ready` deltaP `-5.4487` edge `0.0655` maxDD `-4.666`
- `market_context_high->fx_24h` score `-2.0497` n `117` status `ready` deltaP `-2.4039` edge `0.0062` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.4204` n `143` status `ready` deltaP `-2.3878` edge `-0.0363` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4219` n `143` status `ready` deltaP `-4.5883` edge `-0.1087` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.3768` n `117` status `ready` deltaP `-7.2784` edge `-0.0474` maxDD `-19.8832`
- `market_context_high->crypto_major_4h` score `-4.9211` n `133` status `ready` deltaP `-0.7346` edge `-0.3031` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.3272` n `117` status `ready` deltaP `-23.1571` edge `-0.1978` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
