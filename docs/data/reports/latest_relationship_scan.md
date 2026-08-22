# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T12:37:30.875284+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.98` n `145` status `ready` deltaP `7.3478` edge `0.0554` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2219` n `137` status `ready` deltaP `18.4808` edge `-0.0608` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.09` n `137` status `ready` deltaP `7.7844` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0241` n `145` status `ready` deltaP `7.7225` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0069` n `145` status `ready` deltaP `4.5148` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2682` n `137` status `ready` deltaP `6.6761` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3226` n `145` status `ready` deltaP `0.8259` edge `-0.005` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3546` n `145` status `ready` deltaP `4.3382` edge `0.0326` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5101` n `137` status `ready` deltaP `4.0146` edge `0.0114` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7435` n `137` status `ready` deltaP `-2.0685` edge `0.0035` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9146` n `145` status `ready` deltaP `-6.9688` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6994` n `137` status `ready` deltaP `-0.9836` edge `0.0692` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.7696` n `137` status `ready` deltaP `4.9815` edge `-0.0527` maxDD `-5.5715`
- `market_context_high->fx_24h` score `-1.8187` n `123` status `ready` deltaP `0.0635` edge `0.009` maxDD `-2.2121`
- `market_context_high->commodity_24h` score `-1.9851` n `123` status `ready` deltaP `-5.31` edge `0.0533` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.408` n `145` status `ready` deltaP `-2.3983` edge `-0.0352` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4354` n `145` status `ready` deltaP `-4.7718` edge `-0.1086` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.4892` n `123` status `ready` deltaP `-8.363` edge `-0.0453` maxDD `-20.6255`
- `market_context_high->metal_24h` score `-5.4489` n `123` status `ready` deltaP `-24.4918` edge `-0.2045` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.4729` n `137` status `ready` deltaP `-1.1305` edge `-0.3189` maxDD `-5.3711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
