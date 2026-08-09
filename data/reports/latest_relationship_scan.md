# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T01:22:37.313977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.2028` n `103` status `ready` deltaP `4.5729` edge `0.5424` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5782` n `103` status `ready` deltaP `12.9062` edge `0.1864` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4118` n `119` status `ready` deltaP `13.7913` edge `0.093` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8505` n `103` status `ready` deltaP `22.0958` edge `0.0484` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.8424` n `131` status `ready` deltaP `10.3053` edge `0.0358` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4783` n `103` status `ready` deltaP `9.1002` edge `0.1538` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4073` n `131` status `ready` deltaP `2.9712` edge `-0.0042` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.5524` n `119` status `ready` deltaP `4.919` edge `-0.0035` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.5853` n `119` status `ready` deltaP `-0.2446` edge `-0.0129` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6091` n `131` status `ready` deltaP `-3.2865` edge `-0.0066` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.7626` n `131` status `ready` deltaP `-2.6877` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.7973` n `131` status `ready` deltaP `1.4124` edge `0.007` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0567` n `119` status `ready` deltaP `-2.758` edge `-0.0162` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0685` n `131` status `ready` deltaP `-11.2344` edge `-0.0333` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.2235` n `119` status `ready` deltaP `2.1354` edge `-0.0658` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0051` n `131` status `ready` deltaP `-9.7819` edge `-0.064` maxDD `-6.3636`
- `market_context_high->crypto_major_24h` score `-3.7027` n `103` status `ready` deltaP `6.2197` edge `-0.1006` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4698` n `103` status `ready` deltaP `-12.4461` edge `-0.1452` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.6238` n `119` status `ready` deltaP `-12.2438` edge `-0.1385` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.2727` n `131` status `ready` deltaP `-5.2464` edge `-0.6097` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
