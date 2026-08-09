# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T02:37:27.600239+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.3324` n `103` status `ready` deltaP `4.5729` edge `0.5532` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6431` n `103` status `ready` deltaP `13.2535` edge `0.1895` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.431` n `124` status `ready` deltaP `14.4522` edge `0.0902` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8933` n `136` status `ready` deltaP `11.0162` edge `0.0353` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8474` n `103` status `ready` deltaP `22.0958` edge `0.048` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5002` n `103` status `ready` deltaP `9.1002` edge `0.1566` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3341` n `136` status `ready` deltaP `3.8262` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.4258` n `124` status `ready` deltaP `6.427` edge `-0.003` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.568` n `124` status `ready` deltaP `0.0737` edge `-0.0128` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6847` n `136` status `ready` deltaP `-4.6803` edge `-0.007` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.8404` n `136` status `ready` deltaP `-3.6456` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9246` n `136` status `ready` deltaP `0.2113` edge `0.0044` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0149` n `124` status `ready` deltaP `-1.8195` edge `-0.0171` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1001` n `136` status `ready` deltaP `-11.7339` edge `-0.0326` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4238` n `124` status `ready` deltaP `0.1868` edge `-0.0695` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1535` n `136` status `ready` deltaP `-10.6331` edge `-0.0647` maxDD `-6.8427`
- `market_context_high->crypto_major_24h` score `-3.5851` n `103` status `ready` deltaP `6.2197` edge `-0.0908` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.489` n `103` status `ready` deltaP `-12.4461` edge `-0.1468` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.5776` n `124` status `ready` deltaP `-12.0033` edge `-0.1358` maxDD `-6.585`
- `market_context_high->unknown_1h` score `-8.2646` n `136` status `ready` deltaP `-5.1603` edge `-0.6096` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
