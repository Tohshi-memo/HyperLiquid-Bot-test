# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T14:22:27.092779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7285`

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

- `market_context_high->unknown_24h` score `2571.6946` n `106` status `ready` deltaP `-8.2252` edge `214.4057` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `77.2155` n `103` status `ready` deltaP `-5.8717` edge `6.5024` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `70.909` n `106` status `ready` deltaP `0.8657` edge `5.9166` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.5414` n `51` status `ready` deltaP `45.2103` edge `1.1655` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.1463` n `106` status `ready` deltaP `26.9359` edge `1.025` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.7685` n `106` status `ready` deltaP `42.6723` edge `0.1312` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.5314` n `98` status `ready` deltaP `16.8088` edge `0.4042` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.8846` n `106` status `ready` deltaP `23.165` edge `0.0451` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.4445` n `106` status `ready` deltaP `8.6718` edge `0.2019` maxDD `-4.48`
- `market_context_high->metal_1h` score `1.0586` n `106` status `ready` deltaP `14.7045` edge `0.0192` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.9001` n `106` status `ready` deltaP `11.366` edge `0.102` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.7974` n `106` status `ready` deltaP `7.8466` edge `0.1017` maxDD `-2.3383`
- `news_risk_high->crypto_alt_1h` score `0.4211` n `103` status `ready` deltaP `6.315` edge `0.0884` maxDD `-3.9659`
- `market_context_high->crypto_major_4h` score `0.3474` n `106` status `ready` deltaP `18.0396` edge `0.1827` maxDD `-14.5879`
- `market_context_high->fx_1h` score `0.1845` n `106` status `ready` deltaP `7.6376` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->metal_24h` score `0.1734` n `106` status `ready` deltaP `14.6128` edge `0.1895` maxDD `-10.5088`
- `market_context_high->fx_4h` score `0.0927` n `106` status `ready` deltaP `6.995` edge `0.0002` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `-0.02` n `106` status `ready` deltaP `10.0524` edge `0.0523` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.2244` n `106` status `ready` deltaP `5.1068` edge `0.0031` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.4507` n `106` status `ready` deltaP `3.8329` edge `0.0942` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
