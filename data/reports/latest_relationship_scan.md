# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T19:07:22.544591+00:00`
- Price records: `480`
- Market context records: `572`
- Flow alert records: `1615`
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

- `market_context_high->crypto_alt_24h` score `4.8654` n `146` status `ready` deltaP `7.388` edge `0.361` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.8716` n `146` status `ready` deltaP `9.7496` edge `0.2077` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0167` n `146` status `ready` deltaP `10.3931` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2799` n `146` status `ready` deltaP `2.612` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5002` n `146` status `ready` deltaP `2.3944` edge `0.0398` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6701` n `146` status `ready` deltaP `0.3657` edge `-0.003` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1269` n `146` status `ready` deltaP `-3.6261` edge `-0.0094` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.264` n `146` status `ready` deltaP `-1.9648` edge `-0.0112` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3081` n `146` status `ready` deltaP `4.5097` edge `-0.0076` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7238` n `146` status `ready` deltaP `-5.4506` edge `0.0922` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9163` n `146` status `ready` deltaP `4.1268` edge `-0.0149` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.135` n `146` status `ready` deltaP `0.9381` edge `-0.0319` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2652` n `146` status `ready` deltaP `2.5212` edge `0.0514` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0959` n `146` status `ready` deltaP `10.7109` edge `0.0412` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2069` n `146` status `ready` deltaP `-2.975` edge `-0.0322` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2722` n `146` status `ready` deltaP `-4.4032` edge `-0.0474` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5112` n `146` status `ready` deltaP `-5.536` edge `0.0944` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.5299` n `146` status `ready` deltaP `-9.6575` edge `0.0307` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6408` n `146` status `ready` deltaP `-5.4434` edge `-0.0415` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.2701` n `146` status `ready` deltaP `0.3365` edge `-0.2536` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
