# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T22:37:25.901012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6523`

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

- `market_context_high->unknown_4h` score `42.44` n `43` status `ready` deltaP `-3.0559` edge `3.6018` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.7952` n `37` status `ready` deltaP `11.2472` edge `0.7541` maxDD `-31.3588`
- `market_context_high->fx_4h` score `1.791` n `43` status `ready` deltaP `21.4868` edge `0.0336` maxDD `-0.2073`
- `market_context_high->index_24h` score `1.1674` n `37` status `ready` deltaP `14.6913` edge `0.1148` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8774` n `37` status `ready` deltaP `10.9422` edge `0.009` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.7053` n `43` status `ready` deltaP `17.7857` edge `0.0272` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `0.3305` n `55` status `ready` deltaP `12.0114` edge `0.0169` maxDD `-1.7019`
- `market_context_high->equity_1h` score `0.202` n `55` status `ready` deltaP `2.4061` edge `0.116` maxDD `-4.8243`
- `market_context_high->commodity_4h` score `0.1924` n `43` status `ready` deltaP `3.8323` edge `0.0359` maxDD `-1.633`
- `market_context_high->commodity_24h` score `-0.1018` n `37` status `ready` deltaP `2.3931` edge `0.0905` maxDD `-6.5601`
- `market_context_high->metal_1h` score `-0.1523` n `55` status `ready` deltaP `1.3582` edge `0.0042` maxDD `-0.6226`
- `market_context_high->index_1h` score `-0.4233` n `55` status `ready` deltaP `-3.0485` edge `0.0193` maxDD `-0.5935`
- `market_context_high->fx_1h` score `-0.5517` n `55` status `ready` deltaP `-6.1486` edge `0.006` maxDD `-0.1928`
- `market_context_high->metal_24h` score `-1.565` n `37` status `ready` deltaP `7.8735` edge `-0.1276` maxDD `-1.4245`
- `market_context_high->metal_4h` score `-1.6044` n `43` status `ready` deltaP `-7.1114` edge `-0.0391` maxDD `-1.1087`
- `market_context_high->crypto_alt_1h` score `-1.8316` n `55` status `ready` deltaP `1.2928` edge `-0.0691` maxDD `-9.2807`
- `market_context_high->equity_4h` score `-2.3597` n `43` status `ready` deltaP `16.6407` edge `0.0204` maxDD `-24.9053`
- `market_context_high->crypto_major_1h` score `-2.3941` n `55` status `ready` deltaP `-1.1024` edge `-0.1098` maxDD `-10.5165`
- `market_context_high->crypto_alt_4h` score `-3.9578` n `43` status `ready` deltaP `11.0713` edge `-0.151` maxDD `-17.5435`
- `market_context_high->crypto_major_4h` score `-7.0798` n `43` status `ready` deltaP `-1.1273` edge `-0.2981` maxDD `-20.7495`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
