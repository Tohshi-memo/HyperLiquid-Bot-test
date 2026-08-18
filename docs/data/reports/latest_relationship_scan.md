# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T11:37:28.027790+00:00`
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

- `market_context_high->crypto_major_24h` score `2.2347` n `84` status `ready` deltaP `7.8918` edge `0.2544` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5125` n `84` status `ready` deltaP `16.6254` edge `0.2664` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0197` n `96` status `ready` deltaP `9.163` edge `0.0543` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.8039` n `96` status `ready` deltaP `15.0406` edge `0.0243` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.7438` n `96` status `ready` deltaP `9.4766` edge `0.1009` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6467` n `96` status `ready` deltaP `12.7682` edge `0.0075` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.5684` n `96` status `ready` deltaP `10.8232` edge `0.1022` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.5568` n `96` status `ready` deltaP `9.506` edge `0.0057` maxDD `-0.4807`
- `market_context_high->unknown_24h` score `-0.0091` n `84` status `ready` deltaP `14.3105` edge `-0.0784` maxDD `-0.0875`
- `market_context_high->equity_4h` score `-0.0211` n `96` status `ready` deltaP `2.1595` edge `0.0743` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0405` n `96` status `ready` deltaP `4.0232` edge `0.0085` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2329` n `96` status `ready` deltaP `3.0742` edge `-0.0001` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.3543` n `96` status `ready` deltaP `2.3765` edge `0.0189` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3749` n `96` status `ready` deltaP `4.0905` edge `0.0097` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4553` n `96` status `ready` deltaP `-3.5679` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4694` n `96` status `ready` deltaP `1.4845` edge `0.0144` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5665` n `96` status `ready` deltaP `1.0924` edge `0.011` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8557` n `96` status `ready` deltaP `-7.142` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9459` n `84` status `ready` deltaP `-6.6353` edge `0.0194` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.383` n `84` status `ready` deltaP `-14.4797` edge `-0.1771` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
