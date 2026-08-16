# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T19:22:26.036682+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `221.956` n `86` status `ready` deltaP `-22.9126` edge `28.877` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.8775` n `86` status `ready` deltaP `41.2508` edge `0.3872` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.3915` n `123` status `ready` deltaP `13.7195` edge `0.0716` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.1062` n `126` status `ready` deltaP `1.9628` edge `0.0192` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2586` n `123` status `ready` deltaP `4.878` edge `0.0064` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.3145` n `126` status `ready` deltaP `1.3331` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4828` n `126` status `ready` deltaP `2.3216` edge `-0.0058` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8008` n `126` status `ready` deltaP `-7.1262` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.8023` n `123` status `ready` deltaP `8.6382` edge `-0.0114` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.3565` n `86` status `ready` deltaP `-6.565` edge `0.0306` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6314` n `126` status `ready` deltaP `-9.0272` edge `-0.045` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.8863` n `86` status `ready` deltaP `-9.1852` edge `0.0706` maxDD `-7.0954`
- `market_context_high->index_4h` score `-1.9565` n `123` status `ready` deltaP `-11.0772` edge `-0.0083` maxDD `-0.8045`
- `market_context_high->index_24h` score `-2.0099` n `86` status `ready` deltaP `-6.9848` edge `-0.0678` maxDD `-2.1313`
- `market_context_high->crypto_alt_1h` score `-2.0295` n `126` status `ready` deltaP `-2.3358` edge `-0.0196` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.1585` n `126` status `ready` deltaP `-6.0047` edge `-0.0332` maxDD `-5.5318`
- `market_context_high->crypto_major_4h` score `-3.6817` n `123` status `ready` deltaP `-2.0325` edge `-0.0659` maxDD `-12.8552`
- `market_context_high->crypto_major_24h` score `-4.6153` n `86` status `ready` deltaP `-6.1086` edge `-0.0065` maxDD `-32.5588`
- `market_context_high->unknown_1h` score `-6.9399` n `126` status `ready` deltaP `1.3782` edge `-0.5478` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-7.9545` n `123` status `ready` deltaP `-11.0264` edge `-0.1015` maxDD `-26.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
