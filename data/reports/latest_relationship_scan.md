# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T15:22:15.126126+00:00`
- Price records: `672`
- Market context records: `1642`
- Flow alert records: `6637`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.5846` n `174` status `ready` deltaP `27.0622` edge `0.8609` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.4563` n `174` status `ready` deltaP `19.099` edge `0.2985` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `3.2916` n `185` status `ready` deltaP `20.0576` edge `0.407` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `1.7683` n `185` status `ready` deltaP `15.8172` edge `0.3128` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.5551` n `185` status `ready` deltaP `11.5866` edge `0.1618` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.1784` n `174` status `ready` deltaP `18.1867` edge `0.4668` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.0481` n `194` status `ready` deltaP `3.491` edge `0.0831` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.0056` n `174` status `ready` deltaP `23.8879` edge `0.6998` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4491` n `174` status `ready` deltaP `6.6575` edge `0.0231` maxDD `-1.3925`
- `market_context_high->index_4h` score `-0.493` n `185` status `ready` deltaP `-0.0009` edge `0.0457` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4947` n `194` status `ready` deltaP `0.4645` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.4988` n `194` status `ready` deltaP `0.9121` edge `0.0332` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.5625` n `174` status `ready` deltaP `24.3809` edge `0.9715` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `-0.637` n `194` status `ready` deltaP `0.3488` edge `0.0434` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.6479` n `194` status `ready` deltaP `0.1467` edge `0.0082` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.8495` n `194` status `ready` deltaP `1.5294` edge `-0.0068` maxDD `-6.6507`
- `market_context_high->metal_1h` score `-1.3168` n `194` status `ready` deltaP `2.9925` edge `0.0039` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.4076` n `185` status `ready` deltaP `-11.0947` edge `-0.0136` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4873` n `185` status `ready` deltaP `7.3266` edge `0.0964` maxDD `-12.5349`
- `market_context_high->unknown_4h` score `-3.482` n `185` status `ready` deltaP `8.8584` edge `-0.1221` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
