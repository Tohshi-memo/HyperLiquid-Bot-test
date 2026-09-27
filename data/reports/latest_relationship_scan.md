# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T04:22:30.852799+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11522`

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

- `news_risk_high->unknown_24h` score `2288.2716` n `109` status `ready` deltaP `1.2153` edge `190.6812` maxDD `0.0`
- `market_context_high->unknown_1h` score `77.1303` n `44` status `ready` deltaP `10.3022` edge `6.3635` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.9881` n `44` status `ready` deltaP `29.4981` edge `4.1708` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.1538` n `44` status `ready` deltaP `14.9148` edge `2.2847` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.868` n `44` status `ready` deltaP `36.0954` edge `2.1131` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8554` n `44` status `ready` deltaP `33.3176` edge `0.4413` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8178` n `44` status `ready` deltaP `33.5227` edge `0.1185` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.269` n `44` status `ready` deltaP `36.613` edge `0.0354` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8715` n `44` status `ready` deltaP `17.0593` edge `0.1632` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.2208` n `44` status `ready` deltaP `8.8553` edge `0.1053` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.0904` n `44` status `ready` deltaP `9.1181` edge `0.1035` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.0216` n `44` status `ready` deltaP `11.5678` edge `0.0483` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8742` n `44` status `ready` deltaP `6.9152` edge `0.1172` maxDD `-5.2359`
- `news_risk_high->metal_24h` score `0.7847` n `109` status `ready` deltaP `20.4702` edge `0.1289` maxDD `-6.8481`
- `market_context_high->index_1h` score `0.7373` n `44` status `ready` deltaP `11.4181` edge `0.009` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.6161` n `109` status `ready` deltaP `12.6545` edge `0.0365` maxDD `-2.2287`
- `market_context_high->metal_1h` score `0.2695` n `44` status `ready` deltaP `6.4643` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1547` n `44` status `ready` deltaP `7.3625` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.081` n `44` status `ready` deltaP `4.5999` edge `0.065` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1658` n `142` status `ready` deltaP `1.847` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
