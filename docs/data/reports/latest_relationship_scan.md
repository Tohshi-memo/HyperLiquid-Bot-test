# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T21:22:30.506757+00:00`
- Price records: `672`
- Market context records: `8552`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5192.5648` n `60` status `ready` deltaP `41.5972` edge `432.4785` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5733` n `64` status `ready` deltaP `20.0457` edge `0.3905` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9403` n `64` status `ready` deltaP `15.8918` edge `0.0748` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.9016` n `62` status `ready` deltaP `13.3605` edge `0.1651` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7253` n `64` status `ready` deltaP `16.2519` edge `0.0831` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9958` n `64` status `ready` deltaP `6.4405` edge `0.1623` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6451` n `64` status `ready` deltaP `12.9573` edge `0.1355` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4734` n `64` status `ready` deltaP `8.4113` edge `0.0573` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3438` n `64` status `ready` deltaP `6.7646` edge `0.0502` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0815` n `64` status `ready` deltaP `5.1366` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0223` n `64` status `ready` deltaP `3.9203` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.0416` n `64` status `ready` deltaP `10.7088` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0506` n `64` status `ready` deltaP `1.5625` edge `0.0307` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1239` n `64` status `ready` deltaP `3.4057` edge `0.0073` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.2098` n `62` status `ready` deltaP `7.5334` edge `0.0119` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `-0.2779` n `62` status `ready` deltaP `4.4572` edge `-0.0028` maxDD `-2.0038`
- `market_context_high->fx_1h` score `-0.2832` n `62` status `ready` deltaP `2.062` edge `0.0002` maxDD `-0.6874`
- `market_context_high->crypto_alt_1h` score `-0.5034` n `62` status `ready` deltaP `-2.627` edge `0.0157` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7489` n `62` status `ready` deltaP `0.9465` edge `-0.0158` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9649` n `62` status `ready` deltaP `-2.8443` edge `-0.012` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
