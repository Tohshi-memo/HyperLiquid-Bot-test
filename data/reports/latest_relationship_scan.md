# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T02:22:29.660332+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `2890.9548` n `101` status `ready` deltaP `1.2153` edge `240.9048` maxDD `0.0`
- `market_context_high->unknown_1h` score `75.0267` n `44` status `ready` deltaP `10.1524` edge `6.1892` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.4318` n `44` status `ready` deltaP `28.1092` edge `4.1337` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.7998` n `44` status `ready` deltaP `14.9148` edge `2.2552` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.742` n `44` status `ready` deltaP `36.0954` edge `2.1026` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7095` n `44` status `ready` deltaP `31.9287` edge `0.4384` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7134` n `44` status `ready` deltaP `32.3074` edge `0.1179` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3714` n `44` status `ready` deltaP `37.8325` edge `0.0358` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9833` n `44` status `ready` deltaP `18.1264` edge `0.1654` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.292` n `44` status `ready` deltaP `9.1602` edge `0.1092` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.1785` n `101` status `ready` deltaP `17.3697` edge `0.0436` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `1.0724` n `44` status `ready` deltaP `8.8187` edge `0.104` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.0719` n `44` status `ready` deltaP `12.0169` edge `0.0495` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.0172` n `101` status `ready` deltaP `24.3416` edge `0.1329` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.9334` n `44` status `ready` deltaP `7.2201` edge `0.1201` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8008` n `44` status `ready` deltaP `12.1666` edge `0.0093` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2336` n `44` status `ready` deltaP `6.0152` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.0271` n `44` status `ready` deltaP `4.0011` edge `0.0645` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1202` n `139` status `ready` deltaP `2.3726` edge `0.0033` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
