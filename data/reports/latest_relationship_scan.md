# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T07:52:21.050003+00:00`
- Price records: `672`
- Market context records: `954`
- Flow alert records: `2673`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.7932` n `161` status `ready` deltaP `32.4847` edge `1.0496` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.4855` n `161` status `ready` deltaP `8.8542` edge `0.6481` maxDD `0.0`
- `market_context_high->equity_24h` score `1.0671` n `161` status `ready` deltaP `2.6398` edge `0.3318` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.3079` n `161` status `ready` deltaP `1.2703` edge `0.2167` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2637` n `204` status `ready` deltaP `3.0615` edge `0.0384` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3919` n `204` status `ready` deltaP `1.0098` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.5824` n `204` status `ready` deltaP `1.8199` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.6971` n `204` status `ready` deltaP `3.2347` edge `0.0057` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-1.0333` n `192` status `ready` deltaP `1.7149` edge `0.0021` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.0818` n `204` status `ready` deltaP `5.7473` edge `-0.0047` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.2039` n `192` status `ready` deltaP `2.6677` edge `0.0971` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-1.4164` n `192` status `ready` deltaP `-0.7749` edge `0.082` maxDD `-13.0076`
- `market_context_high->unknown_1h` score `-1.4306` n `204` status `ready` deltaP `-3.6222` edge `-0.0179` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.4374` n `192` status `ready` deltaP `0.6732` edge `0.028` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8545` n `204` status `ready` deltaP `-1.8345` edge `-0.0296` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.9244` n `204` status `ready` deltaP `1.2299` edge `-0.0246` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4461` n `192` status `ready` deltaP `8.9939` edge `0.1068` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.3389` n `192` status `ready` deltaP `6.6565` edge `-0.1348` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.3744` n `192` status `ready` deltaP `-2.2485` edge `0.0116` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.4137` n `161` status `ready` deltaP `5.2828` edge `-0.0505` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
