# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T19:07:23.180017+00:00`
- Price records: `672`
- Market context records: `2486`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.3131` n `124` status `ready` deltaP `19.8869` edge `0.343` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.261` n `137` status `ready` deltaP `21.7175` edge `0.4782` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9549` n `137` status `ready` deltaP `18.5809` edge `0.3867` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.9256` n `124` status `ready` deltaP `11.0439` edge `0.5625` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.359` n `137` status `ready` deltaP `8.9806` edge `0.1569` maxDD `-3.6149`
- `market_context_high->crypto_major_1h` score `0.4929` n `148` status `ready` deltaP `7.5134` edge `0.1104` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.4781` n `148` status `ready` deltaP `6.4614` edge `0.1155` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0532` n `124` status `ready` deltaP `4.3514` edge `0.0735` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.1395` n `124` status `ready` deltaP `1.1032` edge `0.6705` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.1569` n `124` status `ready` deltaP `18.4084` edge `0.0169` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1984` n `137` status `ready` deltaP `5.7615` edge `0.0203` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3007` n `148` status `ready` deltaP `1.5779` edge `0.0044` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.4997` n `148` status `ready` deltaP `1.5779` edge `0.0198` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.5178` n `148` status `ready` deltaP `3.083` edge `0.0009` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.5988` n `137` status `ready` deltaP `0.0601` edge `0.0088` maxDD `-0.8774`
- `market_context_high->index_1h` score `-0.6` n `148` status `ready` deltaP `-0.6595` edge `0.0038` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.7413` n `148` status `ready` deltaP `1.1207` edge `0.0067` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.899` n `148` status `ready` deltaP `-0.6392` edge `0.0132` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9034` n `124` status `ready` deltaP `2.8506` edge `0.0037` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9511` n `137` status `ready` deltaP `3.238` edge `0.0379` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
