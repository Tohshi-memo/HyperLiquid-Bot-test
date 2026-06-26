# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T09:07:27.793475+00:00`
- Price records: `672`
- Market context records: `4812`
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

- `market_context_high->unknown_1h` score `11.4723` n `118` status `ready` deltaP `11.7122` edge `0.9197` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8161` n `118` status `ready` deltaP `18.3573` edge `0.65` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.1619` n `111` status `ready` deltaP `12.2842` edge `0.1906` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.1884` n `118` status `ready` deltaP `9.3892` edge `0.1069` maxDD `-6.9604`
- `market_context_high->commodity_1h` score `0.1125` n `118` status `ready` deltaP `5.8865` edge `0.0289` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.095` n `118` status `ready` deltaP `12.1641` edge `0.0483` maxDD `-4.377`
- `market_context_high->fx_4h` score `-0.3088` n `118` status `ready` deltaP `5.1519` edge `0.0037` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.3507` n `118` status `ready` deltaP `7.3713` edge `0.0112` maxDD `-5.4242`
- `market_context_high->equity_1h` score `-0.6894` n `118` status `ready` deltaP `2.144` edge `0.005` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0102` n `118` status `ready` deltaP `-2.3901` edge `-0.0033` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3872` n `118` status `ready` deltaP `-1.1976` edge `-0.0072` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1173` n `111` status `ready` deltaP `19.909` edge `0.1067` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3078` n `118` status `ready` deltaP `-1.2915` edge `-0.0697` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.8053` n `111` status `ready` deltaP `-12.5517` edge `-0.0191` maxDD `-3.1464`
- `market_context_high->crypto_major_1h` score `-2.9927` n `118` status `ready` deltaP `0.3527` edge `-0.077` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.1134` n `118` status `ready` deltaP `1.3473` edge `-0.048` maxDD `-14.9676`
- `market_context_high->index_24h` score `-4.3736` n `111` status `ready` deltaP `-7.0899` edge `-0.1226` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.5476` n `118` status `ready` deltaP `6.4567` edge `-0.0182` maxDD `-43.2966`
- `market_context_high->crypto_major_4h` score `-8.3312` n `118` status `ready` deltaP `3.5914` edge `-0.1765` maxDD `-67.9107`
- `market_context_high->metal_4h` score `-8.5751` n `118` status `ready` deltaP `4.7566` edge `-0.307` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
