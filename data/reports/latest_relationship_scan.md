# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T00:22:23.934720+00:00`
- Price records: `501`
- Market context records: `595`
- Flow alert records: `1682`
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

- `market_context_high->crypto_alt_24h` score `4.5475` n `146` status `ready` deltaP `6.9694` edge `0.3373` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.458` n `146` status `ready` deltaP `10.2993` edge `0.2529` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0705` n `146` status `ready` deltaP `11.4417` edge `0.0199` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3106` n `146` status `ready` deltaP `2.0826` edge `0.0041` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6364` n `146` status `ready` deltaP `1.2921` edge `0.0358` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6504` n `146` status `ready` deltaP `0.7155` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1565` n `146` status `ready` deltaP `-4.206` edge `-0.008` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.251` n `146` status `ready` deltaP `5.0275` edge `-0.0063` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2521` n `146` status `ready` deltaP `-1.9214` edge `-0.0105` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8437` n `146` status `ready` deltaP `4.6594` edge `-0.0124` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.122` n `146` status `ready` deltaP `3.0518` edge `0.0598` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2143` n `146` status `ready` deltaP `0.4115` edge `-0.035` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4102` n `146` status `ready` deltaP `-6.6358` edge `0.0429` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.7951` n `146` status `ready` deltaP `12.5364` edge `0.0541` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2928` n `146` status `ready` deltaP `-3.5386` edge `-0.0356` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2955` n `146` status `ready` deltaP `-4.6044` edge `-0.048` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8086` n `146` status `ready` deltaP `-7.3334` edge `0.0816` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.362` n `146` status `ready` deltaP `-3.6519` edge `-0.0177` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.4327` n `146` status `ready` deltaP `-10.443` edge `-0.0393` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.071` n `146` status `ready` deltaP `0.6058` edge `-0.2388` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
