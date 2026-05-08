# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T06:22:11.676328+00:00`
- Price records: `621`
- Market context records: `726`
- Flow alert records: `2052`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `11.8651` n `146` status `ready` deltaP `28.7332` edge `0.8306` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3525` n `146` status `ready` deltaP `7.8865` edge `0.4816` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.3297` n `149` status `ready` deltaP `5.4718` edge `0.0084` maxDD `-1.6381`
- `market_context_high->index_24h` score `-0.3322` n `146` status `ready` deltaP `-0.2511` edge `0.1735` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.4438` n `155` status `ready` deltaP `2.7627` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5033` n `155` status `ready` deltaP `2.2207` edge `0.0407` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9244` n `155` status `ready` deltaP `0.7683` edge `0.0032` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9946` n `149` status `ready` deltaP `17.5772` edge `0.1259` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0536` n `155` status `ready` deltaP `-0.6999` edge `-0.0021` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0816` n `155` status `ready` deltaP `5.5555` edge `-0.0034` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.16` n `146` status `ready` deltaP `-2.0087` edge `0.1772` maxDD `-10.5047`
- `market_context_high->crypto_alt_1h` score `-1.4691` n `155` status `ready` deltaP `4.0717` edge `-0.0181` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5686` n `155` status `ready` deltaP `-4.605` edge `-0.023` maxDD `-3.4946`
- `market_context_high->index_4h` score `-1.8553` n `149` status `ready` deltaP `1.0296` edge `-0.0092` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0172` n `149` status `ready` deltaP `3.207` edge `0.0675` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8153` n `149` status `ready` deltaP `-1.9654` edge `-0.0063` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2675` n `155` status `ready` deltaP `-4.6301` edge `-0.0455` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5895` n `149` status `ready` deltaP `-5.1949` edge `0.0856` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9779` n `149` status `ready` deltaP `4.3996` edge `-0.173` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2287` n `146` status `ready` deltaP `-14.0352` edge `-0.0596` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
