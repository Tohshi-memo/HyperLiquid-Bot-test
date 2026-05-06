# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T23:22:21.023082+00:00`
- Price records: `497`
- Market context records: `590`
- Flow alert records: `1670`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.6256` n `146` status `ready` deltaP `7.0458` edge `0.3433` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.3924` n `146` status `ready` deltaP `10.484` edge `0.2462` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0968` n `146` status `ready` deltaP `11.888` edge `0.0203` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.289` n `146` status `ready` deltaP `2.4526` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6119` n `146` status `ready` deltaP `1.5239` edge `0.0363` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6418` n `146` status `ready` deltaP `0.8362` edge `-0.0025` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1648` n `146` status `ready` deltaP `-4.2346` edge `-0.0085` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2127` n `146` status `ready` deltaP `5.3572` edge `-0.0053` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2418` n `146` status `ready` deltaP `-1.8223` edge `-0.0103` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8433` n `146` status `ready` deltaP `4.6194` edge `-0.0121` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1453` n `146` status `ready` deltaP `2.8949` edge `0.0589` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2613` n `146` status `ready` deltaP `0.079` edge `-0.0367` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.2969` n `146` status `ready` deltaP `-6.4197` edge `0.0509` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.8754` n `146` status `ready` deltaP `12.0425` edge `0.0507` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.3027` n `146` status `ready` deltaP `-4.664` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3652` n `146` status `ready` deltaP `-3.9042` edge `-0.0392` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.737` n `146` status `ready` deltaP `-6.8435` edge `0.0843` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.3193` n `146` status `ready` deltaP `-10.2998` edge `-0.0308` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4086` n `146` status `ready` deltaP `-3.9785` edge `-0.0215` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0894` n `146` status `ready` deltaP `0.7048` edge `-0.241` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
