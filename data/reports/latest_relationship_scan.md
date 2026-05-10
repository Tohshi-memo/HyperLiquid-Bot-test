# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T09:16:55.826035+00:00`
- Price records: `672`
- Market context records: `960`
- Flow alert records: `2691`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.9054` n `155` status `ready` deltaP `33.4061` edge `1.0528` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.0194` n `155` status `ready` deltaP `9.7222` edge `0.6868` maxDD `0.0`
- `market_context_high->equity_24h` score `1.215` n `155` status `ready` deltaP `1.7742` edge `0.3499` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.475` n `155` status `ready` deltaP `0.2845` edge `0.2372` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3572` n `204` status `ready` deltaP `1.6908` edge `0.001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.387` n `204` status `ready` deltaP `1.6995` edge `0.0372` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.5123` n `204` status `ready` deltaP `2.5008` edge `0.0175` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6732` n `192` status `ready` deltaP `1.7149` edge `0.0019` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7231` n `204` status `ready` deltaP `2.8942` edge `0.0058` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2219` n `192` status `ready` deltaP `2.6677` edge `0.0956` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3521` n `204` status `ready` deltaP `-2.9412` edge `-0.0159` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.5047` n `192` status `ready` deltaP `-0.0635` edge `0.0273` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.5894` n `204` status `ready` deltaP `6.4283` edge `-0.003` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.7971` n `204` status `ready` deltaP `2.2514` edge `-0.0208` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.8962` n `204` status `ready` deltaP `-2.5155` edge `-0.0304` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.4569` n `192` status `ready` deltaP `8.9939` edge `0.1059` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.4875` n `192` status `ready` deltaP `-0.7749` edge `0.0813` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2676` n `192` status `ready` deltaP `-2.2485` edge `0.0205` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3528` n `192` status `ready` deltaP `6.2881` edge `-0.1335` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.1088` n `155` status `ready` deltaP `6.2859` edge `-0.0181` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
