# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T05:52:25.466460+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8811`

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

- `market_context_high->equity_24h` score `3.6036` n `103` status `ready` deltaP `4.5729` edge `0.5758` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7067` n `103` status `ready` deltaP `13.2535` edge `0.1948` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3688` n `137` status `ready` deltaP `15.6846` edge `0.0768` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.896` n `143` status `ready` deltaP `11.2904` edge `0.0337` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8196` n `103` status `ready` deltaP `21.575` edge `0.0479` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5501` n `103` status `ready` deltaP `9.1002` edge `0.163` maxDD `-5.9181`
- `market_context_high->fx_4h` score `-0.2596` n `137` status `ready` deltaP `8.3385` edge `-0.0019` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.3049` n `143` status `ready` deltaP `4.1456` edge `-0.0035` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4867` n `143` status `ready` deltaP `-2.5909` edge `-0.0062` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6553` n `137` status `ready` deltaP `-1.8749` edge `-0.011` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.7111` n `143` status `ready` deltaP `-5.1871` edge `-0.007` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9709` n `143` status `ready` deltaP `-0.3371` edge `0.0042` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0766` n `137` status `ready` deltaP `-2.7661` edge `-0.0187` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.984` n `143` status `ready` deltaP `-10.5827` edge `-0.0306` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6926` n `137` status `ready` deltaP `-2.7984` edge `-0.072` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1975` n `143` status `ready` deltaP `-10.6874` edge `-0.063` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.2467` n `103` status `ready` deltaP `6.2197` edge `-0.0626` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.8517` n `137` status `ready` deltaP `-7.9547` edge `-0.1023` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.5742` n `103` status `ready` deltaP `-12.4461` edge `-0.1539` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.0644` n `143` status `ready` deltaP `-6.2435` edge `-0.5857` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
