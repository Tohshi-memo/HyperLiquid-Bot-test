# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T13:37:29.620286+00:00`
- Price records: `672`
- Market context records: `8096`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.3581` n `87` status `ready` deltaP `36.9051` edge `1.5415` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4447` n `87` status `ready` deltaP `32.8778` edge `0.5325` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3252` n `87` status `ready` deltaP `35.8752` edge `0.4546` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.324` n `43` status `ready` deltaP `30.4453` edge `0.4279` maxDD `-0.6428`
- `news_risk_high->equity_1h` score `3.5855` n `43` status `ready` deltaP `29.0802` edge `0.1358` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.4668` n `43` status `ready` deltaP `14.2407` edge `0.2545` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.3341` n `87` status `ready` deltaP `31.893` edge `0.084` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0889` n `87` status `ready` deltaP `19.7454` edge `0.1928` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7852` n `43` status `ready` deltaP `4.6059` edge `0.2292` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.4941` n `87` status `ready` deltaP `15.4742` edge `0.148` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.3841` n `43` status `ready` deltaP `21.3343` edge `0.0755` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3192` n `87` status `ready` deltaP `21.3011` edge `0.1135` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.1209` n `87` status `ready` deltaP `28.9487` edge `0.0541` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.2284` n `87` status `ready` deltaP `16.0197` edge `0.0223` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.2187` n `43` status `ready` deltaP `12.9076` edge `0.0623` maxDD `-0.7433`
- `market_context_high->crypto_alt_4h` score `0.9789` n `87` status `ready` deltaP `6.9439` edge `0.147` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `0.8425` n `87` status `ready` deltaP `27.0523` edge `0.2162` maxDD `-15.7497`
- `market_context_high->metal_1h` score `0.8111` n `87` status `ready` deltaP `11.3738` edge `0.0296` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.7779` n `43` status `ready` deltaP `3.4884` edge `0.0813` maxDD `-1.1783`
- `market_context_high->crypto_major_4h` score `0.6926` n `87` status `ready` deltaP `8.8678` edge `0.1704` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
