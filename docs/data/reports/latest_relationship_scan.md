# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T18:07:27.820756+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11744`

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

- `news_risk_high->unknown_24h` score `4431.5052` n `85` status `ready` deltaP `1.2153` edge `369.284` maxDD `0.0`
- `market_context_high->unknown_1h` score `68.7862` n `47` status `ready` deltaP `8.3196` edge `5.6838` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.3227` n `47` status `ready` deltaP `20.7003` edge `3.7615` maxDD `-2.4756`
- `market_context_high->equity_24h` score `25.4895` n `47` status `ready` deltaP `32.1587` edge `1.9453` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `25.325` n `47` status `ready` deltaP `15.0598` edge `2.048` maxDD `-2.7051`
- `market_context_high->index_24h` score `6.7615` n `47` status `ready` deltaP `25.9087` edge `0.4037` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2473` n `47` status `ready` deltaP `27.2459` edge `0.1128` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7589` n `47` status `ready` deltaP `31.8922` edge `0.0327` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7375` n `47` status `ready` deltaP `17.4494` edge `0.1536` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0562` n `85` status `ready` deltaP `24.0564` edge `0.068` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4146` n `85` status `ready` deltaP `30.4249` edge `0.1433` maxDD `-6.8481`
- `news_risk_high->crypto_alt_24h` score `1.086` n `85` status `ready` deltaP `8.9522` edge `0.426` maxDD `-29.2814`
- `market_context_high->equity_1h` score `1.0482` n `47` status `ready` deltaP `12.0652` edge `0.0472` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.8336` n `47` status `ready` deltaP `9.2306` edge `0.0747` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8313` n `47` status `ready` deltaP `13.1131` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.4456` n `47` status `ready` deltaP `4.8423` edge `0.0953` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4338` n `47` status `ready` deltaP `9.6604` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4225` n `47` status `ready` deltaP `5.9498` edge `0.0773` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0367` n `47` status `ready` deltaP `3.8763` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0471` n `139` status `ready` deltaP `3.2708` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
