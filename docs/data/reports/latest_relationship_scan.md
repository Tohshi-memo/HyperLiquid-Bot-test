# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T16:37:22.699637+00:00`
- Price records: `672`
- Market context records: `3196`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->commodity_24h` score `13.4933` n `102` status `ready` deltaP `47.1405` edge `0.853` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.8009` n `102` status `ready` deltaP `15.0225` edge `2.4104` maxDD `-71.142`
- `market_context_high->unknown_24h` score `7.1123` n `102` status `ready` deltaP `17.4122` edge `0.7199` maxDD `-17.4635`
- `market_context_high->index_24h` score `6.2445` n `102` status `ready` deltaP `29.4934` edge `0.8594` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8206` n `102` status `ready` deltaP `14.2872` edge `1.3644` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.2712` n `134` status `ready` deltaP `21.0002` edge `0.1784` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.9199` n `102` status `ready` deltaP `14.328` edge `0.0039` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6977` n `134` status `ready` deltaP `11.9494` edge `0.2007` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.462` n `135` status `ready` deltaP `7.179` edge `0.0329` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3856` n `135` status `ready` deltaP `6.7532` edge `0.1185` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4129` n `135` status `ready` deltaP `5.4214` edge `0.0172` maxDD `-4.5023`
- `market_context_high->index_4h` score `-0.7981` n `134` status `ready` deltaP `16.8433` edge `0.0763` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-0.9899` n `135` status `ready` deltaP `3.8367` edge `0.0738` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1974` n `135` status `ready` deltaP `5.2639` edge `0.0137` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.2737` n `134` status `ready` deltaP `-10.2635` edge `-0.0064` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.7218` n `135` status `ready` deltaP `-10.4258` edge `-0.0053` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1393` n `135` status `ready` deltaP `-4.3657` edge `-0.0098` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.4797` n `134` status `ready` deltaP `16.0152` edge `0.3798` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2316` n `135` status `ready` deltaP `1.8053` edge `-0.0787` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7344` n `134` status `ready` deltaP `10.1407` edge `0.246` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
