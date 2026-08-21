# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T04:37:25.355787+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->equity_1h` score `0.3628` n `105` status `ready` deltaP `8.8694` edge `0.0526` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3215` n `105` status `ready` deltaP `10.4078` edge `0.0061` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0826` n `105` status `ready` deltaP `7.9428` edge `0.0079` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0361` n `105` status `ready` deltaP `4.2828` edge `0.1374` maxDD `-8.3685`
- `market_context_high->commodity_24h` score `-0.1628` n `96` status `ready` deltaP `4.6875` edge `0.1312` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2068` n `105` status `ready` deltaP `0.7756` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2499` n `105` status `ready` deltaP `6.5302` edge `-0.018` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3043` n `105` status `ready` deltaP `5.4283` edge `0.0172` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3048` n `105` status `ready` deltaP `2.3396` edge `-0.0023` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.3918` n `105` status `ready` deltaP `7.7802` edge `-0.0618` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.6958` n `105` status `ready` deltaP `-0.546` edge `-0.0054` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7136` n `105` status `ready` deltaP `-2.3476` edge `0.0092` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.786` n `105` status `ready` deltaP `-6.3273` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.8324` n `105` status `ready` deltaP `0.3393` edge `-0.0245` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.2741` n `105` status `ready` deltaP `1.8423` edge `-0.0748` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.7197` n `105` status `ready` deltaP `3.9387` edge `-0.1508` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5882` n `96` status `ready` deltaP `1.0416` edge `-0.0502` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.6416` n `96` status `ready` deltaP `-18.9236` edge `-0.019` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9518` n `96` status `ready` deltaP `-21.0069` edge `-0.164` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.1494` n `96` status `ready` deltaP `12.1527` edge `-0.4595` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
