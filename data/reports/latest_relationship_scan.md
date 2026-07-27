# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T09:52:28.575606+00:00`
- Price records: `672`
- Market context records: `8080`
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

- `market_context_high->equity_24h` score `20.2124` n `85` status `ready` deltaP `36.6887` edge `1.5308` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.8317` n `36` status `ready` deltaP `36.0603` edge `0.5002` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3974` n `87` status `ready` deltaP `32.4205` edge `0.5316` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.27` n `85` status `ready` deltaP `35.8752` edge `0.45` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.6528` n `36` status `ready` deltaP `26.1349` edge `0.3318` maxDD `-0.7975`
- `news_risk_high->equity_1h` score `3.3996` n `42` status `ready` deltaP `27.6447` edge `0.1306` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2965` n `87` status `ready` deltaP `31.5881` edge `0.0829` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0041` n `85` status `ready` deltaP `19.0152` edge `0.1906` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7715` n `42` status `ready` deltaP `2.994` edge `0.2387` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.6563` n `36` status `ready` deltaP `22.9674` edge `0.0873` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.346` n `87` status `ready` deltaP `21.606` edge `0.1137` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3347` n `87` status `ready` deltaP `14.4263` edge `0.1417` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2951` n `85` status `ready` deltaP `30.7371` edge `0.0567` maxDD `-0.6283`
- `news_risk_high->fx_4h` score `1.3701` n `36` status `ready` deltaP `19.0379` edge `0.0179` maxDD `-0.1179`
- `news_risk_high->crypto_alt_4h` score `1.355` n `36` status `ready` deltaP `15.7859` edge `0.1471` maxDD `-3.2895`
- `news_risk_high->metal_4h` score `1.3289` n `36` status `ready` deltaP `12.8895` edge `0.0716` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1314` n `87` status `ready` deltaP `14.9718` edge `0.0212` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `0.972` n `85` status `ready` deltaP `26.2106` edge `0.2132` maxDD `-14.3993`
- `market_context_high->metal_1h` score `0.7715` n `87` status `ready` deltaP `10.9247` edge `0.0293` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.6476` n `87` status `ready` deltaP `4.9622` edge `0.1326` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
