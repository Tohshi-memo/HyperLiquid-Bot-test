# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T11:37:25.842729+00:00`
- Price records: `672`
- Market context records: `5658`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.3419` n `188` status `ready` deltaP `15.2482` edge `0.6014` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9284` n `237` status `ready` deltaP `11.4618` edge `0.2302` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.5329` n `237` status `ready` deltaP `7.9912` edge `0.155` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.3529` n `188` status `ready` deltaP `17.8671` edge `0.055` maxDD `-2.2431`
- `market_context_high->crypto_alt_4h` score `0.1171` n `237` status `ready` deltaP `7.1364` edge `0.1471` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.275` n `249` status `ready` deltaP `1.705` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4105` n `249` status `ready` deltaP `5.1584` edge `0.0321` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5358` n `249` status `ready` deltaP `-0.1461` edge `-0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6327` n `249` status `ready` deltaP `1.4748` edge `0.0336` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8432` n `249` status `ready` deltaP `2.7126` edge `0.0362` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8703` n `249` status `ready` deltaP `1.099` edge `-0.0033` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.916` n `249` status `ready` deltaP `0.7665` edge `0.0054` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2424` n `237` status `ready` deltaP `2.5902` edge `0.0068` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0355` n `237` status `ready` deltaP `-1.689` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3597` n `188` status `ready` deltaP `8.8726` edge `0.037` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0686` n `237` status `ready` deltaP `-14.9789` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8032` n `237` status `ready` deltaP `-2.1875` edge `-0.0348` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.705` n `188` status `ready` deltaP `3.7862` edge `0.0367` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4308` n `188` status `ready` deltaP `-13.7965` edge `-0.2528` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.6484` n `188` status `ready` deltaP `-13.8963` edge `-0.1005` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
