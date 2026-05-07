# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T03:37:16.686308+00:00`
- Price records: `514`
- Market context records: `609`
- Flow alert records: `1721`
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

- `market_context_high->crypto_alt_24h` score `4.9532` n `146` status `ready` deltaP `7.2098` edge `0.3695` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.3004` n `146` status `ready` deltaP `12.5942` edge `0.3078` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0226` n `146` status `ready` deltaP `10.0411` edge `0.0173` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3354` n `146` status `ready` deltaP `1.711` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.621` n `146` status `ready` deltaP `1.3049` edge `0.037` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6734` n `146` status `ready` deltaP `0.287` edge `-0.0029` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0331` n `146` status `ready` deltaP `-3.2339` edge `-0.0042` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.0498` n `146` status `ready` deltaP `6.1483` edge `0.003` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2143` n `146` status `ready` deltaP `-1.6893` edge `-0.0089` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.6206` n `146` status `ready` deltaP `4.8495` edge `0.0896` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6333` n `146` status `ready` deltaP `6.0596` edge `-0.0042` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.2491` n `146` status `ready` deltaP `-0.1137` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3735` n `146` status `ready` deltaP `14.0865` edge `0.0789` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.6297` n `146` status `ready` deltaP `-7.3093` edge `0.0291` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1675` n `146` status `ready` deltaP `-2.9477` edge `-0.0291` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3196` n `146` status `ready` deltaP `-4.7113` edge `-0.0493` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7517` n `146` status `ready` deltaP `-6.8465` edge `0.0831` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2701` n `146` status `ready` deltaP `-2.6339` edge `-0.0127` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6581` n `146` status `ready` deltaP `-10.8894` edge `-0.0551` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8033` n `146` status `ready` deltaP `1.8512` edge `-0.2248` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
