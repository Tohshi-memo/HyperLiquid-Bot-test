# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T19:59:31.964204+00:00`
- Price records: `672`
- Market context records: `1663`
- Flow alert records: `6694`
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

- `market_context_high->metal_24h` score `10.1159` n `169` status `ready` deltaP `28.9337` edge `0.8927` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.529` n `194` status `ready` deltaP `22.7606` edge `0.4921` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7947` n `169` status `ready` deltaP `20.5841` edge `0.3168` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.636` n `194` status `ready` deltaP `18.8474` edge `0.3649` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.969` n `194` status `ready` deltaP `13.0547` edge `0.1865` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7597` n `169` status `ready` deltaP `19.9473` edge `0.5035` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.9919` n `169` status `ready` deltaP `25.7468` edge `0.7696` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7271` n `169` status `ready` deltaP `26.401` edge `1.0655` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.6046` n `206` status `ready` deltaP `6.7874` edge `0.1075` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2859` n `206` status `ready` deltaP `2.3734` edge `0.0412` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3397` n `194` status `ready` deltaP `1.867` edge `0.0529` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.3721` n `206` status `ready` deltaP `3.058` edge `0.0593` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.3884` n `169` status `ready` deltaP `6.9061` edge `0.0265` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.446` n `206` status `ready` deltaP `-0.6162` edge `0.0101` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7227` n `206` status `ready` deltaP `5.1494` edge `0.0066` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8317` n `206` status `ready` deltaP `-0.4171` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.2335` n `194` status `ready` deltaP `9.5393` edge `0.1028` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.3695` n `206` status `ready` deltaP `-0.3764` edge `-0.0179` maxDD `-9.7467`
- `market_context_high->fx_4h` score `-1.9044` n `194` status `ready` deltaP `-7.8765` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.4413` n `194` status `ready` deltaP `11.5367` edge `-0.2199` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
