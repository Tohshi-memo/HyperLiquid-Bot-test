# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T23:52:28.840995+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7053`

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

- `market_context_high->unknown_24h` score `7589.1307` n `55` status `ready` deltaP `1.3889` edge `632.4183` maxDD `0.0`
- `market_context_high->unknown_4h` score `331.6646` n `55` status `ready` deltaP `7.1757` edge `27.5952` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `37.1822` n `55` status `ready` deltaP `4.3604` edge `3.0805` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.286` n `55` status `ready` deltaP `42.7999` edge `1.5121` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.3177` n `94` status `ready` deltaP `31.3091` edge `1.0367` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1722` n `55` status `ready` deltaP `49.1319` edge `0.1868` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1001` n `55` status `ready` deltaP `24.0549` edge `0.3774` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8873` n `55` status `ready` deltaP `40.7545` edge `0.25` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.5371` n `55` status `ready` deltaP `30.8925` edge `0.2891` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.2688` n `55` status `ready` deltaP `5.8952` edge `0.3033` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.062` n `55` status `ready` deltaP `29.3902` edge `0.0843` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.4221` n `126` status `ready` deltaP `9.9279` edge `0.2743` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3919` n `55` status `ready` deltaP `10.3378` edge `0.3054` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9669` n `55` status `ready` deltaP `-3.952` edge `0.4303` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7579` n `55` status `ready` deltaP `20.6374` edge `0.0514` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5476` n `55` status `ready` deltaP `3.3261` edge `0.1593` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.4051` n `55` status `ready` deltaP `3.7752` edge `0.159` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.3928` n `55` status `ready` deltaP `8.0321` edge `0.1235` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9714` n `55` status `ready` deltaP `12.074` edge `0.0253` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5646` n `55` status `ready` deltaP `13.6364` edge `-0.0001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
