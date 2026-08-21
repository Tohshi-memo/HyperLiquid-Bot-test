# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T05:22:25.939810+00:00`
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

- `market_context_high->equity_1h` score `0.3161` n `105` status `ready` deltaP `8.4203` edge `0.0517` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3083` n `105` status `ready` deltaP `10.2581` edge `0.006` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0921` n `105` status `ready` deltaP `8.0952` edge `0.0081` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0253` n `105` status `ready` deltaP `4.2828` edge `0.1365` maxDD `-8.3685`
- `market_context_high->commodity_24h` score `-0.1659` n `96` status `ready` deltaP `4.6875` edge `0.1308` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2507` n `105` status `ready` deltaP `6.5302` edge `-0.0181` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.3048` n `105` status `ready` deltaP `2.3396` edge `-0.0023` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.3058` n `105` status `ready` deltaP `5.4283` edge `0.017` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4158` n `105` status `ready` deltaP `7.6305` edge `-0.0628` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6789` n `105` status `ready` deltaP `-1.8902` edge `0.0106` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7332` n `105` status `ready` deltaP `-0.9951` edge `-0.0072` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.7588` n `105` status `ready` deltaP `-5.8782` edge `-0.0015` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.8666` n `105` status `ready` deltaP `-0.1098` edge `-0.0259` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.3911` n `105` status `ready` deltaP `1.385` edge `-0.0815` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.8318` n `105` status `ready` deltaP `3.4814` edge `-0.1571` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5866` n `96` status `ready` deltaP `1.0416` edge `-0.05` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.5891` n `96` status `ready` deltaP `-18.4027` edge `-0.0181` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9564` n `96` status `ready` deltaP `-21.0069` edge `-0.1646` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.3288` n `96` status `ready` deltaP `11.9791` edge `-0.4733` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
