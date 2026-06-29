# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T21:52:28.452600+00:00`
- Price records: `672`
- Market context records: `5185`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `21.9254` n `82` status `ready` deltaP `32.9692` edge `1.6263` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.5141` n `82` status `ready` deltaP `26.0713` edge `1.2352` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.0462` n `82` status `ready` deltaP `26.952` edge `0.9962` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.6621` n `153` status `ready` deltaP `19.7194` edge `0.4426` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4992` n `153` status `ready` deltaP `13.2672` edge `0.4464` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4081` n `153` status `ready` deltaP `13.7683` edge `0.5048` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5724` n `155` status `ready` deltaP `9.2872` edge `0.2166` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2746` n `153` status `ready` deltaP `9.0427` edge `0.2098` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5145` n `155` status `ready` deltaP `4.2042` edge `0.111` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4973` n `155` status `ready` deltaP `6.2536` edge `0.1243` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.2885` n `155` status `ready` deltaP `7.9148` edge `0.0678` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1454` n `82` status `ready` deltaP `11.1831` edge `0.0271` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0226` n `155` status `ready` deltaP `5.7833` edge `0.0137` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.053` n `155` status `ready` deltaP `5.1593` edge `0.018` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2744` n `155` status `ready` deltaP `1.5096` edge `0.0` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4117` n `153` status `ready` deltaP `6.2301` edge `0.0359` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5132` n `153` status `ready` deltaP `4.62` edge `0.0068` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5962` n `155` status `ready` deltaP `0.7253` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.0447` n `82` status `ready` deltaP `6.6099` edge `-0.0145` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.211` n `153` status `ready` deltaP `1.0641` edge `0.038` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
