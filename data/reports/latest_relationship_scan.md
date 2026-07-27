# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T14:07:27.592369+00:00`
- Price records: `672`
- Market context records: `8098`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11777`

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

- `market_context_high->equity_24h` score `20.4295` n `87` status `ready` deltaP `37.0784` edge `1.5463` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4903` n `87` status `ready` deltaP `32.8778` edge `0.5363` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3432` n `87` status `ready` deltaP `35.8752` edge `0.4561` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.3696` n `43` status `ready` deltaP `30.4453` edge `0.4317` maxDD `-0.6428`
- `news_risk_high->equity_1h` score `3.6083` n `43` status `ready` deltaP `29.0802` edge `0.1377` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.5173` n `43` status `ready` deltaP `14.3931` edge `0.2577` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.3437` n `87` status `ready` deltaP `31.893` edge `0.0848` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.131` n `87` status `ready` deltaP `20.092` edge `0.194` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7816` n `43` status `ready` deltaP `4.6059` edge `0.2289` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5169` n `87` status `ready` deltaP `15.4742` edge `0.1499` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.3937` n `43` status `ready` deltaP `21.3343` edge `0.0763` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3508` n `87` status `ready` deltaP `21.606` edge `0.1141` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0871` n `87` status `ready` deltaP `28.6021` edge `0.0536` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.262` n `87` status `ready` deltaP `16.3191` edge `0.0231` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.2503` n `43` status `ready` deltaP `13.2125` edge `0.0629` maxDD `-0.7433`
- `market_context_high->crypto_alt_4h` score `1.0271` n `87` status `ready` deltaP `7.0963` edge `0.15` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `0.8847` n `87` status `ready` deltaP `27.3989` edge `0.2193` maxDD `-15.7497`
- `market_context_high->metal_1h` score `0.823` n `87` status `ready` deltaP `11.5235` edge `0.0296` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.748` n `43` status `ready` deltaP `3.3387` edge `0.0798` maxDD `-1.1783`
- `market_context_high->crypto_major_4h` score `0.7432` n `87` status `ready` deltaP `9.0202` edge `0.1736` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
