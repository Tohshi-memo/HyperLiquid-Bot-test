# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T12:37:10.575086+00:00`
- Price records: `646`
- Market context records: `755`
- Flow alert records: `2131`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.2548` n `146` status `ready` deltaP `31.599` edge `0.9273` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7005` n `146` status `ready` deltaP `7.4969` edge `0.5132` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.5141` n `146` status `ready` deltaP `3.0533` edge `0.222` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.0571` n `146` status `ready` deltaP `1.533` edge `0.2455` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.2624` n `172` status `ready` deltaP `3.235` edge `0.0026` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.414` n `160` status `ready` deltaP `6.4716` edge `0.0095` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6469` n `172` status `ready` deltaP `1.0115` edge `0.0368` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7046` n `172` status `ready` deltaP `-1.3359` edge `-0.0004` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.8915` n `172` status `ready` deltaP `0.9696` edge `0.0046` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0003` n `172` status `ready` deltaP `6.6543` edge `-0.0003` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3665` n `172` status `ready` deltaP `4.9192` edge `-0.0152` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5177` n `172` status `ready` deltaP `-4.0806` edge `-0.0221` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5904` n `160` status `ready` deltaP `17.4405` edge `0.1218` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7162` n `160` status `ready` deltaP `2.0327` edge `-0.0043` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0314` n `172` status `ready` deltaP `-4.2165` edge `-0.0364` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.1578` n `160` status `ready` deltaP `2.6786` edge `0.0593` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-2.4247` n `160` status `ready` deltaP `-5.5751` edge `0.0764` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-2.5431` n `160` status `ready` deltaP `-0.8427` edge `0.0089` maxDD `-10.5498`
- `market_context_high->unknown_4h` score `-3.6768` n `160` status `ready` deltaP `5.3274` edge `-0.1541` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-5.4539` n `146` status `ready` deltaP `-7.0411` edge `-0.1017` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
