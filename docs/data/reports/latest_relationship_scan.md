# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T23:07:24.773284+00:00`
- Price records: `672`
- Market context records: `3121`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7025`

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

- `market_context_high->commodity_24h` score `14.5501` n `99` status `ready` deltaP `46.9855` edge `0.9421` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.262` n `99` status `ready` deltaP `21.5594` edge `0.9269` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.7869` n `99` status `ready` deltaP `10.6849` edge `2.3301` maxDD `-62.5486`
- `market_context_high->index_24h` score `6.6103` n `99` status `ready` deltaP `31.834` edge `0.8907` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8048` n `99` status `ready` deltaP `12.4684` edge `1.3124` maxDD `-51.0288`
- `market_context_high->commodity_4h` score `2.9956` n `125` status `ready` deltaP `18.5305` edge `0.1719` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0261` n `137` status `ready` deltaP `2.0685` edge `0.0263` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4707` n `137` status `ready` deltaP `4.0703` edge `0.0188` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5266` n `99` status `ready` deltaP `4.4666` edge `-0.0009` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7705` n `137` status `ready` deltaP `3.041` edge `0.0939` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0448` n `137` status `ready` deltaP `0.6644` edge `0.0102` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1357` n `137` status `ready` deltaP `-10.8462` edge `-0.0056` maxDD `-0.7485`
- `market_context_high->index_4h` score `-1.3306` n `125` status `ready` deltaP `10.8768` edge `0.0478` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4276` n `125` status `ready` deltaP `-13.7329` edge `-0.0071` maxDD `-1.0829`
- `market_context_high->crypto_major_1h` score `-2.0842` n `137` status `ready` deltaP `-0.3289` edge `0.0548` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2393` n `137` status `ready` deltaP `-6.1115` edge `-0.0065` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.6727` n `125` status `ready` deltaP `1.7695` edge `-0.0123` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-2.9678` n `137` status `ready` deltaP `2.0128` edge `-0.0581` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.7049` n `125` status `ready` deltaP `13.8146` edge `0.2374` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8324` n `125` status `ready` deltaP `7.7146` edge `-0.0122` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
