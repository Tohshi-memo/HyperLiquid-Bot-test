# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T06:37:20.850422+00:00`
- Price records: `526`
- Market context records: `622`
- Flow alert records: `1758`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.2139` n `146` status `ready` deltaP `7.4546` edge `0.3896` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `5.1348` n `146` status `ready` deltaP `14.8041` edge `0.3626` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.099` n `146` status `ready` deltaP `8.8121` edge `0.0157` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.33` n `146` status `ready` deltaP `1.83` edge `0.0033` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5951` n `146` status `ready` deltaP `1.6132` edge `0.0371` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7123` n `146` status `ready` deltaP `-0.4311` edge `-0.0031` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0546` n `146` status `ready` deltaP `-3.3669` edge `-0.0051` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.167` n `146` status `ready` deltaP `5.7629` edge `-0.0042` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3148` n `146` status `ready` deltaP `-2.5546` edge `-0.0115` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.6714` n `146` status `ready` deltaP `4.859` edge `0.0853` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.7051` n `146` status `ready` deltaP `5.566` edge `-0.0069` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2675` n `146` status `ready` deltaP `14.2707` edge `0.0865` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.3248` n `146` status `ready` deltaP `-0.9394` edge `-0.0352` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.8217` n `146` status `ready` deltaP `-7.8944` edge `0.017` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2832` n `146` status `ready` deltaP `-3.5086` edge `-0.035` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3345` n `146` status `ready` deltaP `-4.7316` edge `-0.0504` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7055` n `146` status `ready` deltaP `-6.4649` edge `0.0844` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.27` n `146` status `ready` deltaP `-2.4536` edge `-0.0139` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6393` n `146` status `ready` deltaP `2.5221` edge `-0.2156` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7971` n `146` status `ready` deltaP `-11.2772` edge `-0.0641` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
