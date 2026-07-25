# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T12:07:26.906068+00:00`
- Price records: `672`
- Market context records: `7876`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `13.1412` n `115` status `ready` deltaP `29.3071` edge `1.0339` maxDD `-6.0681`
- `market_context_high->metal_24h` score `3.4462` n `115` status `ready` deltaP `18.2925` edge `0.2856` maxDD `-1.2959`
- `market_context_high->equity_4h` score `2.8305` n `115` status `ready` deltaP `12.36` edge `0.3781` maxDD `-5.1426`
- `market_context_high->crypto_major_4h` score `1.634` n `115` status `ready` deltaP `17.1262` edge `0.1938` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.6336` n `115` status `ready` deltaP `14.3028` edge `0.1525` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.4517` n `115` status `ready` deltaP `21.3179` edge `0.1372` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.2122` n `115` status `ready` deltaP `13.4783` edge `0.0511` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.1446` n `115` status `ready` deltaP `30.9904` edge `0.0489` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7987` n `115` status `ready` deltaP `11.2573` edge `0.1091` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.3911` n `115` status `ready` deltaP `7.4764` edge `0.0421` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.3493` n `115` status `ready` deltaP `4.8399` edge `0.0401` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.1878` n `115` status `ready` deltaP `7.454` edge `0.0174` maxDD `-0.7743`
- `market_context_high->index_4h` score `0.1401` n `115` status `ready` deltaP `12.6658` edge `0.0562` maxDD `-1.1479`
- `market_context_high->commodity_1h` score `-0.0487` n `115` status `ready` deltaP `4.357` edge `0.0128` maxDD `-0.6722`
- `market_context_high->metal_4h` score `-0.0687` n `115` status `ready` deltaP `6.9167` edge `0.0922` maxDD `-1.1899`
- `market_context_high->fx_1h` score `-0.2719` n `115` status `ready` deltaP `2.3868` edge `-0.0001` maxDD `-0.4112`
- `market_context_high->index_24h` score `-0.7058` n `115` status `ready` deltaP `-1.4931` edge `0.111` maxDD `-1.7889`
- `market_context_high->metal_1h` score `-0.7449` n `115` status `ready` deltaP `0.3996` edge `0.0231` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.0091` n `115` status `ready` deltaP `-0.7685` edge `0.0001` maxDD `-1.6148`
- `market_context_high->crypto_alt_24h` score `-1.5922` n `115` status `ready` deltaP `13.1851` edge `0.2375` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
