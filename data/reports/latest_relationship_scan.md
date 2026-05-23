# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T10:37:15.421676+00:00`
- Price records: `672`
- Market context records: `1622`
- Flow alert records: `6577`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.4388` n `191` status `ready` deltaP `25.9653` edge `0.9394` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.0416` n `191` status `ready` deltaP `18.1446` edge `0.2703` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4445` n `191` status `ready` deltaP `11.8391` edge `0.1509` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.5749` n `191` status `ready` deltaP `14.113` edge `0.3064` maxDD `-19.4759`
- `market_context_high->crypto_major_4h` score `0.3435` n `191` status `ready` deltaP `10.1432` edge `0.2473` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.1331` n `191` status `ready` deltaP `16.7448` edge `0.3893` maxDD `-33.1875`
- `market_context_high->fx_24h` score `-0.2472` n `191` status `ready` deltaP `7.9207` edge `0.0315` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.2491` n `195` status `ready` deltaP `1.1738` edge `0.0626` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.3898` n `195` status `ready` deltaP `2.3653` edge `0.0326` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6466` n `195` status `ready` deltaP `0.8683` edge `0.0035` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.8053` n `191` status `ready` deltaP `0.7782` edge `0.0366` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.8098` n `195` status `ready` deltaP `-0.1735` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.9191` n `195` status `ready` deltaP `-1.5815` edge `0.0284` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0315` n `195` status `ready` deltaP `0.747` edge `0.0012` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2305` n `195` status `ready` deltaP `3.9513` edge `0.0047` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3682` n `191` status `ready` deltaP `9.116` edge `0.0944` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3828` n `191` status `ready` deltaP `-10.5279` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->crypto_major_24h` score `-1.5883` n `191` status `ready` deltaP `22.1432` edge `0.5786` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `-3.5247` n `191` status `ready` deltaP `22.1677` edge `0.7394` maxDD `-88.8062`
- `market_context_high->commodity_4h` score `-5.1866` n `191` status `ready` deltaP `-13.8808` edge `-0.1097` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
