# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T01:28:11.112604+00:00`
- Price records: `601`
- Market context records: `705`
- Flow alert records: `1992`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.7906` n `146` status `ready` deltaP `26.2362` edge `0.7577` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5417` n `146` status `ready` deltaP `8.226` edge `0.4951` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2177` n `149` status `ready` deltaP `7.1157` edge `0.0118` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2823` n `149` status `ready` deltaP `2.912` edge `0.0022` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4924` n `149` status `ready` deltaP `2.2817` edge `0.0412` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6232` n `149` status `ready` deltaP `0.369` edge `0.003` maxDD `-2.8282`
- `market_context_high->index_24h` score `-1.1159` n `146` status `ready` deltaP `-3.1321` edge `0.1274` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1497` n `149` status `ready` deltaP `16.1108` edge `0.1158` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1786` n `149` status `ready` deltaP `-4.1067` edge `-0.0105` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1924` n `149` status `ready` deltaP `-1.8199` edge `-0.0062` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.39` n `149` status `ready` deltaP `4.4607` edge `-0.0141` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6292` n `149` status `ready` deltaP `5.9605` edge `-0.0032` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.677` n `149` status `ready` deltaP `2.3126` edge `-0.0029` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9916` n `149` status `ready` deltaP `3.9614` edge `0.0646` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.2398` n `146` status `ready` deltaP `-5.0966` edge `0.1078` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5721` n `149` status `ready` deltaP `-0.7855` edge `0.0061` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3608` n `149` status `ready` deltaP `-5.106` edge `-0.0501` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8458` n `149` status `ready` deltaP `-6.5982` edge `0.0736` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2846` n `149` status `ready` deltaP `3.0999` edge `-0.1899` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0266` n `146` status `ready` deltaP `-11.7519` edge `-0.0489` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
