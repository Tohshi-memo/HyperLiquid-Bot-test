# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T16:21:21.763691+00:00`
- Price records: `672`
- Market context records: `2474`
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

- `market_context_high->unknown_24h` score `5.4996` n `118` status `ready` deltaP `21.4984` edge `0.3478` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0087` n `136` status `ready` deltaP `20.5882` edge `0.4647` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8395` n `136` status `ready` deltaP `18.0236` edge `0.3808` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2558` n `118` status `ready` deltaP `12.4147` edge `0.5957` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6495` n `136` status `ready` deltaP `10.4556` edge `0.1698` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.7901` n `137` status `ready` deltaP `8.769` edge `0.1268` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.6302` n `137` status `ready` deltaP `7.0283` edge `0.1244` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.04` n `118` status `ready` deltaP `3.6311` edge `0.0772` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.0036` n `118` status `ready` deltaP `1.6949` edge `0.6849` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1646` n `136` status `ready` deltaP `6.0976` edge `0.0224` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2931` n `118` status `ready` deltaP `17.7113` edge `0.0102` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.3622` n `137` status `ready` deltaP `0.365` edge `0.0046` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.4712` n `137` status `ready` deltaP `-1.9363` edge `0.0019` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4766` n `137` status `ready` deltaP `0.5518` edge `0.007` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.5643` n `137` status `ready` deltaP `2.5176` edge `-0.0013` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.5647` n `137` status `ready` deltaP `0.9452` edge `0.0186` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6619` n `136` status `ready` deltaP `-1.094` edge `0.0084` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.7828` n `137` status `ready` deltaP `0.3486` edge `0.0163` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8258` n `118` status `ready` deltaP `4.2079` edge `0.0046` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9648` n `136` status `ready` deltaP `2.977` edge `0.0385` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
