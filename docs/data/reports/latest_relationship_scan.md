# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T05:37:27.432957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9945`

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

- `market_context_high->unknown_1h` score `72.057` n `47` status `ready` deltaP `10.8645` edge `5.9394` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `38.7247` n `46` status `ready` deltaP `26.0341` edge `3.0691` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `23.511` n `46` status `ready` deltaP `21.0069` edge `1.8192` maxDD `0.0`
- `market_context_high->equity_24h` score `22.3577` n `46` status `ready` deltaP `23.43` edge `1.717` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.4637` n `46` status `ready` deltaP `32.4578` edge `0.4143` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9835` n `103` status `ready` deltaP `-1.6569` edge `1.3306` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.9431` n `103` status `ready` deltaP `14.6889` edge `0.4138` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.8339` n `103` status `ready` deltaP `18.8048` edge `0.3352` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.6514` n `104` status `ready` deltaP `14.308` edge `0.1746` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.6438` n `47` status `ready` deltaP `30.9776` edge `0.0292` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.6045` n `46` status `ready` deltaP `26.4342` edge `0.0642` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.1516` n `103` status `ready` deltaP `21.8379` edge `0.1516` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.1294` n `104` status `ready` deltaP `16.4038` edge `0.1116` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.7956` n `47` status `ready` deltaP `13.7908` edge `0.0995` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.6014` n `103` status `ready` deltaP `23.3765` edge `0.0412` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `1.2489` n `103` status `ready` deltaP `-4.2358` edge `0.8336` maxDD `-49.7699`
- `news_risk_high->fx_24h` score `1.2281` n `103` status `ready` deltaP `29.6639` edge `0.1228` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8301` n `47` status `ready` deltaP `13.2628` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6957` n `104` status `ready` deltaP `15.8567` edge `0.0116` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6502` n `47` status `ready` deltaP `9.3706` edge `0.032` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
