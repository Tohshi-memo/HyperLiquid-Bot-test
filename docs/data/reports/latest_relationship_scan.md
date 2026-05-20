# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T23:22:17.620323+00:00`
- Price records: `672`
- Market context records: `1367`
- Flow alert records: `5848`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.137` n `140` status `ready` deltaP `31.8056` edge `0.9959` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.4963` n `140` status `ready` deltaP `13.6012` edge `1.1174` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.2965` n `140` status `ready` deltaP `28.5863` edge `0.8691` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1315` n `140` status `ready` deltaP `22.6389` edge `0.302` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6662` n `140` status `ready` deltaP `15.6547` edge `0.3505` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.9222` n `165` status `ready` deltaP `9.8817` edge `0.1648` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.7721` n `140` status `ready` deltaP `11.498` edge `0.0499` maxDD `-0.9768`
- `market_context_high->metal_4h` score `-0.0135` n `165` status `ready` deltaP `11.6509` edge `0.0643` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0483` n `177` status `ready` deltaP `4.1113` edge `0.0129` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1429` n `177` status `ready` deltaP `2.0155` edge `0.0241` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.1888` n `165` status `ready` deltaP `2.475` edge `0.0682` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.3254` n `177` status `ready` deltaP `1.3109` edge `-0.0039` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4423` n `177` status `ready` deltaP `5.9948` edge `0.0022` maxDD `-3.5762`
- `market_context_high->crypto_alt_1h` score `-0.5693` n `177` status `ready` deltaP `-0.4855` edge `0.0173` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.6986` n `177` status `ready` deltaP `-0.3501` edge `0.0056` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.0588` n `177` status `ready` deltaP `-2.6439` edge `-0.0116` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3563` n `165` status `ready` deltaP `-9.4087` edge `-0.0153` maxDD `-1.3356`
- `market_context_high->crypto_alt_4h` score `-1.5135` n `165` status `ready` deltaP `7.5351` edge `0.1556` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.9764` n `165` status `ready` deltaP `2.5785` edge `0.089` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-2.7556` n `165` status `ready` deltaP `0.485` edge `-0.1294` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
