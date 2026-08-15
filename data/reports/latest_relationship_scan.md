# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T07:52:26.549964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.1098` n `128` status `ready` deltaP `-27.7554` edge `11.9021` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.4003` n `32` status `ready` deltaP `-41.0366` edge `4.6307` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.4003` n `32` status `ready` deltaP `-41.0366` edge `4.6307` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.001` n `36` status `ready` deltaP `21.6349` edge `0.8938` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5344` n `36` status `ready` deltaP `38.965` edge `0.3681` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0832` n `128` status `ready` deltaP `28.852` edge `0.237` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6593` n `32` status `ready` deltaP `31.1958` edge `0.1803` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6593` n `32` status `ready` deltaP `31.1958` edge `0.1803` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.13` n `32` status `ready` deltaP `27.5076` edge `0.4617` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.13` n `32` status `ready` deltaP `27.5076` edge `0.4617` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.1903` n `36` status `ready` deltaP `25.8232` edge `0.0937` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.837` n `32` status `ready` deltaP `20.4385` edge `0.1184` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.837` n `32` status `ready` deltaP `20.4385` edge `0.1184` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.8892` n `128` status `ready` deltaP `18.876` edge `0.0787` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7869` n `36` status `ready` deltaP `20.624` edge `0.0246` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6734` n `36` status `ready` deltaP `7.7728` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2701` n `32` status `ready` deltaP `13.4436` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2701` n `32` status `ready` deltaP `13.4436` edge `0.0395` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6336` n `128` status `ready` deltaP `8.7561` edge `0.0241` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5751` n `32` status `ready` deltaP `7.0253` edge `0.0152` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
