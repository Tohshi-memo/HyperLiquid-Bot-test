# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T16:24:08.338225+00:00`
- Price records: `672`
- Market context records: `2158`
- Flow alert records: `8107`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6489` n `144` status `ready` deltaP `37.6863` edge `0.9798` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9462` n `144` status `ready` deltaP `41.7174` edge `0.7704` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1201` n `144` status `ready` deltaP `24.4241` edge `0.4221` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.452` n `144` status `ready` deltaP `25.5082` edge `0.3104` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0773` n `39` status `ready` deltaP `31.164` edge `0.3821` maxDD `-3.0367`
- `market_context_high->crypto_major_1h` score `3.4809` n `144` status `ready` deltaP `18.3134` edge `0.2157` maxDD `-1.817`
- `market_context_high->index_24h` score `3.415` n `144` status `ready` deltaP `13.3681` edge `0.3183` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `3.3304` n `144` status `ready` deltaP `16.9661` edge `0.2508` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.2162` n `144` status `ready` deltaP `23.8313` edge `0.1775` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.782` n `144` status `ready` deltaP `27.4306` edge `0.581` maxDD `-35.8966`
- `market_context_high->metal_4h` score `2.6052` n `144` status `ready` deltaP `20.2574` edge `0.2208` maxDD `-4.7664`
- `market_context_high->equity_24h` score `2.6014` n `144` status `ready` deltaP `25.1736` edge `0.5388` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.5148` n `39` status `ready` deltaP `31.5393` edge `0.0177` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1765` n `144` status `ready` deltaP `20.3125` edge `1.0022` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4785` n `39` status `ready` deltaP `14.4348` edge `0.0993` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0603` n `43` status `ready` deltaP `19.0189` edge `0.0085` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.7838` n `43` status `ready` deltaP `10.4651` edge `0.0987` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7356` n `144` status `ready` deltaP `10.0258` edge `0.0733` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6202` n `144` status `ready` deltaP `9.4769` edge `0.0555` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4501` n `43` status `ready` deltaP `7.9898` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
