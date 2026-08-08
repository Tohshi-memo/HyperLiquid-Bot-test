# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T16:16:05.365598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11590`

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

- `market_context_high->equity_24h` score `3.1607` n `101` status `ready` deltaP `4.2268` edge `0.5412` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4066` n `101` status `ready` deltaP `11.6921` edge `0.1802` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4958` n `103` status `ready` deltaP `14.2863` edge `0.0967` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.1002` n `101` status `ready` deltaP `25.7116` edge `0.0563` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0373` n `104` status `ready` deltaP `12.0509` edge `0.0404` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3887` n `101` status `ready` deltaP `8.5619` edge `0.1459` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.5145` n `104` status `ready` deltaP `2.9825` edge `0.0201` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.5418` n `104` status `ready` deltaP `1.5603` edge `-0.006` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5713` n `104` status `ready` deltaP `-4.1283` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6237` n `104` status `ready` deltaP `-3.7022` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6635` n `103` status `ready` deltaP `-2.0335` edge `-0.011` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8795` n `103` status `ready` deltaP `1.1751` edge `-0.0058` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0225` n `103` status `ready` deltaP `-2.6107` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9642` n `104` status `ready` deltaP `-11.0951` edge `-0.0268` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.0118` n `103` status `ready` deltaP `1.8263` edge `-0.0461` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.2148` n `101` status `ready` deltaP `6.3565` edge `-0.0769` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.4798` n `104` status `ready` deltaP `-7.9514` edge `-0.054` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-2.567` n `101` status `ready` deltaP `-13.2151` edge `-0.0967` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2952` n `103` status `ready` deltaP `-11.6461` edge `-0.1151` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.9945` n `103` status `ready` deltaP `-14.7111` edge `-0.229` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
