# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T12:37:17.786332+00:00`
- Price records: `672`
- Market context records: `1630`
- Flow alert records: `6603`
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

- `market_context_high->metal_24h` score `10.3057` n `185` status `ready` deltaP `26.806` edge `0.9227` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.2268` n `185` status `ready` deltaP `18.9451` edge `0.2804` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4181` n `186` status `ready` deltaP `11.7494` edge `0.1493` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `1.1996` n `186` status `ready` deltaP `15.9719` edge `0.3277` maxDD `-17.4311`
- `market_context_high->equity_24h` score `0.5528` n `185` status `ready` deltaP `17.4762` edge `0.4194` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.5511` n `186` status `ready` deltaP `11.7519` edge `0.2632` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2483` n `197` status `ready` deltaP `1.5805` edge `0.06` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.3103` n `185` status `ready` deltaP `7.4776` edge `0.0292` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.5369` n `197` status `ready` deltaP `1.126` edge `0.0286` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5711` n `197` status `ready` deltaP `-0.9887` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6452` n `197` status `ready` deltaP `0.7057` edge `0.0047` maxDD `-1.7205`
- `market_context_high->crypto_major_24h` score `-0.7948` n `185` status `ready` deltaP `22.9725` edge `0.6392` maxDD `-62.3533`
- `market_context_high->index_4h` score `-0.8531` n `186` status `ready` deltaP `0.2258` edge `0.0363` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8757` n `197` status `ready` deltaP `-1.1351` edge `0.0284` maxDD `-5.9819`
- `market_context_high->commodity_1h` score `-0.9958` n `197` status `ready` deltaP `1.1632` edge `0.0014` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.3282` n `197` status `ready` deltaP `2.8947` edge `0.0036` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3992` n `186` status `ready` deltaP `8.5776` edge `0.0954` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0643` n `186` status `ready` deltaP `-9.7854` edge `-0.0139` maxDD `-1.4313`
- `market_context_high->crypto_alt_24h` score `-2.2071` n `185` status `ready` deltaP `23.158` edge `0.8426` maxDD `-88.8062`
- `market_context_high->unknown_4h` score `-4.1667` n `186` status `ready` deltaP `7.3796` edge `-0.1693` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
