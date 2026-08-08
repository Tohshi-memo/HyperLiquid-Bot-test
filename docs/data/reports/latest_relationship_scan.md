# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T14:52:27.930081+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.8939` n `95` status `ready` deltaP `3.1012` edge `0.6098` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6178` n `95` status `ready` deltaP `10.5665` edge `0.2053` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4374` n `103` status `ready` deltaP `13.6765` edge `0.0959` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.2469` n `95` status `ready` deltaP `28.1433` edge `0.0589` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9806` n `103` status `ready` deltaP `11.3874` edge `0.0401` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4006` n `95` status `ready` deltaP `6.811` edge `0.1591` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4508` n `103` status `ready` deltaP `3.5987` edge `0.0213` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4854` n `103` status `ready` deltaP `2.2048` edge `-0.0056` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5131` n `103` status `ready` deltaP `-3.6335` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.62` n `103` status `ready` deltaP `-1.2713` edge `-0.0105` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6475` n `103` status `ready` deltaP `-4.1596` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8613` n `103` status `ready` deltaP `1.3275` edge `-0.0053` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.055` n `103` status `ready` deltaP `-3.2204` edge `-0.0129` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.9087` n `103` status `ready` deltaP `2.7409` edge `-0.0436` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.9601` n `103` status `ready` deltaP `-11.0284` edge `-0.0269` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.4961` n `103` status `ready` deltaP `-8.1841` edge `-0.0538` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6515` n `95` status `ready` deltaP `4.5431` edge `-0.1208` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.098` n `95` status `ready` deltaP `-15.7164` edge `-0.1481` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2` n `103` status `ready` deltaP `-11.3412` edge `-0.1092` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.8871` n `103` status `ready` deltaP `-14.2538` edge `-0.2231` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
