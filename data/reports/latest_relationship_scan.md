# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T12:37:17.816558+00:00`
- Price records: `550`
- Market context records: `646`
- Flow alert records: `1832`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.0767` n `146` status `ready` deltaP `18.8733` edge `0.4973` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0081` n `146` status `ready` deltaP `8.7865` edge `0.4469` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1831` n `146` status `ready` deltaP `7.4645` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3495` n `146` status `ready` deltaP `1.4987` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4275` n `146` status `ready` deltaP `2.3732` edge `0.046` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.684` n `146` status `ready` deltaP `-0.1112` edge `-0.0016` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1571` n `146` status `ready` deltaP `-4.3479` edge `-0.0071` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2517` n `146` status `ready` deltaP `5.4092` edge `-0.0089` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.272` n `146` status `ready` deltaP `-2.1407` edge `-0.0107` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7104` n `146` status `ready` deltaP `5.5597` edge `-0.0073` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0809` n `146` status `ready` deltaP `3.9403` edge `0.0573` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2284` n `146` status `ready` deltaP `-0.2145` edge `-0.032` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3822` n `146` status `ready` deltaP `14.0526` edge `0.0784` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9188` n `146` status `ready` deltaP `-8.7489` edge `0.0146` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.2304` n `146` status `ready` deltaP `-4.6213` edge `0.1117` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.4086` n `146` status `ready` deltaP `-4.1768` edge `-0.041` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4739` n `146` status `ready` deltaP `-5.3189` edge `-0.0581` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.4763` n `146` status `ready` deltaP `-5.0107` edge `-0.0233` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6448` n `146` status `ready` deltaP `-11.3242` edge `-0.0511` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8388` n `146` status `ready` deltaP `0.7773` edge `-0.2206` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
