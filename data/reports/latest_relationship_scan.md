# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T16:07:23.260258+00:00`
- Price records: `672`
- Market context records: `2473`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `market_context_high->unknown_24h` score `5.6112` n `117` status `ready` deltaP `22.1287` edge `0.3529` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9919` n `136` status `ready` deltaP `20.5882` edge `0.4633` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8395` n `136` status `ready` deltaP `18.0236` edge `0.3808` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2875` n `117` status `ready` deltaP `12.1395` edge `0.6016` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6435` n `136` status `ready` deltaP `10.4556` edge `0.1693` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.7985` n `137` status `ready` deltaP `8.769` edge `0.1275` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.6362` n `137` status `ready` deltaP `7.0283` edge `0.1249` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.076` n `117` status `ready` deltaP `1.9632` edge `0.6924` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0437` n `117` status `ready` deltaP `3.3921` edge `0.0791` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.152` n `136` status `ready` deltaP `6.25` edge `0.023` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.3078` n `117` status `ready` deltaP `17.5882` edge `0.0098` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.3622` n `137` status `ready` deltaP `0.365` edge `0.0046` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.4595` n `137` status `ready` deltaP `-1.7866` edge `0.0024` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4735` n `137` status `ready` deltaP `0.5518` edge `0.0074` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.5714` n `137` status `ready` deltaP `2.5176` edge `-0.0022` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.5947` n `137` status `ready` deltaP `0.7955` edge `0.0171` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6706` n `136` status `ready` deltaP `-1.2464` edge `0.0083` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.7636` n `137` status `ready` deltaP `0.4983` edge `0.0169` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8035` n `117` status `ready` deltaP `4.6207` edge `0.0047` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9612` n `136` status `ready` deltaP `2.977` edge `0.0388` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
