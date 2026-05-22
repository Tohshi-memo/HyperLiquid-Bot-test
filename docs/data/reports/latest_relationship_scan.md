# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T08:37:22.220566+00:00`
- Price records: `672`
- Market context records: `1510`
- Flow alert records: `6258`
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

- `market_context_high->metal_24h` score `14.0892` n `159` status `ready` deltaP `23.3327` edge `1.1186` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1678` n `159` status `ready` deltaP `28.8424` edge `0.94` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7248` n `159` status `ready` deltaP `27.8892` edge `0.821` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6754` n `159` status `ready` deltaP `19.6672` edge `0.2838` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4037` n `159` status `ready` deltaP `12.8538` edge `0.3473` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0305` n `159` status `ready` deltaP `19.1071` edge `0.0634` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8362` n `185` status `ready` deltaP `5.6369` edge `0.1151` maxDD `-3.6396`
- `market_context_high->equity_1h` score `-0.3281` n `191` status `ready` deltaP `0.6262` edge `0.0285` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3414` n `191` status `ready` deltaP `1.9736` edge `0.0049` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4917` n `191` status `ready` deltaP `0.6333` edge `0.0351` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5139` n `191` status `ready` deltaP `0.0353` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7518` n `191` status `ready` deltaP `-0.4867` edge `-0.001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7655` n `191` status `ready` deltaP `5.1956` edge `0.0008` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.8296` n `185` status `ready` deltaP `8.67` edge `0.1678` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8571` n `185` status `ready` deltaP `5.0247` edge `0.1275` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0329` n `191` status `ready` deltaP `-1.0863` edge `0.0105` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2132` n `185` status `ready` deltaP `10.6929` edge `0.0968` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.3368` n `185` status `ready` deltaP `-4.4397` edge `0.0271` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6549` n `185` status `ready` deltaP `-5.1624` edge `-0.0106` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-1.7162` n `159` status `ready` deltaP `-2.4076` edge `0.146` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
