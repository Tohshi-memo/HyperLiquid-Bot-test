# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T10:07:33.484148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.4455` n `130` status `ready` deltaP `4.7748` edge `0.1747` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5417` n `130` status `ready` deltaP `1.9254` edge `0.0405` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.7304` n `130` status `ready` deltaP `2.3745` edge `0.0004` maxDD `-1.1679`
- `news_risk_high->fx_1h` score `-0.7545` n `130` status `ready` deltaP `-3.5928` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_4h` score `-0.787` n `130` status `ready` deltaP `5.2182` edge `0.0119` maxDD `-2.8071`
- `news_risk_high->fx_4h` score `-1.1403` n `130` status `ready` deltaP `-6.4024` edge `-0.0102` maxDD `-1.4652`
- `news_risk_high->index_24h` score `-1.2308` n `130` status `ready` deltaP `-7.4421` edge `0.1003` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-1.3218` n `130` status `ready` deltaP `-6.7941` edge `-0.0185` maxDD `-2.4538`
- `news_risk_high->fx_24h` score `-1.8917` n `130` status `ready` deltaP `-20.2022` edge `-0.0176` maxDD `-1.2197`
- `news_risk_high->crypto_major_1h` score `-1.918` n `130` status `ready` deltaP `-3.9498` edge `-0.0025` maxDD `-6.1465`
- `news_risk_high->equity_1h` score `-2.0027` n `130` status `ready` deltaP `-4.6361` edge `0.0021` maxDD `-13.2364`
- `news_risk_high->equity_24h` score `-2.4736` n `130` status `ready` deltaP `16.806` edge `0.8613` maxDD `-86.0244`
- `news_risk_high->commodity_1h` score `-2.7448` n `130` status `ready` deltaP `-13.2266` edge `-0.0039` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-2.7919` n `130` status `ready` deltaP `-5.2744` edge `0.0369` maxDD `-13.4186`
- `news_risk_high->metal_4h` score `-4.2119` n `130` status `ready` deltaP `-9.6599` edge `-0.0658` maxDD `-6.6632`
- `news_risk_high->commodity_4h` score `-4.5724` n `130` status `ready` deltaP `-20.326` edge `-0.0101` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-5.7539` n `130` status `ready` deltaP `5.6755` edge `0.0603` maxDD `-36.8767`
- `news_risk_high->metal_24h` score `-6.1405` n `130` status `ready` deltaP `-10.5696` edge `-0.2509` maxDD `-8.5609`
- `news_risk_high->commodity_24h` score `-10.6134` n `130` status `ready` deltaP `-21.951` edge `0.0372` maxDD `-42.3584`
- `news_risk_high->crypto_major_24h` score `-12.3275` n `130` status `ready` deltaP `-20.1357` edge `0.0199` maxDD `-55.703`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
