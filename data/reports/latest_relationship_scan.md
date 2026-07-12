# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T21:52:29.657131+00:00`
- Price records: `672`
- Market context records: `6543`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4015` n `144` status `ready` deltaP `11.8934` edge `0.7842` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.6922` n `34` status `ready` deltaP `38.9975` edge `0.0523` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2578` n `34` status `ready` deltaP `27.8707` edge `0.0204` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.006` n `197` status `ready` deltaP `-6.1696` edge `0.2984` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3357` n `144` status `ready` deltaP `12.784` edge `0.2129` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5409` n `189` status `ready` deltaP `12.7662` edge `0.0276` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.4573` n `34` status `ready` deltaP `4.2357` edge `0.0841` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.308` n `189` status `ready` deltaP `9.5464` edge `0.1174` maxDD `-6.7632`
- `market_context_high->equity_4h` score `-0.2545` n `189` status `ready` deltaP `11.3039` edge `0.0619` maxDD `-8.2573`
- `news_risk_high->crypto_alt_1h` score `-0.275` n `34` status `ready` deltaP `-2.7915` edge `0.0343` maxDD `-2.0756`
- `market_context_high->crypto_major_4h` score `-0.4136` n `189` status `ready` deltaP `12.0484` edge `0.0957` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.4332` n `197` status `ready` deltaP `-0.481` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4766` n `197` status `ready` deltaP `1.3207` edge `-0.0016` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5257` n `197` status `ready` deltaP `6.4949` edge `0.0206` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5437` n `197` status `ready` deltaP `6.2213` edge `0.0154` maxDD `-6.7936`
- `market_context_high->equity_1h` score `-0.6766` n `197` status `ready` deltaP `3.0259` edge `0.0041` maxDD `-4.2147`
- `market_context_high->index_1h` score `-0.752` n `197` status `ready` deltaP `0.7029` edge `0.0046` maxDD `-0.7564`
- `news_risk_high->metal_1h` score `-0.9364` n `34` status `ready` deltaP `-5.2307` edge `-0.0228` maxDD `-1.6568`
- `market_context_high->metal_4h` score `-0.9425` n `189` status `ready` deltaP `1.0082` edge `0.0391` maxDD `-2.6662`
- `market_context_high->unknown_4h` score `-1.1055` n `189` status `ready` deltaP `-19.9582` edge `0.2815` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
