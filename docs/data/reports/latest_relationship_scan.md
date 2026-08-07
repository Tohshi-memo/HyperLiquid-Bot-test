# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T14:07:36.209391+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->metal_24h` score `1.0487` n `110` status `ready` deltaP `3.2782` edge `0.1523` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `0.8875` n `114` status `ready` deltaP `12.0133` edge `0.0785` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.7963` n `121` status `ready` deltaP `10.9294` edge `0.0351` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.5405` n `110` status `ready` deltaP `21.1018` edge `0.0477` maxDD `-4.1933`
- `market_context_high->fx_1h` score `0.1519` n `121` status `ready` deltaP `9.2047` edge `-0.0021` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2074` n `114` status `ready` deltaP `8.3868` edge `0.0035` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4613` n `121` status `ready` deltaP `-1.5205` edge `-0.007` maxDD `-1.36`
- `market_context_high->index_1h` score `-0.9752` n `121` status `ready` deltaP `-2.5746` edge `-0.0107` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0123` n `110` status `ready` deltaP `0.4189` edge `0.085` maxDD `-6.1056`
- `market_context_high->metal_4h` score `-1.1716` n `114` status `ready` deltaP `-0.6017` edge `-0.006` maxDD `-2.343`
- `market_context_high->crypto_alt_1h` score `-1.3094` n `121` status `ready` deltaP `-4.5331` edge `-0.0151` maxDD `-2.4371`
- `market_context_high->equity_1h` score `-1.3714` n `121` status `ready` deltaP `2.9173` edge `-0.0388` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.9421` n `114` status `ready` deltaP `1.1473` edge `-0.0305` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.3711` n `114` status `ready` deltaP `-6.4051` edge `-0.0308` maxDD `-4.594`
- `market_context_high->crypto_major_1h` score `-2.4983` n `121` status `ready` deltaP `-5.3719` edge `-0.0403` maxDD `-7.2328`
- `market_context_high->crypto_alt_24h` score `-3.651` n `110` status `ready` deltaP `-9.3368` edge `-0.0977` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.8262` n `114` status `ready` deltaP `-6.9801` edge `-0.1776` maxDD `-25.2357`
- `market_context_high->equity_4h` score `-6.2685` n `114` status `ready` deltaP `-1.4067` edge `-0.2654` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2762` n `110` status `ready` deltaP `10.2853` edge `0.0033` maxDD `-52.7876`
- `market_context_high->crypto_major_24h` score `-7.1311` n `110` status `ready` deltaP `-7.3547` edge `-0.3229` maxDD `-32.3854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
