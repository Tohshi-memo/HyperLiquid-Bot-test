# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T12:22:22.673018+00:00`
- Price records: `672`
- Market context records: `5247`
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

- `market_context_high->unknown_24h` score `24.9822` n `137` status `ready` deltaP `30.9345` edge `1.8946` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.0891` n `137` status `ready` deltaP `32.1586` edge `1.1592` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `4.7719` n `137` status `ready` deltaP `18.878` edge `0.6605` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.4029` n `155` status `ready` deltaP `14.9135` edge `0.4274` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1242` n `155` status `ready` deltaP `15.2892` edge `0.471` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.2964` n `137` status `ready` deltaP `18.6676` edge `0.6298` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `2.2022` n `155` status `ready` deltaP `17.1351` edge `0.1715` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `0.9146` n `160` status `ready` deltaP `8.3346` edge `0.0848` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5693` n `137` status `ready` deltaP `13.211` edge `0.0489` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4141` n `160` status `ready` deltaP `4.4199` edge `0.1012` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.4052` n `155` status `ready` deltaP `7.5501` edge `0.1473` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.3806` n `160` status `ready` deltaP `6.3398` edge `0.114` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.0102` n `137` status `ready` deltaP `19.485` edge `0.0349` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0982` n `160` status `ready` deltaP `6.2313` edge `0.0468` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1236` n `160` status `ready` deltaP `4.5958` edge `0.0127` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1572` n `160` status `ready` deltaP `4.3301` edge `0.0084` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3395` n `160` status `ready` deltaP `0.378` edge `-0.0008` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.7963` n `155` status `ready` deltaP `-0.0148` edge `0.0014` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8253` n `155` status `ready` deltaP `3.9241` edge `0.0168` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.1319` n `160` status `ready` deltaP `-1.3735` edge `-0.0043` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
