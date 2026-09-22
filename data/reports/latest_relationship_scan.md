# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T17:07:30.321281+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `46.5258` n `46` status `ready` deltaP `7.0122` edge `3.8304` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.0905` n `46` status `ready` deltaP `13.8814` edge `2.4306` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2752` n `46` status `ready` deltaP `12.3189` edge `1.2842` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.1514` n `46` status `ready` deltaP `13.3681` edge `1.1735` maxDD `0.0`
- `market_context_high->index_24h` score `5.5656` n `46` status `ready` deltaP `20.1314` edge `0.3383` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.2072` n `100` status `ready` deltaP `37.7986` edge `0.2818` maxDD `-2.8089`
- `news_risk_high->crypto_major_24h` score `3.0176` n `100` status `ready` deltaP `-10.7708` edge `1.0091` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `2.2352` n `100` status `ready` deltaP `10.8598` edge `0.2182` maxDD `-6.3463`
- `news_risk_high->crypto_alt_1h` score `2.0174` n `100` status `ready` deltaP `12.6707` edge `0.1302` maxDD `-2.058`
- `market_context_high->index_4h` score `1.8692` n `46` status `ready` deltaP `22.2494` edge `0.0208` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.6057` n `100` status `ready` deltaP `13.9085` edge `0.15` maxDD `-6.713`
- `news_risk_high->crypto_major_1h` score `1.2872` n `100` status `ready` deltaP `14.018` edge `0.0661` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.1909` n `100` status `ready` deltaP `18.7256` edge `0.038` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.1869` n `46` status `ready` deltaP `23.3092` edge `-0.0331` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.834` n `46` status `ready` deltaP `7.3614` edge `0.0447` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6579` n `46` status `ready` deltaP `10.5051` edge `0.0101` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6326` n `100` status `ready` deltaP `15.0` edge `0.0129` maxDD `-0.8144`
- `market_context_high->equity_4h` score `0.6281` n `46` status `ready` deltaP `5.6999` edge `0.045` maxDD `-0.4529`
- `news_risk_high->metal_24h` score `0.5423` n `100` status `ready` deltaP `19.2222` edge `0.0258` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.4262` n `100` status `ready` deltaP `18.7778` edge `0.0884` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
