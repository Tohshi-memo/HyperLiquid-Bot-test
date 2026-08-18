# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T12:07:28.957775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2599` n `84` status `ready` deltaP `7.8918` edge `0.2565` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5016` n `84` status `ready` deltaP `16.6254` edge `0.265` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0161` n `96` status `ready` deltaP `9.163` edge `0.054` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7845` n `96` status `ready` deltaP `14.8882` edge `0.0237` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.6774` n `96` status `ready` deltaP `9.1717` edge `0.0974` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6479` n `96` status `ready` deltaP `12.7682` edge `0.0076` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5292` n `96` status `ready` deltaP `9.2066` edge `0.0054` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.484` n `96` status `ready` deltaP `10.5183` edge `0.0972` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0237` n `96` status `ready` deltaP `2.4644` edge `0.076` maxDD `-2.5696`
- `market_context_high->unknown_24h` score `-0.0127` n `84` status `ready` deltaP `14.3105` edge `-0.0787` maxDD `-0.0875`
- `market_context_high->metal_1h` score `-0.0429` n `96` status `ready` deltaP `4.0232` edge `0.0083` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2163` n `96` status `ready` deltaP `3.379` edge `0.0` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.3725` n `96` status `ready` deltaP `4.0905` edge `0.01` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3745` n `96` status `ready` deltaP `2.0771` edge `0.0183` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4803` n `96` status `ready` deltaP `1.3348` edge `0.014` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5799` n `96` status `ready` deltaP `0.94` edge `0.0109` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8557` n `96` status `ready` deltaP `-7.142` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9154` n `84` status `ready` deltaP `-6.2886` edge `0.021` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.347` n `84` status `ready` deltaP `-14.133` edge `-0.1748` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
