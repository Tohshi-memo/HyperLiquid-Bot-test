# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T08:19:22.905268+00:00`
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

- `market_context_high->equity_24h` score `6.102` n `81` status `ready` deltaP `1.9483` edge `0.8015` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6279` n `81` status `ready` deltaP `11.7477` edge `0.2816` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7225` n `81` status `ready` deltaP `33.6034` edge `0.0668` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.5578` n `103` status `ready` deltaP `14.8961` edge `0.0978` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1376` n `81` status `ready` deltaP `7.0216` edge `0.1993` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.086` n `103` status `ready` deltaP `12.585` edge `0.0409` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2927` n `103` status `ready` deltaP `5.2454` edge `0.0235` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4789` n `103` status `ready` deltaP `-3.0347` edge `-0.0064` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5118` n `103` status `ready` deltaP `1.9054` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5361` n `103` status `ready` deltaP `0.253` edge `-0.0099` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6405` n `103` status `ready` deltaP `-4.0099` edge `-0.0058` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9297` n `103` status `ready` deltaP `0.4129` edge `-0.0049` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0645` n `103` status `ready` deltaP `-3.3729` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.6745` n `103` status `ready` deltaP `4.7227` edge `-0.0373` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.772` n `103` status `ready` deltaP `-9.3817` edge `-0.0222` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.2444` n `103` status `ready` deltaP `-5.9386` edge `-0.0478` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6562` n `81` status `ready` deltaP `6.8673` edge `-0.1369` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.7255` n `103` status `ready` deltaP `-8.14` edge `-0.091` maxDD `-6.5487`
- `market_context_high->crypto_alt_24h` score `-3.7818` n `81` status `ready` deltaP `-22.8202` edge `-0.1884` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.348` n `103` status `ready` deltaP `-10.2904` edge `-0.2046` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
