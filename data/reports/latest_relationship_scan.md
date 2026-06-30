# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T11:22:50.168600+00:00`
- Price records: `672`
- Market context records: `5243`
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

- `market_context_high->unknown_24h` score `24.3478` n `133` status `ready` deltaP `31.1939` edge `1.84` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.6323` n `133` status `ready` deltaP `32.8281` edge `1.2` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `5.7374` n `133` status `ready` deltaP `20.0475` edge `0.7165` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.3089` n `155` status `ready` deltaP `14.6086` edge `0.4216` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1002` n `155` status `ready` deltaP `15.2892` edge `0.469` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2178` n `155` status `ready` deltaP `17.1351` edge `0.1728` maxDD `-5.5109`
- `market_context_high->equity_24h` score `1.903` n `133` status `ready` deltaP `18.2944` edge `0.5995` maxDD `-40.0306`
- `market_context_high->unknown_1h` score `1.1012` n `159` status `ready` deltaP `8.4021` edge `0.0999` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5863` n `133` status `ready` deltaP `13.3785` edge `0.0492` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4522` n `159` status `ready` deltaP `4.7462` edge `0.1022` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4064` n `159` status `ready` deltaP `6.6621` edge `0.114` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.3206` n `155` status `ready` deltaP `7.0928` edge `0.1433` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.055` n `133` status `ready` deltaP `18.6508` edge `0.0321` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0707` n `159` status `ready` deltaP `6.2752` edge `0.0488` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1423` n `159` status `ready` deltaP `4.2971` edge `0.0123` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1478` n `159` status `ready` deltaP `4.3583` edge `0.009` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3287` n `159` status `ready` deltaP `0.5546` edge `-0.0006` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.7211` n `159` status `ready` deltaP `-1.2428` edge `-0.0033` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.794` n `155` status `ready` deltaP `-0.0148` edge `0.0017` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8107` n `155` status `ready` deltaP `4.0765` edge `0.017` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
