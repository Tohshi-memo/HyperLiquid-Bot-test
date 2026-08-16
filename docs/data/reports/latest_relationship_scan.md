# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T20:01:10.987439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `207.3517` n `83` status `ready` deltaP `-25.1401` edge `27.0195` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.6674` n `83` status `ready` deltaP `41.3404` edge `0.3691` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.28` n `120` status `ready` deltaP `12.9268` edge `0.0676` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0002` n `123` status `ready` deltaP `3.1681` edge `0.02` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2663` n `120` status `ready` deltaP `4.7357` edge `0.0067` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2881` n `123` status `ready` deltaP `1.6479` edge `0.0015` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5458` n `123` status `ready` deltaP `1.1988` edge `-0.0064` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.6665` n `120` status `ready` deltaP `9.685` edge `-0.0093` maxDD `-4.5909`
- `market_context_high->index_1h` score `-1.1723` n `123` status `ready` deltaP `-6.3945` edge `-0.0029` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.2224` n `120` status `ready` deltaP `-10.2947` edge `-0.0072` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-1.463` n `83` status `ready` deltaP `-7.7727` edge `0.025` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6974` n `123` status `ready` deltaP `-10.1163` edge `-0.0462` maxDD `-4.9849`
- `market_context_high->index_24h` score `-1.7649` n `83` status `ready` deltaP `-5.11` edge `-0.0641` maxDD `-1.9152`
- `market_context_high->metal_24h` score `-1.9924` n `83` status `ready` deltaP `-10.8664` edge `0.0682` maxDD `-7.0954`
- `market_context_high->crypto_major_1h` score `-2.1644` n `123` status `ready` deltaP `-5.8834` edge `-0.0345` maxDD `-5.5318`
- `market_context_high->crypto_alt_1h` score `-2.1842` n `123` status `ready` deltaP `-3.594` edge `-0.0241` maxDD `-7.0497`
- `market_context_high->crypto_major_4h` score `-3.108` n `120` status `ready` deltaP `-0.9857` edge `-0.0573` maxDD `-11.2769`
- `market_context_high->crypto_major_24h` score `-3.8099` n `83` status `ready` deltaP `-4.7273` edge `0.0289` maxDD `-28.867`
- `market_context_high->unknown_1h` score `-6.8244` n `123` status `ready` deltaP `1.8621` edge `-0.5414` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-7.6126` n `120` status `ready` deltaP `-10.0711` edge `-0.0958` maxDD `-25.0488`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
