# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T08:07:28.176980+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.2993` n `105` status `ready` deltaP `8.4203` edge `0.0503` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2951` n `105` status `ready` deltaP `10.1084` edge `0.0059` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.1087` n `105` status `ready` deltaP `4.7402` edge `0.1404` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.047` n `105` status `ready` deltaP `7.333` edge `0.0074` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2468` n `105` status `ready` deltaP `6.5302` edge `-0.0176` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.2472` n `103` status `ready` deltaP `5.9432` edge `0.1231` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.3012` n `105` status `ready` deltaP `5.4283` edge `0.0176` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3024` n `105` status `ready` deltaP `2.3396` edge `-0.0021` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4422` n `105` status `ready` deltaP `7.3311` edge `-0.063` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6859` n `105` status `ready` deltaP `-1.8902` edge `0.0097` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7533` n `105` status `ready` deltaP `-5.8782` edge `-0.0008` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8992` n `105` status `ready` deltaP `-2.3424` edge `-0.0195` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9976` n `105` status `ready` deltaP `-1.3074` edge `-0.0347` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.8778` n `105` status `ready` deltaP `-0.1394` edge `-0.1119` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.2022` n `105` status `ready` deltaP `1.957` edge `-0.1778` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3498` n `103` status `ready` deltaP `-15.8324` edge `-0.0145` maxDD `-2.0613`
- `market_context_high->index_24h` score `-3.981` n `103` status `ready` deltaP `-2.498` edge `-0.0435` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.1121` n `103` status `ready` deltaP `11.5881` edge `-0.3693` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4256` n `103` status `ready` deltaP `-17.6088` edge `-0.1192` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
