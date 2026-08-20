# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T14:37:32.320738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10819`

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

- `market_context_high->equity_4h` score `0.5515` n `105` status `ready` deltaP `7.4841` edge `0.159` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.4971` n `105` status `ready` deltaP `9.4682` edge `0.0598` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3287` n `105` status `ready` deltaP `10.4078` edge `0.0067` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.19` n `105` status `ready` deltaP `12.1704` edge `0.0008` maxDD `-1.273`
- `market_context_high->fx_4h` score `-0.0035` n `105` status `ready` deltaP `6.5708` edge `0.006` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1107` n `105` status `ready` deltaP `3.9863` edge `0.0029` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.1491` n `96` status `ready` deltaP `3.6458` edge `0.1399` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2099` n `105` status `ready` deltaP `0.7756` edge `0.0038` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2546` n `105` status `ready` deltaP `6.0381` edge `0.0195` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3402` n `105` status `ready` deltaP `7.4808` edge `-0.0555` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.3747` n `105` status `ready` deltaP `2.2983` edge `0.0168` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5432` n `105` status `ready` deltaP `2.4351` edge `-0.0014` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7301` n `105` status `ready` deltaP `-2.5` edge `0.0081` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8086` n `105` status `ready` deltaP `-6.7764` edge `-0.0019` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.0392` n `105` status `ready` deltaP `5.6533` edge `0.0027` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.2628` n `105` status `ready` deltaP `7.7497` edge `-0.0548` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.4601` n `96` status `ready` deltaP `17.7083` edge `-0.1891` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5846` n `96` status `ready` deltaP `1.2152` edge `-0.0509` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.773` n `96` status `ready` deltaP `-21.1805` edge `-0.0149` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9299` n `96` status `ready` deltaP `-21.0069` edge `-0.1612` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
