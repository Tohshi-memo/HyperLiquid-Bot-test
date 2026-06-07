# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T12:52:21.442983+00:00`
- Price records: `672`
- Market context records: `3179`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.8641` n `102` status `ready` deltaP `47.1405` edge `0.8839` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.2354` n `102` status `ready` deltaP `20.0572` edge `0.9347` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.4389` n `102` status `ready` deltaP `14.1646` edge `2.3697` maxDD `-71.142`
- `market_context_high->index_24h` score `6.2024` n `102` status `ready` deltaP `29.4934` edge `0.854` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4072` n `102` status `ready` deltaP `12.6225` edge `1.3225` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1186` n `134` status `ready` deltaP `19.8125` edge `0.1736` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.718` n `102` status `ready` deltaP `11.9689` edge `0.0028` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.638` n `134` status `ready` deltaP `11.2031` edge `0.2007` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3504` n `140` status `ready` deltaP `5.9795` edge `0.0316` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3416` n `140` status `ready` deltaP `6.3131` edge `0.0204` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4236` n `140` status `ready` deltaP `6.2318` edge `0.1171` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.8608` n `134` status `ready` deltaP `16.386` edge `0.0713` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0235` n `140` status `ready` deltaP `3.58` edge `0.0712` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2406` n `140` status `ready` deltaP `4.4696` edge `0.0154` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3378` n `134` status `ready` deltaP `-11.4352` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.588` n `140` status `ready` deltaP `-8.7682` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.075` n `140` status `ready` deltaP `-3.8024` edge `-0.0082` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2297` n `134` status `ready` deltaP `17.5078` edge `0.4019` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0584` n `140` status `ready` deltaP `2.9513` edge `-0.0719` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6522` n `134` status `ready` deltaP `10.4455` edge `0.2545` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
