# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T23:39:55.275938+00:00`
- Price records: `594`
- Market context records: `697`
- Flow alert records: `1969`
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

- `market_context_high->crypto_major_24h` score `10.3737` n `146` status `ready` deltaP `25.3149` edge `0.7291` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6057` n `146` status `ready` deltaP `8.3512` edge `0.4996` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1899` n `149` status `ready` deltaP `7.5439` edge `0.0125` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2576` n `149` status `ready` deltaP `3.2812` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5206` n `149` status `ready` deltaP `2.065` edge `0.0403` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5851` n `149` status `ready` deltaP `0.8464` edge `0.0047` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1136` n `149` status `ready` deltaP `-1.3607` edge `-0.0027` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1913` n `149` status `ready` deltaP `15.6255` edge `0.1137` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2168` n `149` status `ready` deltaP `-4.3898` edge `-0.0118` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3938` n `149` status `ready` deltaP `4.4431` edge `-0.0143` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.4086` n `146` status `ready` deltaP `-4.1956` edge `0.1101` maxDD `-5.9609`
- `market_context_high->index_4h` score `-1.6214` n `149` status `ready` deltaP `2.7828` edge `-0.0014` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6319` n `149` status `ready` deltaP `6.0164` edge `-0.0038` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9748` n `149` status `ready` deltaP `4.1859` edge `0.0645` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5901` n `149` status `ready` deltaP `-0.8757` edge `0.0052` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-2.631` n `146` status `ready` deltaP `-6.2364` edge `0.0828` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.2962` n `149` status `ready` deltaP `-4.7628` edge `-0.047` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.816` n `149` status `ready` deltaP `-6.2413` edge `0.0737` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4249` n `149` status `ready` deltaP `2.3815` edge `-0.1968` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9546` n `146` status `ready` deltaP `-10.909` edge `-0.0453` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
