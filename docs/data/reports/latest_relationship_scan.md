# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T11:37:28.885852+00:00`
- Price records: `672`
- Market context records: `5244`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7568`

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

- `market_context_high->unknown_24h` score `24.5308` n `134` status `ready` deltaP `31.2163` edge `1.8551` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.5529` n `134` status `ready` deltaP `32.8565` edge `1.1932` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `5.5125` n `134` status `ready` deltaP `19.6155` edge `0.7048` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.3173` n `155` status `ready` deltaP `14.6086` edge `0.4223` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0966` n `155` status `ready` deltaP `15.2892` edge `0.4687` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2118` n `155` status `ready` deltaP `17.1351` edge `0.1723` maxDD `-5.5109`
- `market_context_high->equity_24h` score `2.0138` n `134` status `ready` deltaP `18.3898` edge `0.6081` maxDD `-40.0306`
- `market_context_high->unknown_1h` score `0.9338` n `160` status `ready` deltaP `8.4843` edge `0.0854` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5832` n `134` status `ready` deltaP `13.3396` edge `0.0492` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3865` n `160` status `ready` deltaP `4.4199` edge `0.0989` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3674` n `160` status `ready` deltaP `6.3398` edge `0.1129` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.34` n `155` status `ready` deltaP `7.2452` edge `0.1439` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.0393` n `134` status `ready` deltaP `18.864` edge `0.0327` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0646` n `160` status `ready` deltaP `6.381` edge `0.0486` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1337` n `160` status `ready` deltaP `4.4461` edge `0.0124` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1381` n `160` status `ready` deltaP `4.4798` edge `0.009` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3473` n `160` status `ready` deltaP `0.2283` edge `-0.0008` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.7947` n `155` status `ready` deltaP `-0.0148` edge `0.0016` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8119` n `155` status `ready` deltaP `4.0765` edge `0.0169` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.0959` n `160` status `ready` deltaP `-1.0741` edge `-0.0033` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
