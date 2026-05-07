# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T15:52:19.224814+00:00`
- Price records: `563`
- Market context records: `660`
- Flow alert records: `1873`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `848`

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

- `market_context_high->crypto_major_24h` score `8.0635` n `146` status `ready` deltaP `20.9029` edge `0.566` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.2525` n `146` status `ready` deltaP `8.7369` edge `0.4676` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1502` n `146` status `ready` deltaP `8.1271` edge `0.0137` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.334` n `147` status `ready` deltaP `1.8276` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4123` n `147` status `ready` deltaP `2.3534` edge `0.0474` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.62` n `147` status `ready` deltaP `0.684` edge `0.0013` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1808` n `147` status `ready` deltaP `-4.3299` edge `-0.0092` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1995` n `147` status `ready` deltaP `5.6272` edge `-0.006` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2386` n `147` status `ready` deltaP `-1.7981` edge `-0.0102` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6181` n `147` status `ready` deltaP `5.8742` edge `-0.0017` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8988` n `146` status `ready` deltaP `4.6417` edge `0.0678` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.993` n `146` status `ready` deltaP `1.3484` edge `-0.0228` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.048` n `146` status `ready` deltaP `15.245` edge `0.0983` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.8879` n `146` status `ready` deltaP `-9.2917` edge `0.0208` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.1054` n `146` status `ready` deltaP `-4.2433` edge `0.1196` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.1627` n `146` status `ready` deltaP `-2.8873` edge `-0.0291` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4516` n `147` status `ready` deltaP `-5.4008` edge `-0.0557` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.6183` n `146` status `ready` deltaP `-6.87` edge `-0.0291` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7096` n `146` status `ready` deltaP `-11.6985` edge `-0.054` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.7818` n `146` status `ready` deltaP `1.1757` edge `-0.2185` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
