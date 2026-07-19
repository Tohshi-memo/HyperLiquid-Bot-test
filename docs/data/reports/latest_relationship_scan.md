# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T22:37:30.384900+00:00`
- Price records: `672`
- Market context records: `7297`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.0876` n `127` status `ready` deltaP `5.3415` edge `0.0021` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.5122` n `127` status `ready` deltaP `0.5434` edge `0.0346` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.5387` n `127` status `ready` deltaP `-0.097` edge `-0.0112` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.612` n `127` status `ready` deltaP `4.4085` edge `0.0332` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.6898` n `124` status `ready` deltaP `2.8805` edge `-0.0108` maxDD `-2.4139`
- `market_context_high->fx_4h` score `-0.8879` n `124` status `ready` deltaP `4.851` edge `0.0138` maxDD `-1.4649`
- `market_context_high->fx_24h` score `-0.9166` n `120` status `ready` deltaP `0.5363` edge `0.0017` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.2462` n `127` status `ready` deltaP `-0.0613` edge `-0.097` maxDD `-1.3217`
- `market_context_high->index_1h` score `-1.3059` n `127` status `ready` deltaP `-5.3746` edge `-0.0088` maxDD `-2.1355`
- `market_context_high->unknown_4h` score `-1.316` n `124` status `ready` deltaP `5.9402` edge `0.0866` maxDD `-6.2031`
- `market_context_high->metal_1h` score `-1.3923` n `127` status `ready` deltaP `-9.7376` edge `-0.0032` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.4464` n `124` status `ready` deltaP `-9.3578` edge `-0.0057` maxDD `-4.6441`
- `market_context_high->crypto_major_4h` score `-3.1161` n `124` status `ready` deltaP `1.2195` edge `-0.0182` maxDD `-23.4879`
- `market_context_high->commodity_24h` score `-3.1529` n `120` status `ready` deltaP `-6.3406` edge `-0.1407` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.3607` n `124` status `ready` deltaP `0.7572` edge `-0.0108` maxDD `-15.2776`
- `market_context_high->equity_1h` score `-4.4114` n `127` status `ready` deltaP `-9.3116` edge `-0.0679` maxDD `-14.3442`
- `market_context_high->index_4h` score `-5.034` n `124` status `ready` deltaP `-14.7824` edge `-0.0591` maxDD `-10.6145`
- `market_context_high->unknown_24h` score `-5.2868` n `121` status `ready` deltaP `-9.2401` edge `-0.046` maxDD `-14.6374`
- `market_context_high->metal_24h` score `-11.109` n `121` status `ready` deltaP `-28.9156` edge `-0.1283` maxDD `-21.708`
- `market_context_high->index_24h` score `-13.2101` n `120` status `ready` deltaP `-30.0217` edge `-0.1671` maxDD `-34.3547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
