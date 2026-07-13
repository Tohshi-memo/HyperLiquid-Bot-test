# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T07:07:25.378489+00:00`
- Price records: `672`
- Market context records: `6580`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `5.6431` n `148` status `ready` deltaP `9.3428` edge `0.738` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0064` n `210` status `ready` deltaP `-5.1297` edge `0.2915` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4103` n `148` status `ready` deltaP `13.9873` edge `0.2111` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3526` n `210` status `ready` deltaP `0.8583` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3893` n `210` status `ready` deltaP `7.3467` edge `0.0277` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5453` n `210` status `ready` deltaP `5.5917` edge `0.0241` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5545` n `210` status `ready` deltaP `-0.3807` edge `0.0034` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6048` n `210` status `ready` deltaP `-0.7086` edge `-0.0045` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9413` n `210` status `ready` deltaP `8.6847` edge `0.0094` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1465` n `210` status `ready` deltaP `2.2313` edge `0.0006` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.3191` n `210` status `ready` deltaP `-1.4315` edge `-0.0101` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3195` n `210` status `ready` deltaP `-4.0262` edge `-0.0024` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.5903` n `210` status `ready` deltaP `-15.9988` edge `0.2147` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7448` n `210` status `ready` deltaP `7.7338` edge `0.0562` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.763` n `210` status `ready` deltaP `-0.228` edge `-0.0033` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.978` n `210` status `ready` deltaP `4.9332` edge `0.0537` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1525` n `210` status `ready` deltaP `-1.5012` edge `0.0201` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-2.4567` n `148` status `ready` deltaP `4.9468` edge `0.0823` maxDD `-6.6002`
- `market_context_high->fx_24h` score `-3.745` n `148` status `ready` deltaP `-3.4706` edge `-0.0035` maxDD `-9.2795`
- `market_context_high->index_24h` score `-4.1355` n `148` status `ready` deltaP `0.2229` edge `-0.0052` maxDD `-10.9395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
