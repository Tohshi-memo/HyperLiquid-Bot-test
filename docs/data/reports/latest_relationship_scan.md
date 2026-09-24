# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T09:37:24.984322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `66.0174` n `47` status `ready` deltaP `10.5651` edge `5.4381` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.4345` n `46` status `ready` deltaP `28.8119` edge `3.2764` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `26.8148` n `46` status `ready` deltaP `23.7847` edge `2.076` maxDD `0.0`
- `market_context_high->equity_24h` score `24.0679` n `46` status `ready` deltaP `26.2078` edge `1.841` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.9439` n `46` status `ready` deltaP `35.2355` edge `0.4358` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `7.6933` n `103` status `ready` deltaP `1.1209` edge `1.5379` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `4.5527` n `103` status `ready` deltaP `-1.458` edge `1.0904` maxDD `-49.7699`
- `news_risk_high->crypto_alt_4h` score `3.5021` n `108` status `ready` deltaP `10.7159` edge `0.3202` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `3.3822` n `108` status `ready` deltaP `15.6052` edge `0.2623` maxDD `-4.7589`
- `market_context_high->metal_24h` score `3.2107` n `46` status `ready` deltaP `29.212` edge `0.0962` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.9097` n `47` status `ready` deltaP `33.4166` edge `0.0351` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.4562` n `114` status `ready` deltaP `13.2472` edge `0.1654` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.3267` n `47` status `ready` deltaP `16.2298` edge `0.1275` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0733` n `114` status `ready` deltaP `15.343` edge `0.114` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6722` n `108` status `ready` deltaP `24.2773` edge `0.0411` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.6006` n `103` status `ready` deltaP `19.0601` edge `0.1242` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.2856` n `103` status `ready` deltaP `30.1847` edge `0.1267` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9583` n `47` status `ready` deltaP `14.6101` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9175` n `47` status `ready` deltaP `11.0173` edge `0.0433` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7538` n `103` status `ready` deltaP `21.0862` edge `0.1009` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
