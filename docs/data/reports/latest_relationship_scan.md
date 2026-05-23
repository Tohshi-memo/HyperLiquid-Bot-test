# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T19:37:13.018181+00:00`
- Price records: `672`
- Market context records: `1661`
- Flow alert records: `6690`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `10.0571` n `169` status `ready` deltaP `28.9337` edge `0.8878` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.5148` n `194` status `ready` deltaP `22.6875` edge `0.4914` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7983` n `169` status `ready` deltaP `20.5841` edge `0.3171` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.6265` n `194` status `ready` deltaP `18.7748` edge `0.3646` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.9627` n `194` status `ready` deltaP `12.9909` edge `0.1864` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7669` n `169` status `ready` deltaP `19.9473` edge `0.5041` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.9643` n `169` status `ready` deltaP `25.7468` edge `0.7673` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7211` n `169` status `ready` deltaP `26.401` edge `1.065` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.5941` n `205` status `ready` deltaP `6.5956` edge `0.1079` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.1984` n `205` status `ready` deltaP `2.1769` edge `0.0409` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.343` n `194` status `ready` deltaP `1.8029` edge `0.0529` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.3827` n `205` status `ready` deltaP `2.8377` edge `0.0594` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4094` n `169` status `ready` deltaP `6.7331` edge `0.0259` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4583` n `205` status `ready` deltaP `-0.8222` edge `0.0099` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7352` n `205` status `ready` deltaP `4.9387` edge `0.0064` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8208` n `205` status `ready` deltaP `-0.3111` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.2412` n `194` status `ready` deltaP `9.4581` edge `0.1027` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.3031` n `205` status `ready` deltaP `-0.1278` edge `-0.0172` maxDD `-9.5876`
- `market_context_high->fx_4h` score `-1.91` n `194` status `ready` deltaP `-7.9461` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.3676` n `194` status `ready` deltaP `11.6172` edge `-0.2143` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
