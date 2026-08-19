# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T18:22:38.238170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9828`

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

- `market_context_high->equity_4h` score `2.3291` n `96` status `ready` deltaP `11.9156` edge `0.2035` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.9627` n `96` status `ready` deltaP `15.8995` edge `0.0877` maxDD `-0.4112`
- `market_context_high->index_1h` score `1.0013` n `96` status `ready` deltaP `16.6604` edge `0.0111` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.6459` n `96` status `ready` deltaP `14.4309` edge `0.0152` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.3293` n `96` status `ready` deltaP `6.7708` edge `0.1804` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.2976` n `96` status `ready` deltaP `18.2291` edge `-0.0461` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.2078` n `96` status `ready` deltaP `8.8668` edge `0.0237` maxDD `-0.5728`
- `market_context_high->crypto_major_24h` score `0.1543` n `96` status `ready` deltaP `3.4722` edge `0.1105` maxDD `-4.9964`
- `market_context_high->unknown_1h` score `0.1317` n `96` status `ready` deltaP `7.5599` edge `-0.0167` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.0628` n `96` status `ready` deltaP `7.9522` edge `0.0053` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0334` n `96` status `ready` deltaP `4.4723` edge `0.0061` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.6372` n `96` status `ready` deltaP `2.3827` edge `-0.0131` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.6404` n `96` status `ready` deltaP `0.7298` edge `-0.0068` maxDD `-2.413`
- `market_context_high->crypto_major_4h` score `-0.6544` n `96` status `ready` deltaP `7.4949` edge `-0.0024` maxDD `-3.1677`
- `market_context_high->commodity_4h` score `-0.6957` n `96` status `ready` deltaP `-0.94` edge `0.0021` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8799` n `96` status `ready` deltaP `-7.4414` edge `-0.0066` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.1199` n `96` status `ready` deltaP `5.3354` edge `-0.0019` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.7586` n `96` status `ready` deltaP `-7.4653` edge `0.0269` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.6036` n `96` status `ready` deltaP `-19.618` edge `-0.0112` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
