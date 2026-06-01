# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T07:37:19.523839+00:00`
- Price records: `672`
- Market context records: `2541`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_major_24h` score `5.3578` n `116` status `ready` deltaP `13.2663` edge `0.6366` maxDD `-17.2848`
- `market_context_high->crypto_alt_4h` score `5.2202` n `154` status `ready` deltaP `23.6419` edge `0.5453` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.1726` n `116` status `ready` deltaP `19.3307` edge `0.335` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.6402` n `154` status `ready` deltaP `16.8831` edge `0.3718` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.8634` n `154` status `ready` deltaP `10.6885` edge `0.189` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.2766` n `116` status `ready` deltaP `20.546` edge `0.0486` maxDD `-3.6684`
- `market_context_high->crypto_alt_1h` score `1.0714` n `154` status `ready` deltaP `9.2426` edge `0.1464` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.615` n `154` status `ready` deltaP `7.7942` edge `0.1187` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.3792` n `116` status `ready` deltaP `4.5259` edge `0.0995` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.1151` n `116` status `ready` deltaP `-0.1556` edge `0.6852` maxDD `-41.5528`
- `market_context_high->unknown_1h` score `-0.0811` n `154` status `ready` deltaP `3.6978` edge `0.0376` maxDD `-2.8543`
- `market_context_high->index_4h` score `-0.1463` n `154` status `ready` deltaP `6.054` edge `0.0316` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.3226` n `154` status `ready` deltaP `2.403` edge `0.0065` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3558` n `154` status `ready` deltaP `4.0983` edge `0.0149` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4092` n `154` status `ready` deltaP `1.5476` edge `0.012` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.4798` n `154` status `ready` deltaP `1.3493` edge `0.0045` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.8058` n `154` status `ready` deltaP `3.8842` edge `0.0457` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.813` n `154` status `ready` deltaP `-0.0894` edge `0.0167` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8718` n `154` status `ready` deltaP `0.1524` edge `0.0123` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8937` n `116` status `ready` deltaP `2.4365` edge `0.0031` maxDD `-2.3798`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
