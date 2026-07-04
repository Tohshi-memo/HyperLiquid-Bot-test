# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T07:22:29.618967+00:00`
- Price records: `672`
- Market context records: `5639`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8683`

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

- `market_context_high->equity_24h` score `2.8192` n `174` status `ready` deltaP `14.314` edge `0.6474` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3526` n `174` status `ready` deltaP `21.9588` edge `0.0637` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.6324` n `237` status `ready` deltaP `9.9374` edge `0.2157` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4637` n `237` status `ready` deltaP `7.3814` edge `0.1533` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.261` n `237` status `ready` deltaP `5.1547` edge `0.1288` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2719` n `237` status `ready` deltaP `1.749` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.375` n `237` status `ready` deltaP `5.316` edge `0.034` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5574` n `237` status `ready` deltaP `-0.6058` edge `0.0001` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5894` n `237` status `ready` deltaP `4.4304` edge `0.0459` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5926` n `237` status `ready` deltaP `1.5861` edge `0.0362` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9549` n `237` status `ready` deltaP `0.2792` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0309` n `237` status `ready` deltaP `-0.5786` edge `-0.0055` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3422` n `237` status `ready` deltaP `0.7609` edge `0.0062` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9843` n `237` status `ready` deltaP `-1.0792` edge `0.009` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.2873` n `174` status `ready` deltaP `10.9555` edge `0.0324` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9942` n `237` status `ready` deltaP `-13.6069` edge `-0.0548` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8688` n `237` status `ready` deltaP `-2.7973` edge `-0.0362` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4109` n `174` status `ready` deltaP `4.5977` edge `0.0558` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2584` n `174` status `ready` deltaP `-10.9315` edge `-0.2498` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.2448` n `174` status `ready` deltaP `-17.6305` edge `-0.1253` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
