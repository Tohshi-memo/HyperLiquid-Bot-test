# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T18:07:21.334076+00:00`
- Price records: `476`
- Market context records: `568`
- Flow alert records: `1603`
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

- `market_context_high->crypto_alt_24h` score `4.8955` n `144` status `ready` deltaP `7.4635` edge `0.363` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9424` n `144` status `ready` deltaP `9.8246` edge `0.2131` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0051` n `146` status `ready` deltaP `9.9736` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3048` n `146` status `ready` deltaP `2.1484` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.547` n `146` status `ready` deltaP `2.005` edge `0.0385` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6456` n `146` status `ready` deltaP `0.7025` edge `-0.0021` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1397` n `146` status `ready` deltaP `-3.651` edge `-0.0103` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.223` n `146` status `ready` deltaP `-1.6479` edge `-0.0099` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3437` n `146` status `ready` deltaP `4.2141` edge `-0.0086` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7717` n `144` status `ready` deltaP `-5.5999` edge `0.0892` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9441` n `146` status `ready` deltaP `3.8687` edge `-0.0155` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0774` n `146` status `ready` deltaP `1.2527` edge `-0.0292` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2403` n `146` status `ready` deltaP `2.7874` edge `0.0517` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.1232` n `146` status `ready` deltaP `-2.6947` edge `-0.0271` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.1733` n `146` status `ready` deltaP `10.1787` edge `0.0383` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2299` n `146` status `ready` deltaP `-4.04` edge `-0.0463` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5355` n `146` status `ready` deltaP `-5.885` edge `0.0947` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.6189` n `144` status `ready` deltaP `-9.8404` edge `0.0245` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5377` n `144` status `ready` deltaP `-5.4078` edge `-0.0407` maxDD `-20.0671`
- `market_context_high->unknown_4h` score `-5.3706` n `146` status `ready` deltaP `-0.2144` edge `-0.2583` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
