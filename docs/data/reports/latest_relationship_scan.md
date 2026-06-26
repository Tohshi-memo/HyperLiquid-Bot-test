# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T09:22:31.974079+00:00`
- Price records: `672`
- Market context records: `4813`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7572`

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

- `market_context_high->unknown_1h` score `11.4819` n `118` status `ready` deltaP `11.7122` edge `0.9205` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8269` n `118` status `ready` deltaP `18.3573` edge `0.6509` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.1264` n `111` status `ready` deltaP `12.1106` edge `0.1888` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.161` n `118` status `ready` deltaP `9.2368` edge `0.1044` maxDD `-6.9604`
- `market_context_high->commodity_1h` score `0.1065` n `118` status `ready` deltaP `5.8865` edge `0.0284` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0911` n `118` status `ready` deltaP `12.1641` edge `0.0478` maxDD `-4.377`
- `market_context_high->fx_4h` score `-0.3001` n `118` status `ready` deltaP `5.3044` edge `0.0038` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.3695` n `118` status `ready` deltaP `7.2188` edge `0.0098` maxDD `-5.4242`
- `market_context_high->equity_1h` score `-0.6918` n `118` status `ready` deltaP `2.144` edge `0.0048` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0102` n `118` status `ready` deltaP `-2.3901` edge `-0.0033` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3884` n `118` status `ready` deltaP `-1.1976` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.106` n `111` status `ready` deltaP `20.0826` edge `0.107` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3062` n `118` status `ready` deltaP `-1.2915` edge `-0.0695` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.8204` n `111` status `ready` deltaP `-12.7253` edge `-0.0192` maxDD `-3.1464`
- `market_context_high->crypto_major_1h` score `-2.974` n `118` status `ready` deltaP `0.5024` edge `-0.0756` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.0942` n `118` status `ready` deltaP `1.497` edge `-0.0474` maxDD `-14.9676`
- `market_context_high->index_24h` score `-4.3736` n `111` status `ready` deltaP `-7.0899` edge `-0.1226` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.5829` n `118` status `ready` deltaP `6.3042` edge `-0.0217` maxDD `-43.2966`
- `market_context_high->crypto_major_4h` score `-8.3641` n `118` status `ready` deltaP `3.439` edge `-0.1797` maxDD `-67.9107`
- `market_context_high->metal_4h` score `-8.5947` n `118` status `ready` deltaP `4.6042` edge `-0.3085` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
