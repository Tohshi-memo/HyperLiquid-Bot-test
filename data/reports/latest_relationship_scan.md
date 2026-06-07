# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T16:07:22.643219+00:00`
- Price records: `672`
- Market context records: `3194`
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

- `market_context_high->commodity_24h` score `13.6104` n `104` status `ready` deltaP `47.329` edge `0.8615` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0425` n `104` status `ready` deltaP `16.1726` edge `2.4337` maxDD `-71.142`
- `market_context_high->unknown_24h` score `7.5347` n `104` status `ready` deltaP `17.6683` edge `0.7534` maxDD `-17.4635`
- `market_context_high->index_24h` score `6.2774` n `104` status `ready` deltaP `30.0213` edge `0.8601` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8436` n `104` status `ready` deltaP `13.6351` edge `1.3717` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.2334` n `136` status `ready` deltaP `20.8124` edge `0.1765` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.9` n `104` status `ready` deltaP `14.1693` edge `0.0033` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.731` n `136` status `ready` deltaP `12.4103` edge `0.2004` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.434` n `136` status `ready` deltaP `6.9038` edge `0.0324` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3852` n `136` status `ready` deltaP `5.7591` edge `0.0185` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.3921` n `136` status `ready` deltaP `6.4944` edge `0.1194` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7548` n `136` status `ready` deltaP `17.3153` edge `0.0787` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-0.9935` n `136` status `ready` deltaP `3.6324` edge `0.0747` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2177` n `136` status `ready` deltaP `5.0106` edge `0.0137` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3036` n `136` status `ready` deltaP `-10.8232` edge `-0.0065` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6492` n `136` status `ready` deltaP `-9.5324` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1503` n `136` status `ready` deltaP `-4.5483` edge `-0.0095` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-3.1951` n `136` status `ready` deltaP `1.9769` edge `-0.0768` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.6164` n `136` status `ready` deltaP `16.6517` edge `0.3921` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-3.6604` n `136` status `ready` deltaP `10.3479` edge `0.2541` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
