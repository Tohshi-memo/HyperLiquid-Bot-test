# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T05:02:58.933689+00:00`
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

- `market_context_high->equity_1h` score `0.3341` n `105` status `ready` deltaP `8.57` edge `0.0522` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3083` n `105` status `ready` deltaP `10.2581` edge `0.006` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0921` n `105` status `ready` deltaP `8.0952` edge `0.0081` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0313` n `105` status `ready` deltaP `4.2828` edge `0.137` maxDD `-8.3685`
- `market_context_high->commodity_24h` score `-0.1652` n `96` status `ready` deltaP `4.6875` edge `0.1309` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.206` n `105` status `ready` deltaP `0.7756` edge `0.0043` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2515` n `105` status `ready` deltaP `6.5302` edge `-0.0182` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3051` n `105` status `ready` deltaP `5.4283` edge `0.0171` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3204` n `105` status `ready` deltaP `2.1899` edge `-0.0026` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.417` n `105` status `ready` deltaP `7.6305` edge `-0.0629` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6907` n `105` status `ready` deltaP `-2.0427` edge `0.0101` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7215` n `105` status `ready` deltaP `-0.8454` edge `-0.0067` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.7681` n `105` status `ready` deltaP `-6.0279` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.8542` n `105` status `ready` deltaP `0.0399` edge `-0.0253` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.3513` n `105` status `ready` deltaP `1.5375` edge `-0.0792` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.7932` n `105` status `ready` deltaP `3.6339` edge `-0.1549` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5866` n `96` status `ready` deltaP `1.0416` edge `-0.05` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.6066` n `96` status `ready` deltaP `-18.5764` edge `-0.0184` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9549` n `96` status `ready` deltaP `-21.0069` edge `-0.1644` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.2736` n `96` status `ready` deltaP `11.9791` edge `-0.4687` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
