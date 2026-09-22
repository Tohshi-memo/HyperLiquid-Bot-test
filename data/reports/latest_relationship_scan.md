# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T20:10:15.992452+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9378`

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

- `market_context_high->unknown_4h` score `45.7338` n `46` status `ready` deltaP `7.0122` edge `3.7644` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4568` n `46` status `ready` deltaP `12.6661` edge `2.3859` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2181` n `46` status `ready` deltaP `12.1453` edge `1.2806` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.9276` n `46` status `ready` deltaP `11.2847` edge `1.0854` maxDD `0.0`
- `market_context_high->index_24h` score `5.5227` n `46` status `ready` deltaP `19.6105` edge `0.3382` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.2539` n `96` status `ready` deltaP `39.0625` edge `0.2953` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.7633` n `96` status `ready` deltaP `-10.0694` edge `1.1499` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9703` n `96` status `ready` deltaP `14.6341` edge `0.2077` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.9211` n `96` status `ready` deltaP `11.4329` edge `0.267` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.209` n `96` status `ready` deltaP `12.4314` edge `0.1366` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.862` n `46` status `ready` deltaP `22.2494` edge `0.0202` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5518` n `96` status `ready` deltaP `13.9284` edge `0.0758` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.1966` n `96` status `ready` deltaP `18.5722` edge `0.0395` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `1.0366` n `96` status `ready` deltaP `-8.507` edge `0.6312` maxDD `-32.7147`
- `market_context_high->metal_24h` score `0.9918` n `46` status `ready` deltaP `21.9203` edge `-0.0401` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7118` n `46` status `ready` deltaP `6.4632` edge `0.0405` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5933` n `96` status `ready` deltaP `14.7268` edge `0.0106` maxDD `-0.7468`
- `news_risk_high->fx_24h` score `0.5808` n `96` status `ready` deltaP `20.3125` edge `0.098` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.4756` n `96` status `ready` deltaP `18.75` edge `0.0204` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
