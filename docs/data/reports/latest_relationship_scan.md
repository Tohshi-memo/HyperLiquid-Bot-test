# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T08:52:30.377812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9962`

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

- `market_context_high->unknown_4h` score `34.3712` n `118` status `ready` deltaP `-2.4003` edge `2.9449` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `11.6679` n `51` status `ready` deltaP `23.509` edge `1.5714` maxDD `-12.2456`
- `market_context_high->crypto_alt_24h` score `9.8421` n `51` status `ready` deltaP `11.877` edge `1.4883` maxDD `-18.1203`
- `risk_on_high->crypto_alt_4h` score `3.7655` n `50` status `ready` deltaP `18.9695` edge `0.2321` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.7655` n `50` status `ready` deltaP `18.9695` edge `0.2321` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.438` n `50` status `ready` deltaP `33.2012` edge `0.3047` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.438` n `50` status `ready` deltaP `33.2012` edge `0.3047` maxDD `-4.1548`
- `market_context_high->equity_24h` score `2.9626` n `51` status `ready` deltaP `8.027` edge `0.4666` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.9677` n `51` status `ready` deltaP `27.9309` edge `0.1221` maxDD `-0.4833`
- `risk_on_high->crypto_alt_1h` score `1.1102` n `50` status `ready` deltaP `6.7066` edge `0.1075` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.1102` n `50` status `ready` deltaP `6.7066` edge `0.1075` maxDD `-2.4421`
- `market_context_high->unknown_1h` score `0.9337` n `118` status `ready` deltaP `-5.3638` edge `0.1472` maxDD `-1.024`
- `market_context_high->crypto_alt_1h` score `0.8989` n `118` status `ready` deltaP `7.7235` edge `0.1185` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.7264` n `118` status `ready` deltaP `10.8283` edge `0.2315` maxDD `-11.1784`
- `risk_on_high->crypto_major_1h` score `0.4954` n `50` status `ready` deltaP `5.8503` edge `0.0898` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4954` n `50` status `ready` deltaP `5.8503` edge `0.0898` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.2394` n `118` status `ready` deltaP `3.2401` edge `0.0854` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.0284` n `118` status `ready` deltaP `4.2915` edge `0.2296` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.1676` n `118` status `ready` deltaP `5.4324` edge `0.0059` maxDD `-0.4868`
- `market_context_high->metal_24h` score `-0.2126` n `51` status `ready` deltaP `6.8423` edge `0.036` maxDD `-2.7096`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
