# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T12:37:27.994635+00:00`
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

- `market_context_high->index_1h` score `0.4449` n `119` status `ready` deltaP `11.8276` edge `0.007` maxDD `-0.5685`
- `market_context_high->equity_1h` score `0.3625` n `119` status `ready` deltaP `8.7757` edge `0.0532` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.1985` n `107` status `ready` deltaP `9.9456` edge `0.0094` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0451` n `119` status `ready` deltaP `3.7815` edge `0.0049` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.1025` n `107` status `ready` deltaP `4.0802` edge `0.1272` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.3052` n `107` status `ready` deltaP `5.4849` edge `0.0167` maxDD `-1.7252`
- `market_context_high->metal_4h` score `-0.3142` n `107` status `ready` deltaP `5.6246` edge `-0.0202` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.4139` n `119` status `ready` deltaP `1.4442` edge `-0.0045` maxDD `-0.503`
- `market_context_high->commodity_24h` score `-0.442` n `105` status `ready` deltaP `4.5883` edge `0.1159` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5429` n `119` status `ready` deltaP `9.6262` edge `-0.0867` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6728` n `119` status `ready` deltaP `-4.5539` edge `0.0007` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7228` n `107` status `ready` deltaP `-2.2096` edge `0.0071` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.1102` n `119` status `ready` deltaP `-1.2982` edge `-0.0037` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.5742` n `119` status `ready` deltaP `-4.1287` edge `-0.0718` maxDD `-4.1996`
- `market_context_high->fx_24h` score `-3.0874` n `105` status `ready` deltaP `-13.1697` edge `-0.0085` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.4769` n `107` status `ready` deltaP `-1.3278` edge `-0.1539` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.134` n `105` status `ready` deltaP `-4.9008` edge `-0.0471` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.228` n `107` status `ready` deltaP `-1.2352` edge `-0.242` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.438` n `105` status `ready` deltaP `-16.7212` edge `-0.1267` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.7449` n `105` status `ready` deltaP `8.9881` edge `-0.4047` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
