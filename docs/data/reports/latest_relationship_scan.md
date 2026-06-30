# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T12:07:27.419944+00:00`
- Price records: `672`
- Market context records: `5246`
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

- `market_context_high->unknown_24h` score `24.8528` n `136` status `ready` deltaP `31.0866` edge `1.8828` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.3145` n `136` status `ready` deltaP `32.5163` edge `1.1756` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `5.0642` n `136` status `ready` deltaP `19.1176` edge `0.6791` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.3619` n `155` status `ready` deltaP `14.7611` edge `0.425` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.105` n `155` status `ready` deltaP `15.2892` edge `0.4694` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.2147` n `136` status `ready` deltaP `18.5764` edge `0.6236` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `2.2058` n `155` status `ready` deltaP `17.1351` edge `0.1718` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `0.9326` n `160` status `ready` deltaP `8.4843` edge `0.0853` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.574` n `136` status `ready` deltaP `13.2557` edge `0.049` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4021` n `160` status `ready` deltaP `4.4199` edge `0.1002` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.3702` n `155` status `ready` deltaP `7.3977` edge `0.1454` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.3698` n `160` status `ready` deltaP `6.3398` edge `0.1131` maxDD `-6.9639`
- `market_context_high->index_24h` score `-0.0059` n `136` status `ready` deltaP `19.281` edge `0.0342` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0982` n `160` status `ready` deltaP `6.2313` edge `0.0468` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1337` n `160` status `ready` deltaP `4.4461` edge `0.0124` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1548` n `160` status `ready` deltaP `4.3301` edge `0.0086` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.348` n `160` status `ready` deltaP `0.2283` edge `-0.0009` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.7963` n `155` status `ready` deltaP `-0.0148` edge `0.0014` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8265` n `155` status `ready` deltaP `3.9241` edge `0.0167` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.1127` n `160` status `ready` deltaP `-1.2238` edge `-0.0037` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
