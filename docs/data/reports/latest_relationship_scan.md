# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T08:52:18.775832+00:00`
- Price records: `672`
- Market context records: `2546`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.4805` n `153` status `ready` deltaP `24.2258` edge `0.5631` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.4475` n `120` status `ready` deltaP `19.6181` edge `0.356` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.5107` n `120` status `ready` deltaP `11.1111` edge `0.571` maxDD `-16.2014`
- `market_context_high->crypto_major_4h` score `3.8339` n `153` status `ready` deltaP `17.4289` edge `0.3843` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9055` n `153` status `ready` deltaP `10.87` edge `0.1913` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1884` n `153` status `ready` deltaP `9.9409` edge `0.1515` maxDD `-6.1656`
- `market_context_high->equity_24h` score `0.7285` n `120` status `ready` deltaP `17.5` edge `0.0111` maxDD `-3.0311`
- `market_context_high->crypto_major_1h` score `0.7134` n `153` status `ready` deltaP `8.3343` edge `0.1233` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.5594` n `120` status `ready` deltaP `5.7292` edge `0.1065` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.0886` n `153` status `ready` deltaP `6.4303` edge `0.0339` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1333` n `153` status `ready` deltaP `3.405` edge `0.0352` maxDD `-2.8543`
- `market_context_high->crypto_alt_24h` score `-0.1388` n `120` status `ready` deltaP `-1.7361` edge `0.659` maxDD `-41.2179`
- `market_context_high->index_1h` score `-0.2264` n `153` status `ready` deltaP `3.0801` edge `0.01` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.3056` n `153` status `ready` deltaP `1.4843` edge `0.0044` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.3616` n `153` status `ready` deltaP `2.178` edge `0.0139` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.3667` n `153` status `ready` deltaP `3.9637` edge `0.0144` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.7285` n `153` status `ready` deltaP `4.3111` edge `0.0493` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7527` n `153` status `ready` deltaP `0.3053` edge `0.0191` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8334` n `153` status `ready` deltaP `0.5878` edge `0.0126` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.9518` n `120` status `ready` deltaP `0.7986` edge `0.0021` maxDD `-2.3556`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
