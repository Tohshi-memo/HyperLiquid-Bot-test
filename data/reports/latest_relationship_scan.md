# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T19:22:20.811671+00:00`
- Price records: `481`
- Market context records: `573`
- Flow alert records: `1618`
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

- `market_context_high->crypto_alt_24h` score `4.8337` n `146` status `ready` deltaP `7.367` edge `0.3585` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.8799` n `146` status `ready` deltaP `9.7029` edge `0.2087` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0221` n `146` status `ready` deltaP `10.4969` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.274` n `146` status `ready` deltaP `2.7267` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5106` n `146` status `ready` deltaP `2.2792` edge `0.0397` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6768` n `146` status `ready` deltaP `0.2824` edge `-0.0033` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1336` n `146` status `ready` deltaP `-3.7247` edge `-0.0093` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2762` n `146` status `ready` deltaP `-2.0432` edge `-0.0117` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2968` n `146` status `ready` deltaP `4.6352` edge `-0.0075` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7669` n `146` status `ready` deltaP `-5.51` edge `0.089` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9261` n `146` status `ready` deltaP `4.0334` edge `-0.0151` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.1472` n `146` status `ready` deltaP `0.8603` edge `-0.0324` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2449` n `146` status `ready` deltaP `2.6705` edge `0.0521` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.077` n `146` status `ready` deltaP `10.8425` edge `0.0419` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2244` n `146` status `ready` deltaP `-3.0443` edge `-0.0332` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2842` n `146` status `ready` deltaP `-4.493` edge `-0.0478` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5055` n `146` status `ready` deltaP `-5.4497` edge `0.0943` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.5895` n `146` status `ready` deltaP `-9.6969` edge `0.026` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6275` n `146` status `ready` deltaP `-5.3536` edge `-0.0404` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.2448` n `146` status `ready` deltaP `0.4728` edge `-0.2524` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
