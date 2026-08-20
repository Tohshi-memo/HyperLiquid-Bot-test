# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T06:52:28.438723+00:00`
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

- `market_context_high->equity_4h` score `1.7948` n `96` status `ready` deltaP `9.7815` edge `0.1732` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7493` n `96` status `ready` deltaP `14.7019` edge `0.0779` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.8659` n `96` status `ready` deltaP `15.1634` edge `0.0098` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.2714` n `96` status `ready` deltaP `11.5345` edge `0.0033` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.085` n `96` status `ready` deltaP `6.4236` edge `0.1514` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0391` n `96` status `ready` deltaP `7.3424` edge `0.0198` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0107` n `96` status `ready` deltaP `7.19` edge `0.0037` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.1319` n `96` status `ready` deltaP `5.4641` edge `-0.0247` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1867` n `96` status `ready` deltaP `2.9753` edge `0.0033` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3463` n `96` status `ready` deltaP `-1.6218` edge `0.0023` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.4917` n `96` status `ready` deltaP `17.7083` edge `-0.1084` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.7918` n `96` status `ready` deltaP `-2.9217` edge `0.003` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8134` n `96` status `ready` deltaP `-0.0187` edge `-0.024` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8821` n `96` status `ready` deltaP `1.7839` edge `-0.0405` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9382` n `96` status `ready` deltaP `-8.639` edge `-0.0061` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9332` n `96` status `ready` deltaP `4.5732` edge `-0.0646` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0348` n `96` status `ready` deltaP `7.19` edge `-0.1154` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.2238` n `96` status `ready` deltaP `-16.1458` edge `-0.0027` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8162` n `96` status `ready` deltaP `-0.8681` edge `-0.0667` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.323` n `96` status `ready` deltaP `-16.1458` edge `-0.1158` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
