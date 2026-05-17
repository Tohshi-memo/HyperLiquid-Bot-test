# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T18:07:17.139637+00:00`
- Price records: `672`
- Market context records: `1037`
- Flow alert records: `4893`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->crypto_major_24h` score `14.3408` n `182` status `ready` deltaP `33.1683` edge `1.0328` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5607` n `182` status `ready` deltaP `11.3932` edge `0.4275` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.3681` n `182` status `ready` deltaP `11.416` edge `0.2834` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5222` n `182` status `ready` deltaP `10.7072` edge `0.2196` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.0686` n `182` status `ready` deltaP `-6.2067` edge `0.4023` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0688` n `183` status `ready` deltaP `5.4236` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.434` n `183` status `ready` deltaP `4.4288` edge `0.0123` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6249` n `183` status `ready` deltaP `0.0572` edge `0.0232` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6651` n `183` status `ready` deltaP `1.1788` edge `0.0175` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0373` n `182` status `ready` deltaP `1.6199` edge `0.0024` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.066` n `183` status `ready` deltaP `5.8277` edge `-0.0037` maxDD `-7.9187`
- `market_context_high->index_4h` score `-1.376` n `182` status `ready` deltaP `-0.2144` edge `0.0344` maxDD `-6.1444`
- `market_context_high->crypto_alt_1h` score `-1.3825` n `183` status `ready` deltaP `-0.0032` edge `-0.0066` maxDD `-5.3538`
- `market_context_high->equity_4h` score `-1.5563` n `182` status `ready` deltaP `1.9515` edge `0.0725` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.945` n `183` status `ready` deltaP `2.6316` edge `-0.0348` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.8725` n `182` status `ready` deltaP `1.1157` edge `0.031` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1143` n `182` status `ready` deltaP `7.5114` edge `0.061` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1682` n `182` status `ready` deltaP `3.218` edge `-0.02` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5332` n `182` status `ready` deltaP `-4.5263` edge `0.0525` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9568` n `182` status `ready` deltaP `-1.1492` edge `-0.1563` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
