# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T14:07:20.140081+00:00`
- Price records: `672`
- Market context records: `1744`
- Flow alert records: `6922`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8852`

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

- `market_context_high->metal_24h` score `7.1542` n `158` status `ready` deltaP `26.4123` edge `0.6627` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8107` n `196` status `ready` deltaP `20.3615` edge `0.5251` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.4358` n `158` status `ready` deltaP `15.5386` edge `0.7981` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.4041` n `158` status `ready` deltaP `18.9676` edge `0.3634` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.1225` n `196` status `ready` deltaP `21.1952` edge `0.4428` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0141` n `196` status `ready` deltaP `13.1844` edge `0.3904` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.9419` n `158` status `ready` deltaP `17.4758` edge `0.6185` maxDD `-33.1875`
- `market_context_high->equity_4h` score `2.876` n `196` status `ready` deltaP `15.1972` edge `0.2478` maxDD `-5.0894`
- `market_context_high->crypto_major_24h` score `0.747` n `158` status `ready` deltaP `20.0601` edge `0.7871` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.7341` n `196` status `ready` deltaP `10.6459` edge `0.0991` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7261` n `196` status `ready` deltaP `7.2712` edge `0.1144` maxDD `-4.1892`
- `market_context_high->crypto_major_1h` score `0.1573` n `196` status `ready` deltaP `4.598` edge `0.0898` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.1008` n `158` status `ready` deltaP `21.077` edge `1.0488` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0179` n `196` status `ready` deltaP `4.6713` edge `0.0512` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.261` n `196` status `ready` deltaP `3.3179` edge `0.0193` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2927` n `196` status `ready` deltaP `12.444` edge `0.1487` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5043` n `196` status `ready` deltaP `6.2447` edge `0.0273` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6714` n `158` status `ready` deltaP `6.4135` edge `0.0062` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6887` n `196` status `ready` deltaP `-3.5653` edge `-0.0013` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.639` n `196` status `ready` deltaP `0.3391` edge `0.0081` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
