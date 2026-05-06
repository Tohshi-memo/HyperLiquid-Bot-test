# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T21:22:16.847608+00:00`
- Price records: `489`
- Market context records: `582`
- Flow alert records: `1644`
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

- `market_context_high->crypto_alt_24h` score `4.7282` n `146` status `ready` deltaP `7.2031` edge `0.3508` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0751` n `146` status `ready` deltaP `9.5925` edge `0.2257` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0676` n `146` status `ready` deltaP `11.3109` edge `0.0204` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2812` n `146` status `ready` deltaP `2.5873` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6071` n `146` status `ready` deltaP `1.5835` edge `0.0363` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6792` n `146` status `ready` deltaP `0.252` edge `-0.0034` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1695` n `146` status `ready` deltaP `-4.2931` edge `-0.0085` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2615` n `146` status `ready` deltaP `5.0022` edge `-0.007` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2792` n `146` status `ready` deltaP `-2.0349` edge `-0.012` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.908` n `146` status `ready` deltaP `4.1251` edge `-0.0142` maxDD `-11.4508`
- `market_context_high->index_24h` score `-2.0801` n `146` status `ready` deltaP `-5.9742` edge `0.066` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.1275` n `146` status `ready` deltaP `3.2074` edge `0.0583` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2525` n `146` status `ready` deltaP `0.2497` edge `-0.0371` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9453` n `146` status `ready` deltaP `11.6641` edge `0.0474` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2806` n `146` status `ready` deltaP `-4.3737` edge `-0.0483` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3711` n `146` status `ready` deltaP `-3.5882` edge `-0.0418` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.581` n `146` status `ready` deltaP `-5.8387` edge `0.0906` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.0701` n `146` status `ready` deltaP `-10.0045` edge `-0.012` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.524` n `146` status `ready` deltaP `-4.6519` edge `-0.0318` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0586` n `146` status `ready` deltaP `1.3307` edge `-0.2426` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
