# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T13:52:27.050086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10809`

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

- `market_context_high->equity_24h` score `3.8484` n `103` status `ready` deltaP `4.5729` edge `0.5962` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4315` n `103` status `ready` deltaP `10.1285` edge `0.1927` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.185` n `143` status `ready` deltaP `15.0521` edge `0.0657` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7785` n `143` status `ready` deltaP `10.6916` edge `0.0279` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7169` n `103` status `ready` deltaP `21.4013` edge `0.0359` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4524` n `103` status `ready` deltaP `7.1905` edge `0.1632` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3481` n `143` status `ready` deltaP `3.6965` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3583` n `143` status `ready` deltaP `-0.3454` edge `-0.0047` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5199` n `143` status `ready` deltaP `5.3706` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6729` n `143` status `ready` deltaP `-4.5883` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.788` n `143` status `ready` deltaP `0.4563` edge `-0.0082` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8917` n `143` status `ready` deltaP `-0.0376` edge `0.0088` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9828` n `143` status `ready` deltaP `-1.2035` edge `-0.0171` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.906` n `143` status `ready` deltaP `-10.1336` edge `-0.0271` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3873` n `143` status `ready` deltaP `-0.0469` edge `-0.0649` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1699` n `143` status `ready` deltaP `-10.8371` edge `-0.0597` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.6601` n `143` status `ready` deltaP `-7.2095` edge `-0.0913` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.9682` n `103` status `ready` deltaP `2.2266` edge `-0.0961` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.178` n `103` status `ready` deltaP `-17.1336` edge `-0.2563` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8041` n `143` status `ready` deltaP `-5.9441` edge `-0.566` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
