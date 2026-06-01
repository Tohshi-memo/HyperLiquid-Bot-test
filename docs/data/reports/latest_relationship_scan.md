# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T06:52:19.662206+00:00`
- Price records: `672`
- Market context records: `2538`
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

- `market_context_high->crypto_alt_4h` score `5.1185` n `157` status `ready` deltaP `23.7057` edge `0.5364` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.7718` n `116` status `ready` deltaP `19.3307` edge `0.3016` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.5811` n `157` status `ready` deltaP `17.0586` edge `0.3657` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.0937` n `116` status `ready` deltaP `13.2663` edge `0.6298` maxDD `-20.7292`
- `market_context_high->unknown_4h` score `1.9203` n `157` status `ready` deltaP `11.1902` edge `0.1904` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1358` n `157` status `ready` deltaP `9.6876` edge `0.1488` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6453` n `157` status `ready` deltaP `8.2641` edge `0.1181` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.6376` n `116` status `ready` deltaP `19.1691` edge `0.036` maxDD `-5.1864`
- `market_context_high->index_24h` score `0.0709` n `116` status `ready` deltaP `3.8374` edge `0.0784` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.0085` n `116` status `ready` deltaP `0.5328` edge `0.6813` maxDD `-42.7009`
- `market_context_high->index_4h` score `-0.0857` n `157` status `ready` deltaP `6.7365` edge `0.0321` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.2274` n `157` status `ready` deltaP `3.4298` edge `0.0272` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.318` n `157` status `ready` deltaP `2.235` edge `0.008` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3316` n `157` status `ready` deltaP `4.4424` edge `0.0157` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4015` n `157` status `ready` deltaP `2.2674` edge `0.0049` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.4829` n `157` status `ready` deltaP `0.7294` edge `0.008` maxDD `-2.9823`
- `market_context_high->fx_4h` score `-0.826` n `157` status `ready` deltaP `0.6505` edge `0.0128` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8322` n `157` status `ready` deltaP `-0.2688` edge `0.0163` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8571` n `116` status `ready` deltaP `3.125` edge `0.0036` maxDD `-2.4117`
- `market_context_high->metal_4h` score `-0.9031` n `157` status `ready` deltaP `2.9536` edge `0.0438` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
