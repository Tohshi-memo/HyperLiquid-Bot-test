# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T17:52:33.613106+00:00`
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

- `market_context_high->unknown_4h` score `46.5582` n `46` status `ready` deltaP `7.0122` edge `3.8331` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.7824` n `46` status `ready` deltaP `13.3605` edge `2.4084` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.274` n `46` status `ready` deltaP `12.3189` edge `1.2841` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.7282` n `46` status `ready` deltaP `12.8472` edge `1.1417` maxDD `0.0`
- `market_context_high->index_24h` score `5.574` n `46` status `ready` deltaP `20.1314` edge `0.339` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.4113` n `99` status `ready` deltaP `-10.5745` edge `1.0406` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2751` n `99` status `ready` deltaP `38.0051` edge `0.2844` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `2.3997` n `99` status `ready` deltaP `11.2004` edge `0.2251` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `1.9864` n `99` status `ready` deltaP `14.2492` edge `0.1588` maxDD `-5.0609`
- `news_risk_high->crypto_alt_1h` score `1.8732` n `99` status `ready` deltaP `12.0986` edge `0.122` maxDD `-2.058`
- `market_context_high->index_4h` score `1.8692` n `46` status `ready` deltaP `22.2494` edge `0.0208` maxDD `-0.0692`
- `news_risk_high->fx_4h` score `1.2486` n `99` status `ready` deltaP `19.3721` edge `0.0385` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.1965` n `46` status `ready` deltaP `23.3092` edge `-0.0323` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `1.1119` n `99` status `ready` deltaP `13.4459` edge `0.0553` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.7717` n `46` status `ready` deltaP `6.9123` edge `0.0425` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6447` n `46` status `ready` deltaP `10.3554` edge `0.01` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.59` n `99` status `ready` deltaP `14.6465` edge `0.0117` maxDD `-0.8144`
- `market_context_high->equity_4h` score `0.5471` n `46` status `ready` deltaP `5.2426` edge `0.0413` maxDD `-0.4529`
- `news_risk_high->metal_24h` score `0.519` n `99` status `ready` deltaP `18.9394` edge `0.0247` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.4526` n `99` status `ready` deltaP `18.9552` edge `0.0906` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
