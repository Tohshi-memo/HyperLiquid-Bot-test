# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T19:22:18.624772+00:00`
- Price records: `672`
- Market context records: `1660`
- Flow alert records: `6687`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.9971` n `169` status `ready` deltaP `28.9337` edge `0.8828` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.4635` n `193` status `ready` deltaP `22.5566` edge `0.488` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7971` n `169` status `ready` deltaP `20.5841` edge `0.317` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.593` n `193` status `ready` deltaP `18.6253` edge `0.3628` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.9351` n `193` status `ready` deltaP `12.8414` edge `0.1851` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7681` n `169` status `ready` deltaP `19.9473` edge `0.5042` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.9391` n `169` status `ready` deltaP `25.7468` edge `0.7652` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7211` n `169` status `ready` deltaP `26.401` edge `1.065` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.6286` n `204` status `ready` deltaP `6.8921` edge `0.1088` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.1887` n `204` status `ready` deltaP `2.3189` edge `0.0412` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.357` n `193` status `ready` deltaP `1.5946` edge `0.0525` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.3735` n `204` status `ready` deltaP `2.9559` edge `0.0598` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4305` n `169` status `ready` deltaP `6.56` edge `0.0253` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4483` n `204` status `ready` deltaP `-0.6898` edge `0.0103` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7471` n `204` status `ready` deltaP `4.7258` edge `0.0063` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8109` n `204` status `ready` deltaP `-0.2025` edge `-0.003` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.263` n `193` status `ready` deltaP `9.231` edge `0.1024` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.2651` n `204` status `ready` deltaP `0.1233` edge `-0.0165` maxDD `-9.3877`
- `market_context_high->fx_4h` score `-1.9017` n `193` status `ready` deltaP `-7.858` edge `-0.0132` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.2108` n `193` status `ready` deltaP `11.4329` edge `-0.2` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
