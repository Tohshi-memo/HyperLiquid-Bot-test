# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T14:22:15.099746+00:00`
- Price records: `672`
- Market context records: `1745`
- Flow alert records: `6926`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1674` n `158` status `ready` deltaP `26.4123` edge `0.6638` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8215` n `196` status `ready` deltaP `20.3615` edge `0.526` maxDD `-9.1295`
- `market_context_high->index_24h` score `4.3933` n `158` status `ready` deltaP `18.9676` edge `0.3625` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `4.3871` n `158` status `ready` deltaP `15.3653` edge `0.7952` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.1345` n `196` status `ready` deltaP `21.1952` edge `0.4438` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `2.9913` n `196` status `ready` deltaP `13.1844` edge `0.3885` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.9011` n `158` status `ready` deltaP `17.4758` edge `0.6151` maxDD `-33.1875`
- `market_context_high->equity_4h` score `2.893` n `196` status `ready` deltaP `15.3497` edge `0.2482` maxDD `-5.0894`
- `market_context_high->crypto_alt_1h` score `0.7417` n `196` status `ready` deltaP `7.2712` edge `0.1157` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.7389` n `196` status `ready` deltaP `10.6459` edge `0.0995` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.6491` n `158` status `ready` deltaP `19.8868` edge `0.7801` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.1729` n `196` status `ready` deltaP `4.598` edge `0.0911` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0263` n `196` status `ready` deltaP `4.6713` edge `0.0519` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `0.0186` n `158` status `ready` deltaP `20.9036` edge `1.0431` maxDD `-88.8062`
- `market_context_high->index_1h` score `-0.2598` n `196` status `ready` deltaP `3.3179` edge `0.0194` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2849` n `196` status `ready` deltaP `12.444` edge `0.1497` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.498` n `196` status `ready` deltaP `6.2447` edge `0.0281` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6726` n `158` status `ready` deltaP `6.4135` edge `0.0061` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6887` n `196` status `ready` deltaP `-3.5653` edge `-0.0013` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.6474` n `196` status `ready` deltaP `0.3391` edge `0.0074` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
