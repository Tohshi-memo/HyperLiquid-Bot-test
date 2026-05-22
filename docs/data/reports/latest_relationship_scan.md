# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T01:52:21.417148+00:00`
- Price records: `672`
- Market context records: `1482`
- Flow alert records: `6175`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->crypto_alt_24h` score `12.48` n `172` status `ready` deltaP `28.985` edge `1.0484` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.3864` n `172` status `ready` deltaP `27.3538` edge `0.8797` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0116` n `172` status `ready` deltaP `16.0126` edge `0.9776` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1918` n `172` status `ready` deltaP `20.3327` edge `0.3224` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.1661` n `172` status `ready` deltaP `13.6144` edge `0.4891` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5902` n `212` status `ready` deltaP `7.1416` edge `0.1679` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.5225` n `172` status `ready` deltaP `14.9467` edge `0.0488` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1375` n `212` status `ready` deltaP `12.4367` edge `0.2605` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0363` n `212` status `ready` deltaP `2.7143` edge `0.0389` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1466` n `212` status `ready` deltaP `3.1183` edge `0.0135` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4588` n `212` status `ready` deltaP `2.045` edge `0.0505` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.5627` n `212` status `ready` deltaP `0.2416` edge `0.0604` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-0.7247` n `212` status `ready` deltaP `6.9288` edge `0.1643` maxDD `-13.3376`
- `market_context_high->fx_1h` score `-0.8815` n `212` status `ready` deltaP `-1.0253` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0251` n `212` status `ready` deltaP `-4.3546` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1692` n `212` status `ready` deltaP `5.3921` edge `0.0002` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.214` n `212` status `ready` deltaP `-1.2202` edge `-0.0009` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5267` n `212` status `ready` deltaP `-0.6355` edge `0.0127` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7486` n `212` status `ready` deltaP `8.1857` edge `0.0689` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0689` n `212` status `ready` deltaP `-11.988` edge `-0.0701` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
