# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T08:52:20.878972+00:00`
- Price records: `672`
- Market context records: `1511`
- Flow alert records: `6261`
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

- `market_context_high->metal_24h` score `14.0856` n `159` status `ready` deltaP `23.3327` edge `1.1183` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.163` n `159` status `ready` deltaP `28.8424` edge `0.9396` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7512` n `159` status `ready` deltaP `27.8892` edge `0.8232` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6706` n `159` status `ready` deltaP `19.6672` edge `0.2834` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4157` n `159` status `ready` deltaP `12.8538` edge `0.3483` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0269` n `159` status `ready` deltaP `19.1071` edge `0.0631` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8748` n `185` status `ready` deltaP `5.7894` edge `0.1173` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.3201` n `192` status `ready` deltaP `2.1645` edge `0.0054` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3449` n `192` status `ready` deltaP `0.4459` edge `0.0283` maxDD `-2.8014`
- `market_context_high->crypto_alt_1h` score `-0.4962` n `192` status `ready` deltaP `0.5021` edge `0.0354` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.4996` n `192` status `ready` deltaP `0.2807` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7512` n `192` status `ready` deltaP `5.4111` edge `0.0012` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7701` n `192` status `ready` deltaP `-0.7485` edge `-0.0016` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.8092` n `185` status `ready` deltaP `8.8225` edge `0.1694` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8454` n `185` status `ready` deltaP `5.0247` edge `0.129` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0049` n `192` status `ready` deltaP `-0.8327` edge `0.0124` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.1902` n `185` status `ready` deltaP `10.8454` edge `0.0977` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.3344` n `185` status `ready` deltaP `-4.4397` edge `0.0273` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6537` n `185` status `ready` deltaP `-5.1624` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-1.7318` n `159` status `ready` deltaP `-2.4076` edge `0.1447` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
