# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T10:07:30.801010+00:00`
- Price records: `672`
- Market context records: `8081`
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

- `market_context_high->equity_24h` score `20.2244` n `85` status `ready` deltaP `36.6887` edge `1.5318` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.8293` n `37` status `ready` deltaP `36.2105` edge `0.499` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.4046` n `87` status `ready` deltaP `32.4205` edge `0.5322` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.276` n `85` status `ready` deltaP `35.8752` edge `0.4505` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.1782` n `37` status `ready` deltaP `24.1101` edge `0.3115` maxDD `-1.2571`
- `news_risk_high->equity_1h` score `3.402` n `42` status `ready` deltaP `27.6447` edge `0.1308` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2989` n `87` status `ready` deltaP `31.5881` edge `0.0831` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0065` n `85` status `ready` deltaP `19.0152` edge `0.1908` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7584` n `42` status `ready` deltaP `2.8443` edge `0.2386` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.6768` n `37` status `ready` deltaP `23.4179` edge `0.086` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.3371` n `87` status `ready` deltaP `14.4263` edge `0.1419` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.3314` n `87` status `ready` deltaP `21.4536` edge `0.1135` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.2777` n `85` status `ready` deltaP `30.5638` edge `0.0564` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3791` n `37` status `ready` deltaP `13.563` edge `0.0713` maxDD `-0.7433`
- `news_risk_high->fx_4h` score `1.2296` n `37` status `ready` deltaP `17.3863` edge `0.0172` maxDD `-0.1179`
- `market_context_high->index_1h` score `1.1314` n `87` status `ready` deltaP `14.9718` edge `0.0212` maxDD `-0.4716`
- `news_risk_high->crypto_alt_4h` score `1.0155` n `37` status `ready` deltaP `14.0615` edge `0.1273` maxDD `-3.9346`
- `market_context_high->commodity_24h` score `0.9927` n `85` status `ready` deltaP `26.3839` edge `0.2147` maxDD `-14.3993`
- `market_context_high->metal_1h` score `0.7847` n `87` status `ready` deltaP `11.0744` edge `0.0294` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.6862` n `87` status `ready` deltaP `5.1146` edge `0.1348` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
