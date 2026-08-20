# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T06:37:29.466065+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10797`

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

- `market_context_high->equity_4h` score `1.8213` n `96` status `ready` deltaP `9.9339` edge `0.1744` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7756` n `96` status `ready` deltaP `14.8516` edge `0.0791` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.8791` n `96` status `ready` deltaP `15.3131` edge `0.0099` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.2714` n `96` status `ready` deltaP `11.5345` edge `0.0033` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.0874` n `96` status `ready` deltaP `6.4236` edge `0.1517` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0525` n `96` status `ready` deltaP `7.4949` edge `0.0199` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.01` n `96` status `ready` deltaP `7.19` edge `0.0036` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.1139` n `96` status `ready` deltaP `5.6138` edge `-0.0242` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1712` n `96` status `ready` deltaP `3.125` edge `0.0036` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3549` n `96` status `ready` deltaP `-1.7715` edge `0.0022` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.4701` n `96` status `ready` deltaP `17.7083` edge `-0.1066` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.7807` n `96` status `ready` deltaP `-2.7693` edge `0.0034` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.808` n `96` status `ready` deltaP `-0.0187` edge `-0.0233` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8743` n `96` status `ready` deltaP `1.7839` edge `-0.0395` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9297` n `96` status `ready` deltaP `-8.4893` edge `-0.006` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9248` n `96` status `ready` deltaP `4.5732` edge `-0.0639` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0022` n `96` status `ready` deltaP `7.3424` edge `-0.1137` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.2087` n `96` status `ready` deltaP `-15.9722` edge `-0.0026` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8162` n `96` status `ready` deltaP `-0.8681` edge `-0.0667` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.296` n `96` status `ready` deltaP `-15.9722` edge `-0.1135` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
