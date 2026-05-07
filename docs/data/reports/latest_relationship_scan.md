# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T04:07:19.046719+00:00`
- Price records: `516`
- Market context records: `611`
- Flow alert records: `1728`
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

- `market_context_high->crypto_alt_24h` score `5.0915` n `146` status `ready` deltaP `7.6484` edge `0.3781` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.4734` n `146` status `ready` deltaP `12.9713` edge `0.3197` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0374` n `146` status `ready` deltaP `9.8321` edge `0.0168` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3461` n `146` status `ready` deltaP `1.5343` edge `0.0032` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6244` n `146` status `ready` deltaP `1.2917` edge `0.0368` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6807` n `146` status `ready` deltaP `0.1321` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0083` n `146` status `ready` deltaP `-3.0287` edge `-0.0035` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.0196` n `146` status `ready` deltaP `6.3758` edge `0.004` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2297` n `146` status `ready` deltaP `-1.8364` edge `-0.0092` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5331` n `146` status `ready` deltaP `5.1178` edge `0.0951` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6069` n `146` status `ready` deltaP `6.2687` edge `-0.0034` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.2592` n `146` status `ready` deltaP `-0.2541` edge `-0.0343` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.2986` n `146` status `ready` deltaP `14.3178` edge `0.0836` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.6641` n `146` status `ready` deltaP `-7.4091` edge `0.0269` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1545` n `146` status `ready` deltaP `-2.875` edge `-0.0285` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2945` n `146` status `ready` deltaP `-4.4869` edge `-0.0487` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7324` n `146` status `ready` deltaP `-6.6808` edge `0.0836` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2583` n `146` status `ready` deltaP `-2.4829` edge `-0.0122` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6766` n `146` status `ready` deltaP `-10.9556` edge `-0.0562` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.7463` n `146` status `ready` deltaP `2.0986` edge `-0.2217` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
