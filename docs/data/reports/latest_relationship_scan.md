# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T21:37:29.560900+00:00`
- Price records: `672`
- Market context records: `5706`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.981` n `264` status `ready` deltaP `11.9411` edge `0.2226` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0695` n `214` status `ready` deltaP `16.6975` edge `0.5337` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.8091` n `264` status `ready` deltaP `9.0493` edge `0.168` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1874` n `264` status `ready` deltaP `6.7027` edge `0.1348` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.244` n `276` status `ready` deltaP `2.3865` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.3634` n `276` status `ready` deltaP `3.8119` edge `0.0399` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4426` n `276` status `ready` deltaP `1.6771` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5121` n `276` status `ready` deltaP `2.1414` edge `0.0374` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5735` n `276` status `ready` deltaP `3.6449` edge `0.0286` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6405` n `276` status `ready` deltaP `0.0781` edge `0.0042` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0651` n `214` status `ready` deltaP `11.5362` edge `0.0431` maxDD `-3.5247`
- `market_context_high->commodity_1h` score `-1.0841` n `276` status `ready` deltaP `-0.8895` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2469` n `264` status `ready` deltaP `2.6515` edge `0.0059` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2739` n `264` status `ready` deltaP `-0.5543` edge `0.0091` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.672` n `264` status `ready` deltaP `-8.1301` edge `-0.0508` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8927` n `214` status `ready` deltaP `2.1223` edge `0.0292` maxDD `-18.1364`
- `market_context_high->commodity_4h` score `-3.9281` n `264` status `ready` deltaP `-4.3329` edge `-0.0309` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.2745` n `214` status `ready` deltaP `6.1478` edge `0.0485` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9609` n `214` status `ready` deltaP `-7.6519` edge `-0.242` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.0911` n `214` status `ready` deltaP `-10.9196` edge `-0.0739` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
