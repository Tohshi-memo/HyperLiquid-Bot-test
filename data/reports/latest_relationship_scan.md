# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T08:52:29.830917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `market_context_high->crypto_alt_24h` score `12.6699` n `40` status `ready` deltaP `51.4583` edge `0.7525` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9163` n `40` status `ready` deltaP `51.1458` edge `0.5815` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.3351` n `32` status `ready` deltaP `-8.0793` edge `0.2394` maxDD `-3.2755`
- `news_risk_high->commodity_1h` score `0.7867` n `32` status `ready` deltaP `17.122` edge `0.0079` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.7635` n `32` status `ready` deltaP `11.2847` edge `0.0578` maxDD `-1.5526`
- `news_risk_high->commodity_4h` score `0.5439` n `32` status `ready` deltaP `15.0152` edge `-0.0047` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.2972` n `47` status `ready` deltaP `6.8161` edge `0.0301` maxDD `-1.3282`
- `news_risk_high->crypto_alt_1h` score `0.2822` n `32` status `ready` deltaP `13.5479` edge `0.0099` maxDD `-3.1233`
- `market_context_high->commodity_4h` score `0.2682` n `47` status `ready` deltaP `4.5764` edge `0.0885` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1487` n `32` status `ready` deltaP `-1.372` edge `0.0596` maxDD `-0.3783`
- `news_risk_high->index_1h` score `0.0965` n `32` status `ready` deltaP `5.0524` edge `-0.0015` maxDD `-0.5845`
- `news_risk_high->fx_4h` score `0.0928` n `32` status `ready` deltaP `4.6494` edge `0.0356` maxDD `-0.3761`
- `market_context_high->fx_1h` score `-0.0014` n `47` status `ready` deltaP `7.1155` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.0487` n `47` status `ready` deltaP `12.9606` edge `-0.0048` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.233` n `47` status `ready` deltaP `2.1439` edge `0.0464` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.3316` n `32` status `ready` deltaP `-1.1976` edge `-0.0026` maxDD `-0.5538`
- `news_risk_high->fx_1h` score `-0.4501` n `32` status `ready` deltaP `-1.3286` edge `0.0025` maxDD `-0.1588`
- `news_risk_high->crypto_major_1h` score `-0.5415` n `32` status `ready` deltaP `5.3705` edge `-0.0332` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-0.8699` n `32` status `ready` deltaP `-8.3458` edge `0.0264` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
