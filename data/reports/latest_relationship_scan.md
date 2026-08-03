# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T10:37:28.897788+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->crypto_alt_24h` score `12.2847` n `40` status `ready` deltaP `51.4583` edge `0.7204` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8647` n `40` status `ready` deltaP `51.1458` edge `0.5772` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.7752` n `31` status `ready` deltaP `-6.668` edge `0.2608` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9311` n `31` status `ready` deltaP `19.688` edge `0.0093` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9293` n `31` status `ready` deltaP `12.192` edge `0.0614` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3292` n `47` status `ready` deltaP `7.2652` edge `0.0312` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3251` n `31` status `ready` deltaP `13.7047` edge `-0.0142` maxDD `-1.6728`
- `news_risk_high->index_4h` score `0.3125` n `31` status `ready` deltaP `0.2409` edge `0.0625` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.2884` n `47` status `ready` deltaP `4.5764` edge `0.0911` maxDD `-2.7703`
- `news_risk_high->fx_4h` score `0.1533` n `31` status `ready` deltaP `5.0453` edge `0.0363` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.1156` n `31` status `ready` deltaP `12.1885` edge `-0.0024` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0387` n `31` status `ready` deltaP `3.9405` edge `-0.0015` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0334` n `47` status `ready` deltaP `6.5167` edge `-0.0088` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1279` n `47` status `ready` deltaP `12.046` edge `-0.0053` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.2439` n `47` status `ready` deltaP `2.1439` edge `0.045` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.2443` n `31` status `ready` deltaP `-0.4153` edge `0.0026` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.584` n `31` status `ready` deltaP `-2.2117` edge `-0.002` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7332` n `31` status `ready` deltaP `3.7087` edge `-0.0467` maxDD `-3.762`
- `news_risk_high->equity_1h` score `-0.9401` n `31` status `ready` deltaP `-9.7112` edge `0.0265` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
