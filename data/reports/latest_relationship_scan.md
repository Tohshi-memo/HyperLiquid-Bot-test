# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T07:07:21.010774+00:00`
- Price records: `672`
- Market context records: `2640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5342` n `137` status `ready` deltaP `17.9808` edge `0.5408` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1931` n `137` status `ready` deltaP `25.1035` edge `0.5333` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5498` n `137` status `ready` deltaP `14.4182` edge `0.3807` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `3.0612` n `137` status `ready` deltaP `6.1334` edge `0.7392` maxDD `-32.999`
- `market_context_high->index_24h` score `1.2214` n `137` status `ready` deltaP `11.5737` edge `0.1227` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.1235` n `137` status `ready` deltaP `10.1348` edge `0.1448` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0261` n `137` status `ready` deltaP `6.5971` edge `0.1465` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.5875` n `137` status `ready` deltaP `7.3463` edge `0.1194` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4918` n `137` status `ready` deltaP `10.8799` edge `0.0526` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0605` n `137` status `ready` deltaP `3.2104` edge `0.0277` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.2423` n `137` status `ready` deltaP `2.7613` edge `0.0108` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.3255` n `137` status `ready` deltaP `3.9033` edge `0.0287` maxDD `-2.548`
- `market_context_high->commodity_1h` score `-0.4105` n `137` status `ready` deltaP `5.1936` edge `0.019` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4412` n `137` status `ready` deltaP `0.2338` edge `0.0058` maxDD `-2.114`
- `market_context_high->fx_1h` score `-0.5045` n `137` status `ready` deltaP `-0.1213` edge `0.0034` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.7887` n `137` status `ready` deltaP `4.0222` edge `-0.0015` maxDD `-0.9498`
- `market_context_high->fx_4h` score `-0.9287` n `137` status `ready` deltaP `-0.7344` edge `0.0106` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0015` n `137` status `ready` deltaP `-2.0848` edge `0.0143` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.0177` n `137` status `ready` deltaP `4.6477` edge `0.0328` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.2438` n `137` status `ready` deltaP `2.9998` edge `0.0168` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
