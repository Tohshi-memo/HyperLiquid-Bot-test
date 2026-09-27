# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T01:47:08.689437+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3056.832` n `99` status `ready` deltaP `1.2153` edge `254.7279` maxDD `0.0`
- `market_context_high->unknown_1h` score `74.9295` n `44` status `ready` deltaP `10.3022` edge `6.1801` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.3404` n `44` status `ready` deltaP `27.762` edge `4.1284` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.819` n `44` status `ready` deltaP `14.9148` edge `2.2568` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7252` n `44` status `ready` deltaP `36.0954` edge `2.1012` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.692` n `44` status `ready` deltaP `31.7551` edge `0.4381` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6832` n `44` status `ready` deltaP `31.9602` edge `0.1177` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3872` n `44` status `ready` deltaP `37.985` edge `0.0361` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.028` n `44` status `ready` deltaP `18.4312` edge `0.1671` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.386` n `44` status `ready` deltaP `9.4651` edge `0.115` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.247` n `99` status `ready` deltaP `17.8662` edge `0.046` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `1.1492` n `44` status `ready` deltaP `9.1181` edge `0.1084` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.1114` n `44` status `ready` deltaP `12.3163` edge `0.0508` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.0805` n `99` status `ready` deltaP `25.3946` edge `0.134` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `1.0166` n `44` status `ready` deltaP `7.525` edge `0.125` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8032` n `44` status `ready` deltaP `12.1666` edge `0.0095` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2599` n `44` status `ready` deltaP `6.3146` edge `0.0112` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1547` n `44` status `ready` deltaP `7.3625` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.1243` n `44` status `ready` deltaP `4.3005` edge `0.0706` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1178` n `139` status `ready` deltaP `2.3726` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
