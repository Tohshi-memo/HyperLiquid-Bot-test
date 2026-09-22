# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T07:22:31.705354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `48.2374` n `46` status `ready` deltaP `7.3171` edge `3.971` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `33.9681` n `46` status `ready` deltaP `20.6522` edge `2.7086` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `18.7192` n `46` status `ready` deltaP `19.4444` edge `1.4303` maxDD `0.0`
- `market_context_high->equity_24h` score `16.8912` n `46` status `ready` deltaP `14.2286` edge `1.3228` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `6.251` n `101` status `ready` deltaP `-4.703` edge `1.2381` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6136` n `46` status `ready` deltaP `20.1314` edge `0.3423` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.893` n `101` status `ready` deltaP `35.6968` edge `0.2635` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5815` n `101` status `ready` deltaP `12.669` edge `0.2516` maxDD `-7.675`
- `news_risk_high->crypto_alt_24h` score `2.2382` n `101` status `ready` deltaP `-4.318` edge `0.7034` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.1671` n `101` status `ready` deltaP `13.2374` edge `0.1389` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1088` n `101` status `ready` deltaP `16.0227` edge `0.1947` maxDD `-8.0625`
- `market_context_high->index_4h` score `2.0405` n `46` status `ready` deltaP `23.9263` edge `0.0239` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5029` n `101` status `ready` deltaP `14.8841` edge `0.0783` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.291` n `46` status `ready` deltaP `8.9011` edge `0.0789` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0259` n `46` status `ready` deltaP `8.3642` edge `0.0892` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9336` n `46` status `ready` deltaP `7.3614` edge `0.053` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8983` n `101` status `ready` deltaP `15.6529` edge `0.0341` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6567` n `46` status `ready` deltaP `10.3554` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5274` n `101` status `ready` deltaP `13.6998` edge `0.0128` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4151` n `46` status `ready` deltaP `0.3125` edge `0.0848` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
