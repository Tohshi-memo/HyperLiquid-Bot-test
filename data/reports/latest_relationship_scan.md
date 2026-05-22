# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T10:37:15.453134+00:00`
- Price records: `672`
- Market context records: `1518`
- Flow alert records: `6282`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `14.2835` n `159` status `ready` deltaP `24.3514` edge `1.128` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2398` n `159` status `ready` deltaP `28.8424` edge `0.946` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7639` n `159` status `ready` deltaP `28.0628` edge `0.8231` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6958` n `159` status `ready` deltaP `19.6672` edge `0.2855` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3605` n `159` status `ready` deltaP `12.8538` edge `0.3437` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0403` n `159` status `ready` deltaP `19.2152` edge `0.0635` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8029` n `184` status `ready` deltaP `5.6402` edge `0.1123` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.5063` n `196` status `ready` deltaP `0.8066` edge `0.0031` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.5813` n `196` status `ready` deltaP `-0.1436` edge `0.0288` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.7172` n `196` status `ready` deltaP `-1.3228` edge `0.0174` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.8386` n `184` status `ready` deltaP `8.8415` edge `0.1655` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.87` n `196` status `ready` deltaP `-0.9257` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.8869` n `184` status `ready` deltaP `4.4075` edge `0.1278` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0347` n `196` status `ready` deltaP `-1.0754` edge `0.0102` maxDD `-6.1883`
- `market_context_high->metal_1h` score `-1.0789` n `196` status `ready` deltaP `5.7406` edge `0.0054` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.1351` n `184` status `ready` deltaP `11.1745` edge `0.1001` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.1955` n `196` status `ready` deltaP `-0.7485` edge `-0.0025` maxDD `-4.7041`
- `market_context_high->index_4h` score `-1.3218` n `184` status `ready` deltaP `-4.2683` edge `0.0272` maxDD `-3.7119`
- `market_context_high->unknown_24h` score `-1.6137` n `159` status `ready` deltaP `-2.5812` edge `0.1557` maxDD `-10.1706`
- `market_context_high->fx_4h` score `-1.691` n `184` status `ready` deltaP `-5.6137` edge `-0.0106` maxDD `-1.4313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
