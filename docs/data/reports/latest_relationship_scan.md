# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T20:07:25.087749+00:00`
- Price records: `672`
- Market context records: `6425`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.2892` n `32` status `ready` deltaP `31.5972` edge `0.8282` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.0419` n `146` status `ready` deltaP `18.2624` edge `0.7951` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5996` n `32` status `ready` deltaP `55.5556` edge `0.1796` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1863` n `32` status `ready` deltaP `43.6738` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1276` n `32` status `ready` deltaP `35.4167` edge `0.1284` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.5701` n `32` status `ready` deltaP `13.1944` edge `0.4477` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4961` n `32` status `ready` deltaP `30.0898` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5178` n `32` status `ready` deltaP `14.4274` edge `0.1451` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8661` n `32` status `ready` deltaP `10.1235` edge `0.0897` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.7763` n `201` status `ready` deltaP `-6.9719` edge `0.2047` maxDD `-3.4826`
- `market_context_high->metal_4h` score `0.3177` n `195` status `ready` deltaP `10.319` edge `0.0415` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.236` n `195` status `ready` deltaP `9.5857` edge `0.0234` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1878` n `32` status `ready` deltaP `7.1295` edge `-0.0287` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2867` n `146` status `ready` deltaP `18.5978` edge `0.0961` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5333` n `201` status `ready` deltaP `1.0941` edge `0.0021` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5885` n `32` status `ready` deltaP `-0.1497` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.592` n `195` status `ready` deltaP `7.0622` edge `0.0469` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6473` n `201` status `ready` deltaP `-1.8426` edge `-0.0024` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6967` n `201` status `ready` deltaP `-3.0402` edge `0.0029` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7479` n `32` status `ready` deltaP `0.5208` edge `-0.0122` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
