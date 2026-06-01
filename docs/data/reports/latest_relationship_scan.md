# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T22:07:23.884907+00:00`
- Price records: `672`
- Market context records: `2601`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.8755` n `138` status `ready` deltaP `18.0178` edge `0.569` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.4263` n `146` status `ready` deltaP `25.3488` edge `0.5511` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6986` n `146` status `ready` deltaP `15.6783` edge `0.3847` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4743` n `146` status `ready` deltaP `11.8797` edge `0.1624` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `1.292` n `138` status `ready` deltaP `3.3892` edge `0.7229` maxDD `-39.0265`
- `market_context_high->unknown_4h` score `0.8767` n `146` status `ready` deltaP `7.6846` edge `0.1268` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.8348` n `146` status `ready` deltaP `9.3122` edge `0.1269` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.8226` n `138` status `ready` deltaP `8.7032` edge `0.1086` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2048` n `146` status `ready` deltaP `8.8227` edge `0.0424` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0676` n `146` status `ready` deltaP `4.6899` edge `0.0125` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3229` n `146` status `ready` deltaP `2.3993` edge `0.0234` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4722` n `146` status `ready` deltaP `4.9032` edge `0.0158` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5589` n `146` status `ready` deltaP `1.86` edge `0.0158` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.6158` n `146` status `ready` deltaP `4.6546` edge `0.0564` maxDD `-4.7664`
- `market_context_high->equity_24h` score `-0.6248` n `138` status `ready` deltaP `12.968` edge `-0.0715` maxDD `-2.3615`
- `market_context_high->fx_1h` score `-0.6389` n `146` status `ready` deltaP `-0.5352` edge `0.0038` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.757` n `146` status `ready` deltaP `0.2215` edge `0.0193` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.901` n `146` status `ready` deltaP `-0.2255` edge `0.0122` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9314` n `138` status `ready` deltaP `3.3364` edge `-0.0005` maxDD `-1.6157`
- `market_context_high->commodity_4h` score `-1.1535` n `146` status `ready` deltaP `2.5768` edge `0.0292` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
