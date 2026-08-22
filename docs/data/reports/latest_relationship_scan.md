# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T23:52:26.563048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_1h` score `2.3744` n `33` status `ready` deltaP `29.0828` edge `0.0158` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.7359` n `137` status `ready` deltaP `6.0569` edge `0.127` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.6701` n `33` status `ready` deltaP `22.3145` edge `0.0074` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.2284` n `137` status `ready` deltaP `20.3011` edge `-0.0033` maxDD `-0.3736`
- `news_risk_high->commodity_1h` score `0.9698` n `33` status `ready` deltaP `22.4642` edge `-0.0071` maxDD `-0.4666`
- `news_risk_high->equity_1h` score `0.8914` n `33` status `ready` deltaP `19.7333` edge `0.0109` maxDD `-0.9204`
- `market_context_high->fx_4h` score `0.131` n `137` status `ready` deltaP `8.6901` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0734` n `137` status `ready` deltaP `5.9236` edge `0.0042` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.14` n `137` status `ready` deltaP `2.0314` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3722` n `137` status `ready` deltaP `3.9403` edge `0.033` maxDD `-5.2257`
- `news_risk_high->metal_1h` score `-0.383` n `33` status `ready` deltaP `-2.5631` edge `-0.0097` maxDD `-0.1184`
- `market_context_high->metal_4h` score `-0.4266` n `137` status `ready` deltaP `6.4269` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.5562` n `137` status `ready` deltaP `0.047` edge `-0.0048` maxDD `-0.6822`
- `news_risk_high->crypto_major_1h` score `-0.5729` n `33` status `ready` deltaP `8.8823` edge `-0.0449` maxDD `-5.0209`
- `market_context_high->index_4h` score `-0.6259` n `137` status `ready` deltaP `1.9216` edge `0.0105` maxDD `-2.618`
- `news_risk_high->index_1h` score `-0.8036` n `33` status `ready` deltaP `-10.157` edge `0.0` maxDD `-0.1583`
- `market_context_high->fx_24h` score `-0.9115` n `121` status `ready` deltaP `0.7877` edge `0.0085` maxDD `-2.1153`
- `market_context_high->commodity_4h` score `-1.0268` n `137` status `ready` deltaP `-6.7206` edge `-0.0018` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.098` n `137` status `ready` deltaP `-8.0379` edge `-0.0024` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `-1.3462` n `137` status `ready` deltaP `7.5641` edge `-0.0158` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
