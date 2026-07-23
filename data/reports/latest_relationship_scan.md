# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T14:22:27.069386+00:00`
- Price records: `672`
- Market context records: `7676`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14675`

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

- `market_context_high->index_1h` score `0.014` n `145` status `ready` deltaP `5.7451` edge `0.0114` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1284` n `145` status `ready` deltaP `8.3213` edge `0.0241` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1992` n `145` status `ready` deltaP `2.4726` edge `0.0212` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.2895` n `144` status `ready` deltaP `9.7706` edge `0.0195` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4287` n `145` status `ready` deltaP `4.694` edge `0.0511` maxDD `-6.9884`
- `market_context_high->commodity_1h` score `-0.4292` n `145` status `ready` deltaP `0.8739` edge `-0.0039` maxDD `-1.5561`
- `market_context_high->metal_1h` score `-0.6161` n `145` status `ready` deltaP `1.4196` edge `0.0161` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.688` n `145` status `ready` deltaP `7.7781` edge `0.0281` maxDD `-3.1189`
- `market_context_high->fx_1h` score `-0.7597` n `145` status `ready` deltaP `-1.691` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_4h` score `-0.7823` n `145` status `ready` deltaP `0.3828` edge `0.0003` maxDD `-1.7768`
- `market_context_high->crypto_alt_4h` score `-0.8277` n `145` status `ready` deltaP `3.5607` edge `0.0613` maxDD `-9.2919`
- `market_context_high->crypto_major_4h` score `-0.9473` n `145` status `ready` deltaP `10.1524` edge `0.0679` maxDD `-13.563`
- `market_context_high->commodity_24h` score `-1.3265` n `144` status `ready` deltaP `7.2009` edge `-0.0002` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5353` n `145` status `ready` deltaP `-1.6333` edge `-0.0547` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6355` n `145` status `ready` deltaP `-2.2687` edge `0.0486` maxDD `-4.4521`
- `market_context_high->equity_4h` score `-1.6429` n `145` status `ready` deltaP `-0.3416` edge `0.1789` maxDD `-18.647`
- `market_context_high->metal_24h` score `-2.1082` n `145` status `ready` deltaP `-2.8568` edge `0.0613` maxDD `-6.67`
- `market_context_high->equity_24h` score `-2.2723` n `144` status `ready` deltaP `12.4516` edge `0.0527` maxDD `-29.496`
- `market_context_high->fx_4h` score `-2.6369` n `145` status `ready` deltaP `-7.0294` edge `-0.005` maxDD `-2.0973`
- `market_context_high->index_24h` score `-3.5971` n `144` status `ready` deltaP `-21.5471` edge `-0.0414` maxDD `-7.4228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
