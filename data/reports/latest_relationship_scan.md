# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T09:07:28.172380+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11572`

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

- `market_context_high->equity_24h` score `6.1056` n `81` status `ready` deltaP `1.9483` edge `0.8018` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6887` n `81` status `ready` deltaP `12.2685` edge `0.2832` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7217` n `81` status `ready` deltaP `33.6034` edge `0.0667` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.5176` n `103` status `ready` deltaP `14.4387` edge `0.0975` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1448` n `81` status `ready` deltaP `7.0216` edge `0.1999` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.086` n `103` status `ready` deltaP `12.585` edge `0.0409` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3346` n `103` status `ready` deltaP `4.7963` edge `0.023` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.496` n `103` status `ready` deltaP `-3.3341` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5118` n `103` status `ready` deltaP `1.9054` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5448` n `103` status `ready` deltaP `0.1006` edge `-0.01` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6483` n `103` status `ready` deltaP `-4.1596` edge `-0.0058` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9163` n `103` status `ready` deltaP `0.5653` edge `-0.0048` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0811` n `103` status `ready` deltaP `-3.6778` edge `-0.0132` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.6879` n `103` status `ready` deltaP `4.5702` edge `-0.0374` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8019` n `103` status `ready` deltaP `-9.6811` edge `-0.0227` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.2911` n `103` status `ready` deltaP `-6.3877` edge `-0.0487` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6777` n `81` status `ready` deltaP `6.6937` edge `-0.1385` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.7339` n `103` status `ready` deltaP `-8.14` edge `-0.0917` maxDD `-6.5487`
- `market_context_high->crypto_alt_24h` score `-3.7818` n `81` status `ready` deltaP `-22.8202` edge `-0.1884` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.3978` n `103` status `ready` deltaP `-10.7477` edge `-0.2057` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
