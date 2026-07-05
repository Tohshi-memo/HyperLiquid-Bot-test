# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T00:37:26.686716+00:00`
- Price records: `672`
- Market context records: `5720`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8892`

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

- `market_context_high->crypto_major_4h` score `1.3085` n `270` status `ready` deltaP `9.7403` edge `0.198` maxDD `-7.9783`
- `market_context_high->equity_24h` score `1.0222` n `218` status `ready` deltaP `17.0919` edge `0.525` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.2332` n `270` status `ready` deltaP `7.6942` edge `0.132` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1834` n `282` status `ready` deltaP `3.5068` edge `0.0012` maxDD `-0.5144`
- `market_context_high->crypto_alt_4h` score `-0.2558` n `270` status `ready` deltaP `7.1048` edge `0.1404` maxDD `-10.3933`
- `market_context_high->metal_1h` score `-0.4489` n `282` status `ready` deltaP `1.6` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5751` n `282` status `ready` deltaP `2.8921` edge `0.0338` maxDD `-4.4135`
- `market_context_high->index_1h` score `-0.6141` n `282` status `ready` deltaP `0.6466` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6142` n `282` status `ready` deltaP `3.2871` edge `0.0276` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7562` n `282` status `ready` deltaP `-1.6552` edge `-0.0052` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.8883` n `282` status `ready` deltaP `0.7963` edge `0.0288` maxDD `-4.9843`
- `market_context_high->fx_24h` score `-1.1121` n `218` status `ready` deltaP `11.0347` edge `0.0422` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1694` n `270` status `ready` deltaP `1.2003` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2596` n `270` status `ready` deltaP `2.5711` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6008` n `270` status `ready` deltaP `-6.9264` edge `-0.0497` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8538` n `218` status `ready` deltaP `2.789` edge `0.03` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8655` n `270` status `ready` deltaP `-3.9261` edge `-0.0284` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3094` n `218` status `ready` deltaP `7.1961` edge `0.0386` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5163` n `218` status `ready` deltaP `-5.6925` edge `-0.2372` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.3133` n `218` status `ready` deltaP `-9.3591` edge `-0.0664` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
