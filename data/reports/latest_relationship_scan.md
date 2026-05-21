# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T14:07:21.866920+00:00`
- Price records: `672`
- Market context records: `1429`
- Flow alert records: `6029`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8786`

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

- `market_context_high->crypto_alt_24h` score `11.8745` n `154` status `ready` deltaP `28.7811` edge `0.9993` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.7986` n `154` status `ready` deltaP `12.3354` edge `1.0677` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.72` n `154` status `ready` deltaP `27.3539` edge `0.9075` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8781` n `154` status `ready` deltaP `19.3813` edge `0.3026` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8851` n `154` status `ready` deltaP `12.5271` edge `0.3896` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0426` n `203` status `ready` deltaP `5.9518` edge `0.1302` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0839` n `154` status `ready` deltaP `9.3592` edge `0.0495` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1797` n `215` status `ready` deltaP `3.1403` edge `0.0106` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2753` n `215` status `ready` deltaP `2.306` edge `0.0217` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5429` n `215` status `ready` deltaP `1.2429` edge `-0.0028` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.6195` n `203` status `ready` deltaP `0.2508` edge `0.0556` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.6447` n `215` status `ready` deltaP `-0.6817` edge `0.0123` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8058` n `215` status `ready` deltaP `1.1572` edge `0.0275` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9567` n `215` status `ready` deltaP `3.6485` edge `-0.0134` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.1301` n `203` status `ready` deltaP `8.2467` edge `0.1828` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3208` n `203` status `ready` deltaP `4.9974` edge `0.1275` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5741` n `203` status `ready` deltaP `-3.7524` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.789` n `215` status `ready` deltaP `-1.4998` edge `-0.0034` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.6977` n `203` status `ready` deltaP `-10.5446` edge `-0.0209` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.722` n `203` status `ready` deltaP `4.6332` edge `0.0045` maxDD `-11.9775`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
