# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T02:52:16.504994+00:00`
- Price records: `672`
- Market context records: `1693`
- Flow alert records: `6782`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->unknown_24h` score `7.2996` n `142` status `ready` deltaP `18.3806` edge `1.0178` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.7211` n `142` status `ready` deltaP `25.7834` edge `0.6308` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.2217` n `192` status `ready` deltaP `22.4339` edge `0.552` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9419` n `192` status `ready` deltaP `22.1671` edge `0.4516` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8745` n `142` status `ready` deltaP `17.0963` edge `0.3467` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9871` n `192` status `ready` deltaP `15.7012` edge `0.2537` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8994` n `142` status `ready` deltaP `16.0095` edge `0.5414` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6625` n `199` status `ready` deltaP `6.5056` edge `0.1142` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4007` n `142` status `ready` deltaP `24.1508` edge `1.0533` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.3654` n `192` status `ready` deltaP `7.3424` edge `0.0904` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0121` n `199` status `ready` deltaP `4.2812` edge `0.0513` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.0971` n `199` status `ready` deltaP `3.9825` edge `0.0816` maxDD `-4.6327`
- `market_context_high->metal_4h` score `-0.4468` n `192` status `ready` deltaP `12.0299` edge `0.1317` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5318` n `199` status `ready` deltaP `0.3679` edge `0.0164` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6071` n `199` status `ready` deltaP `5.8428` edge `0.0168` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-0.6536` n `142` status `ready` deltaP `22.4841` edge `0.6249` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.6636` n `199` status `ready` deltaP `-2.903` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8209` n `142` status `ready` deltaP `4.7249` edge `0.005` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.7471` n `192` status `ready` deltaP `-6.2246` edge `-0.0112` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.122` n `199` status `ready` deltaP `0.4649` edge `-0.0297` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
