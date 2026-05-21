# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T15:22:22.589364+00:00`
- Price records: `672`
- Market context records: `1435`
- Flow alert records: `6044`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `12.1457` n `154` status `ready` deltaP `28.7811` edge `1.0219` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.0313` n `154` status `ready` deltaP `13.2034` edge `1.0813` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6708` n `154` status `ready` deltaP `27.3539` edge `0.9034` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0305` n `154` status `ready` deltaP `19.3813` edge `0.3153` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.2499` n `154` status `ready` deltaP `12.5271` edge `0.42` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.1963` n `208` status `ready` deltaP `6.1328` edge `0.1418` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.132` n `154` status `ready` deltaP `9.7065` edge `0.0512` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1724` n `220` status `ready` deltaP `1.8372` edge `0.0334` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2062` n `220` status `ready` deltaP `3.0186` edge `0.0092` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.6297` n `220` status `ready` deltaP `-0.4491` edge `0.012` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.6863` n `208` status `ready` deltaP `-0.3284` edge `0.0539` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.7134` n `220` status `ready` deltaP `1.5623` edge `0.0325` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.7162` n `220` status `ready` deltaP `0.9363` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.9031` n `220` status `ready` deltaP `3.9902` edge `-0.0088` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.1224` n `208` status `ready` deltaP `8.478` edge `0.1819` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3115` n `208` status `ready` deltaP `4.8898` edge `0.129` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6136` n `208` status `ready` deltaP `-4.1862` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.6411` n `220` status `ready` deltaP `-0.8655` edge `0.0047` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7663` n `208` status `ready` deltaP `5.0305` edge `0.0092` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0822` n `208` status `ready` deltaP `-10.1431` edge `-0.0179` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
