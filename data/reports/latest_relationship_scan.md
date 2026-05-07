# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T08:37:22.419326+00:00`
- Price records: `534`
- Market context records: `630`
- Flow alert records: `1783`
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

- `market_context_high->crypto_major_24h` score `5.5857` n `146` status `ready` deltaP `16.21` edge `0.3908` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2669` n `146` status `ready` deltaP `7.306` edge `0.395` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0637` n `146` status `ready` deltaP `9.3865` edge `0.0164` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3138` n `146` status `ready` deltaP `2.0964` edge `0.0036` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5128` n `146` status `ready` deltaP `1.9376` edge `0.0418` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7385` n `146` status `ready` deltaP `-0.8282` edge `-0.0038` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1242` n `146` status `ready` deltaP `-3.8924` edge `-0.0074` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2643` n `146` status `ready` deltaP `5.327` edge `-0.0094` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3443` n `146` status `ready` deltaP `-2.7293` edge `-0.0128` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7972` n `146` status `ready` deltaP `5.0607` edge `-0.0112` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0013` n `146` status `ready` deltaP `4.3502` edge `0.0612` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3911` n `146` status `ready` deltaP `-1.4685` edge `-0.0372` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4819` n `146` status `ready` deltaP `13.6166` edge `0.073` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0195` n `146` status `ready` deltaP `-8.2665` edge `0.003` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.4147` n `146` status `ready` deltaP `-3.9976` edge `-0.0427` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4614` n `146` status `ready` deltaP `-5.3735` edge `-0.0567` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5204` n `146` status `ready` deltaP `-5.8312` edge `0.0956` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2815` n `146` status `ready` deltaP `-2.5693` edge `-0.0146` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.752` n `146` status `ready` deltaP `1.9225` edge `-0.221` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.968` n `146` status `ready` deltaP `-11.5239` edge `-0.0767` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
