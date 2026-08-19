# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T14:22:36.131515+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11750`

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

- `market_context_high->equity_4h` score `2.1835` n `96` status `ready` deltaP `11.6107` edge `0.1934` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8848` n `96` status `ready` deltaP `15.151` edge `0.0862` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.5535` n `96` status `ready` deltaP `4.6875` edge `0.219` maxDD `-4.9964`
- `market_context_high->metal_4h` score `1.0342` n `96` status `ready` deltaP `16.8699` edge `0.0313` maxDD `-1.273`
- `market_context_high->index_1h` score `0.975` n `96` status `ready` deltaP `16.361` edge `0.0109` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.6313` n `96` status `ready` deltaP `9.5486` edge `0.2006` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `0.5886` n `96` status `ready` deltaP `9.1717` edge `0.09` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `0.3444` n `96` status `ready` deltaP `18.2291` edge `-0.0422` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `0.1545` n `96` status `ready` deltaP `7.8593` edge `-0.0168` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1428` n `96` status `ready` deltaP `9.3242` edge `0.0064` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1336` n `96` status `ready` deltaP `8.1046` edge `0.0226` maxDD `-0.5728`
- `market_context_high->metal_1h` score `0.0673` n `96` status `ready` deltaP `5.3705` edge `0.0085` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.2339` n `96` status `ready` deltaP `7.4695` edge `0.0577` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4601` n `96` status `ready` deltaP `2.5324` edge `0.0086` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.5039` n `96` status `ready` deltaP `1.3286` edge `0.0067` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6121` n `96` status `ready` deltaP `0.2795` edge `0.0047` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8892` n `96` status `ready` deltaP `-7.5911` edge `-0.0068` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.3427` n `96` status `ready` deltaP `-4.6875` edge `0.0617` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.7783` n `96` status `ready` deltaP `-21.0069` edge `-0.0165` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
