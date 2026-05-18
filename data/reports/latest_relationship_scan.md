# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T05:22:17.690255+00:00`
- Price records: `672`
- Market context records: `1087`
- Flow alert records: `5033`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8786`

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

- `market_context_high->crypto_major_24h` score `16.5919` n `156` status `ready` deltaP `35.5961` edge `1.1917` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.8235` n `156` status `ready` deltaP `12.2235` edge `0.5272` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.5822` n `156` status `ready` deltaP `14.8414` edge `0.4159` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.6651` n `156` status `ready` deltaP `-2.674` edge `0.5733` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5946` n `156` status `ready` deltaP `14.9679` edge `0.3139` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.8399` n `163` status `ready` deltaP `10.1274` edge `0.1563` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.1752` n `163` status `ready` deltaP `11.8257` edge `0.1877` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.9111` n `163` status `ready` deltaP `7.8184` edge `0.0921` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6748` n `174` status `ready` deltaP `8.8684` edge `0.0288` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5246` n `174` status `ready` deltaP `3.3725` edge `0.059` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1728` n `174` status `ready` deltaP `7.3749` edge `0.0418` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0537` n `174` status `ready` deltaP `7.3267` edge `0.0012` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1235` n `174` status `ready` deltaP `7.0566` edge `0.0037` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2191` n `174` status `ready` deltaP `3.1833` edge `0.0448` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3463` n `163` status `ready` deltaP `7.751` edge `0.1699` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6225` n `163` status `ready` deltaP `2.6307` edge `0.0023` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6617` n `174` status `ready` deltaP `-0.8019` edge `0.0013` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.8255` n `163` status `ready` deltaP `5.2746` edge `-0.0738` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.4236` n `163` status `ready` deltaP `8.2934` edge `-0.1356` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.1155` n `156` status `ready` deltaP `4.6367` edge `-0.0227` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
