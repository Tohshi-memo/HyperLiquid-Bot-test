# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T13:22:26.905883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `774.9168` n `136` status `ready` deltaP `1.2153` edge `64.5683` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.384` n `40` status `ready` deltaP `10.3743` edge `12.9675` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.4189` n `36` status `ready` deltaP `29.6875` edge `4.6221` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.788` n `36` status `ready` deltaP `35.5903` edge `2.3598` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.101` n `36` status `ready` deltaP `14.4097` edge `2.367` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.5381` n `36` status `ready` deltaP `32.9861` edge `0.5004` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.8312` n `40` status `ready` deltaP `19.4512` edge `0.3272` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.3793` n `36` status `ready` deltaP `39.2362` edge `0.1272` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.9655` n `40` status `ready` deltaP `24.6951` edge `0.1993` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1879` n `40` status `ready` deltaP `34.939` edge `0.0398` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.5059` n `40` status `ready` deltaP `10.0915` edge `0.232` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7766` n `40` status `ready` deltaP `19.4611` edge `0.0586` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.5772` n `40` status `ready` deltaP `11.2126` edge `0.1456` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4143` n `40` status `ready` deltaP `11.4072` edge `0.1276` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0655` n `40` status `ready` deltaP `14.7605` edge `0.0099` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9137` n `40` status `ready` deltaP `15.5389` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.8694` n `136` status `ready` deltaP `16.6463` edge `0.031` maxDD `-2.2287`
- `market_context_high->metal_4h` score `0.3947` n `40` status `ready` deltaP `7.378` edge `0.0216` maxDD `-0.3647`
- `news_risk_high->metal_24h` score `0.3936` n `136` status `ready` deltaP `14.563` edge `0.1212` maxDD `-6.8392`
- `news_risk_high->index_1h` score `-0.1259` n `139` status `ready` deltaP `2.3145` edge `0.0031` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
