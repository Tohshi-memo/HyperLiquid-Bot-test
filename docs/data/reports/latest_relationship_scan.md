# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T12:52:17.089484+00:00`
- Price records: `672`
- Market context records: `1424`
- Flow alert records: `6014`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.7884` n `154` status `ready` deltaP `27.3539` edge `0.9132` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.6837` n `154` status `ready` deltaP `28.7811` edge `0.9834` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.6521` n `154` status `ready` deltaP `11.9882` edge `1.0578` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8013` n `154` status `ready` deltaP `19.3813` edge `0.2962` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6007` n `154` status `ready` deltaP `12.5271` edge `0.3659` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9086` n `202` status `ready` deltaP `5.2373` edge `0.1238` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0635` n `154` status `ready` deltaP `9.3592` edge `0.0478` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1999` n `210` status `ready` deltaP `3.1124` edge `0.0091` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3167` n `210` status `ready` deltaP `1.9689` edge `0.0205` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4209` n `210` status `ready` deltaP `2.0673` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5754` n `210` status `ready` deltaP `0.72` edge `0.0238` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.6307` n `210` status `ready` deltaP `-0.4762` edge `0.0121` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.7106` n `202` status `ready` deltaP `-0.1675` edge `0.0508` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.9346` n `210` status `ready` deltaP `3.9307` edge `-0.014` maxDD `-6.2283`
- `market_context_high->crypto_alt_4h` score `-1.2042` n `202` status `ready` deltaP `7.8015` edge `0.1796` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2962` n `202` status `ready` deltaP `5.29` edge `0.1276` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6116` n `202` status `ready` deltaP `-4.1159` edge `-0.0098` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.8768` n `210` status `ready` deltaP `-2.0416` edge `-0.0071` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.5984` n `202` status `ready` deltaP `-10.0896` edge `-0.0112` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8435` n `202` status `ready` deltaP `4.149` edge `-0.0048` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
