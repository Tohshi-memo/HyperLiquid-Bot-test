# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T16:22:22.643286+00:00`
- Price records: `672`
- Market context records: `2157`
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

- `market_context_high->crypto_alt_4h` score `13.6561` n `144` status `ready` deltaP `37.6863` edge `0.9804` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.951` n `144` status `ready` deltaP `41.7174` edge `0.7708` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1261` n `144` status `ready` deltaP `24.4241` edge `0.4226` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.4544` n `144` status `ready` deltaP `25.5082` edge `0.3106` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0671` n `39` status `ready` deltaP `31.0116` edge `0.3818` maxDD `-3.0367`
- `market_context_high->crypto_major_1h` score `3.4845` n `144` status `ready` deltaP `18.3134` edge `0.216` maxDD `-1.817`
- `market_context_high->index_24h` score `3.4174` n `144` status `ready` deltaP `13.3681` edge `0.3185` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `3.3376` n `144` status `ready` deltaP `16.9661` edge `0.2514` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.2174` n `144` status `ready` deltaP `23.8313` edge `0.1776` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.7892` n `144` status `ready` deltaP `27.4306` edge `0.5816` maxDD `-35.8966`
- `market_context_high->metal_4h` score `2.6088` n `144` status `ready` deltaP `20.2574` edge `0.2211` maxDD `-4.7664`
- `market_context_high->equity_24h` score `2.605` n `144` status `ready` deltaP `25.1736` edge `0.5391` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.5148` n `39` status `ready` deltaP `31.5393` edge `0.0177` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1796` n `144` status `ready` deltaP `20.3125` edge `1.0026` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4845` n `39` status `ready` deltaP `14.4348` edge `0.0998` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0783` n `43` status `ready` deltaP `19.1686` edge `0.009` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.7822` n `43` status `ready` deltaP `10.4651` edge `0.0985` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.738` n `144` status `ready` deltaP `10.0258` edge `0.0735` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6238` n `144` status `ready` deltaP `9.4769` edge `0.0558` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
