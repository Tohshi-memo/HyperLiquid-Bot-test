# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T01:22:14.216420+00:00`
- Price records: `672`
- Market context records: `1274`
- Flow alert records: `5576`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.9929` n `128` status `ready` deltaP `41.5798` edge `1.3354` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.5558` n `128` status `ready` deltaP `6.25` edge `1.0047` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.8054` n `128` status `ready` deltaP `25.6076` edge `0.7647` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.5632` n `132` status `ready` deltaP `5.4878` edge `0.632` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.2245` n `128` status `ready` deltaP `27.2569` edge `0.3623` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8863` n `128` status `ready` deltaP `25.1736` edge `0.5631` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.5209` n `132` status `ready` deltaP `17.766` edge `0.2413` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3718` n `128` status `ready` deltaP `1.5625` edge `0.4602` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.7568` n `128` status `ready` deltaP `-12.5` edge `0.3779` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.7369` n `132` status `ready` deltaP `13.387` edge `0.1238` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.9733` n `132` status `ready` deltaP `18.616` edge `0.1001` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.5667` n `144` status `ready` deltaP `12.4751` edge `0.0251` maxDD `-2.2164`
- `market_context_high->index_1h` score `0.5296` n `144` status `ready` deltaP `8.4207` edge `0.0245` maxDD `-0.9206`
- `market_context_high->equity_1h` score `0.4679` n `144` status `ready` deltaP `5.2354` edge `0.0468` maxDD `-1.7505`
- `market_context_high->fx_24h` score `0.1198` n `128` status `ready` deltaP `3.9063` edge `0.0304` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `0.0701` n `132` status `ready` deltaP `7.9222` edge `0.1725` maxDD `-10.3058`
- `market_context_high->crypto_alt_1h` score `-0.3282` n `144` status `ready` deltaP `1.077` edge `0.0378` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.4143` n `144` status `ready` deltaP `2.0168` edge `-0.0024` maxDD `-0.3124`
- `market_context_high->crypto_alt_4h` score `-0.5633` n `132` status `ready` deltaP `8.6197` edge `0.1888` maxDD `-18.4789`
- `market_context_high->crypto_major_1h` score `-0.7143` n `144` status `ready` deltaP `0.7485` edge `0.0055` maxDD `-5.8323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
