# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T08:57:12.513184+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.8967` n `91` status `ready` deltaP `-6.188` edge `3.5032` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6533` n `91` status `ready` deltaP `35.3439` edge `0.6117` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9175` n `91` status `ready` deltaP `19.4832` edge `1.3282` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.628` n `91` status `ready` deltaP `10.0578` edge `0.7529` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.3069` n `91` status `ready` deltaP `15.2674` edge `0.1988` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2356` n `91` status `ready` deltaP `6.3977` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1509` n `91` status `ready` deltaP `9.0956` edge `0.0476` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1062` n `91` status `ready` deltaP `8.674` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2904` n `91` status `ready` deltaP `9.4235` edge `0.0909` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3217` n `91` status `ready` deltaP `3.4481` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3566` n `91` status `ready` deltaP `6.7172` edge `0.058` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.389` n `91` status `ready` deltaP `0.4031` edge `0.0025` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7702` n `91` status `ready` deltaP `-2.5562` edge `-0.0117` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.922` n `91` status `ready` deltaP `-4.4383` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9324` n `91` status `ready` deltaP `-4.8563` edge `0.0136` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-0.9605` n `91` status `ready` deltaP `-4.0682` edge `-0.0114` maxDD `-0.9885`
- `market_context_high->crypto_alt_1h` score `-1.1424` n `91` status `ready` deltaP `-1.9444` edge `0.0316` maxDD `-4.7735`
- `market_context_high->crypto_alt_4h` score `-1.1905` n `91` status `ready` deltaP `-8.4763` edge `0.0972` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.2325` n `91` status `ready` deltaP `-10.3376` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2874` n `91` status `ready` deltaP `-10.8651` edge `0.0006` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
