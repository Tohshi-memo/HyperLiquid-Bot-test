# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T18:37:16.308357+00:00`
- Price records: `672`
- Market context records: `1449`
- Flow alert records: `6085`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `market_context_high->crypto_alt_24h` score `13.0422` n `159` status `ready` deltaP `28.8424` edge `1.0962` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9422` n `159` status `ready` deltaP `27.4764` edge `0.9252` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.8231` n `159` status `ready` deltaP `14.5309` edge `1.0551` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3666` n `159` status `ready` deltaP `19.6672` edge `0.3414` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.1689` n `159` status `ready` deltaP `12.8538` edge `0.4944` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5646` n `221` status `ready` deltaP `7.3771` edge `0.1642` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2581` n `159` status `ready` deltaP `11.4321` edge `0.0502` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1153` n `228` status `ready` deltaP `3.5246` edge `0.0134` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1321` n `228` status `ready` deltaP `1.996` edge `0.0357` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.4666` n `221` status `ready` deltaP `10.5707` edge `0.2226` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.4685` n `228` status `ready` deltaP `0.8352` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4997` n `221` status `ready` deltaP `0.9381` edge `0.061` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.6164` n `228` status `ready` deltaP `1.6494` edge `0.04` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0444` n `221` status `ready` deltaP `-4.1607` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.0684` n `221` status `ready` deltaP `5.5886` edge `0.1446` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1795` n `228` status `ready` deltaP `4.709` edge `0.0039` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.1889` n `228` status `ready` deltaP `-1.1766` edge `0.0009` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6967` n `228` status `ready` deltaP `-1.4103` edge `0.0037` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.9235` n `221` status `ready` deltaP `7.604` edge `0.0582` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.1839` n `221` status `ready` deltaP `-11.5337` edge `-0.0548` maxDD `-9.7864`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
