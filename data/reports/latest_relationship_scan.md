# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T17:07:27.693897+00:00`
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

- `market_context_high->equity_24h` score `3.0691` n `102` status `ready` deltaP `4.4015` edge `0.5324` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3834` n `102` status `ready` deltaP `11.8668` edge `0.1771` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5068` n `103` status `ready` deltaP `14.4387` edge `0.0966` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.0421` n `102` status `ready` deltaP `24.7141` edge `0.0555` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0337` n `104` status `ready` deltaP `12.0509` edge `0.0401` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3919` n `102` status `ready` deltaP `8.8337` edge `0.1445` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.5277` n `104` status `ready` deltaP `2.8328` edge `0.02` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.5681` n `104` status `ready` deltaP `1.2609` edge `-0.0062` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5721` n `104` status `ready` deltaP `-4.1283` edge `-0.0069` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.64` n `104` status `ready` deltaP `-4.0016` edge `-0.0058` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6904` n `103` status `ready` deltaP `-2.4909` edge `-0.0114` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8685` n `103` status `ready` deltaP `1.3275` edge `-0.0059` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9702` n `104` status `ready` deltaP `-11.0951` edge `-0.0273` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.0664` n `103` status `ready` deltaP `1.369` edge `-0.0476` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.1791` n `102` status `ready` deltaP `6.638` edge `-0.0742` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.4834` n `104` status `ready` deltaP `-7.9514` edge `-0.0543` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.8474` n `102` status `ready` deltaP `-12.8268` edge `-0.0908` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.336` n `103` status `ready` deltaP `-11.6461` edge `-0.1185` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0161` n `103` status `ready` deltaP `-14.7111` edge `-0.2308` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
