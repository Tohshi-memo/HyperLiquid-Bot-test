# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T07:52:35.157177+00:00`
- Price records: `672`
- Market context records: `5124`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `26.9278` n `66` status `ready` deltaP `28.851` edge `2.0859` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.4427` n `126` status `ready` deltaP `7.9817` edge `0.7145` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.0086` n `117` status `ready` deltaP `19.6008` edge `0.5556` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.2284` n `117` status `ready` deltaP `14.4622` edge `0.4992` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6373` n `117` status `ready` deltaP `12.203` edge `0.451` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9176` n `126` status `ready` deltaP `6.5583` edge `0.1289` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7578` n `126` status `ready` deltaP `8.2644` edge `0.1326` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.7343` n `126` status `ready` deltaP `8.0411` edge `0.0669` maxDD `-2.745`
- `market_context_high->commodity_24h` score `0.6541` n `66` status `ready` deltaP `17.4242` edge `0.116` maxDD `-7.5308`
- `market_context_high->equity_4h` score `0.4856` n `117` status `ready` deltaP `7.3849` edge `0.1551` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1899` n `126` status `ready` deltaP `7.3662` edge `0.0267` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0248` n `126` status `ready` deltaP `5.5556` edge `0.0154` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4047` n `117` status `ready` deltaP `4.3581` edge `0.0308` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6215` n `126` status `ready` deltaP `-2.1267` edge `-0.0014` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.6277` n `117` status `ready` deltaP `1.1191` edge `0.0531` maxDD `-4.6157`
- `market_context_high->commodity_1h` score `-0.9413` n `126` status `ready` deltaP `0.2091` edge `-0.0029` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0013` n `117` status `ready` deltaP `-3.2964` edge `0.0009` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.5014` n `66` status `ready` deltaP `-2.8567` edge `-0.0097` maxDD `-1.3761`
- `market_context_high->metal_24h` score `-1.5241` n `66` status `ready` deltaP `-0.7892` edge `0.1249` maxDD `-18.87`
- `market_context_high->commodity_4h` score `-2.6003` n `117` status `ready` deltaP `-1.5375` edge `-0.0313` maxDD `-7.6781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
