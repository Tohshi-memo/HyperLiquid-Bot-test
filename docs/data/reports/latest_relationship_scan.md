# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T10:52:29.580745+00:00`
- Price records: `672`
- Market context records: `6383`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.1517` n `32` status `ready` deltaP `37.6736` edge `0.9429` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4035` n `32` status `ready` deltaP `53.2986` edge `0.1783` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.295` n `32` status `ready` deltaP `17.5347` edge `0.5117` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.255` n `32` status `ready` deltaP `36.9792` edge `0.1286` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9352` n `32` status `ready` deltaP `40.625` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3847` n `32` status `ready` deltaP `28.7425` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5286` n `32` status `ready` deltaP `14.8765` edge `0.1435` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8769` n `32` status `ready` deltaP `11.0217` edge `0.0851` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4894` n `219` status `ready` deltaP `15.1353` edge `0.0415` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1697` n `219` status `ready` deltaP `9.042` edge `0.0215` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `0.1371` n `228` status `ready` deltaP `-5.904` edge `0.1516` maxDD `-3.7317`
- `news_risk_high->unknown_1h` score `-0.2057` n `32` status `ready` deltaP `6.9798` edge `-0.0292` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2437` n `146` status `ready` deltaP `19.6205` edge `0.0948` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4042` n `228` status `ready` deltaP `3.4563` edge `0.0029` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6401` n `228` status `ready` deltaP `-1.9356` edge `0.0028` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6454` n `228` status `ready` deltaP `-1.9251` edge `-0.0016` maxDD `-2.1314`
- `news_risk_high->metal_1h` score `-0.7014` n `32` status `ready` deltaP `-2.2455` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7101` n `228` status `ready` deltaP `-0.6435` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7354` n `32` status `ready` deltaP `0.5208` edge `-0.0106` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.8655` n `219` status `ready` deltaP `7.2238` edge `0.0496` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
