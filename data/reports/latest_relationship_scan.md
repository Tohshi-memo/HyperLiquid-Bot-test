# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T19:52:16.595715+00:00`
- Price records: `672`
- Market context records: `1559`
- Flow alert records: `6397`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.5796` n `182` status `ready` deltaP `24.3379` edge `0.9861` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.9194` n `182` status `ready` deltaP `26.9974` edge `0.9316` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.4005` n `182` status `ready` deltaP `26.7399` edge `0.7183` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0488` n `182` status `ready` deltaP `20.7799` edge `0.3075` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9231` n `182` status `ready` deltaP `14.9363` edge `0.3767` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.5078` n `182` status `ready` deltaP `14.7932` edge `0.0486` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3941` n `199` status `ready` deltaP `5.5483` edge `0.1053` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.0343` n `199` status `ready` deltaP `13.2545` edge `0.2392` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.1625` n `199` status `ready` deltaP `9.1272` edge `0.1892` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2997` n `199` status `ready` deltaP `1.2668` edge `0.0555` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6499` n `199` status `ready` deltaP `-2.4433` edge `-0.0038` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7071` n `199` status `ready` deltaP `-0.1978` edge `0.0028` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.736` n `199` status `ready` deltaP `5.1478` edge `0.0049` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7416` n `199` status `ready` deltaP `0.0256` edge `0.0012` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.7672` n `199` status `ready` deltaP `-1.0328` edge `0.0238` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.8763` n `199` status `ready` deltaP `-0.4438` edge `0.0263` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.376` n `199` status `ready` deltaP `-10.3973` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4031` n `199` status `ready` deltaP `10.0587` edge `0.0852` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4206` n `199` status `ready` deltaP `-4.2875` edge `0.0191` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.0409` n `199` status `ready` deltaP `-13.4805` edge `-0.0937` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
