# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T04:52:27.146014+00:00`
- Price records: `672`
- Market context records: `5216`
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

- `market_context_high->unknown_24h` score `18.3476` n `110` status `ready` deltaP `33.5164` edge `1.3245` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.148` n `110` status `ready` deltaP `31.7645` edge `1.3334` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.0721` n `110` status `ready` deltaP `27.3011` edge `0.9127` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.2849` n `155` status `ready` deltaP `13.694` edge `0.4257` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.209` n `155` status `ready` deltaP `14.0696` edge `0.4862` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `4.1829` n `155` status `ready` deltaP `18.6595` edge `0.3264` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.9821` n `155` status `ready` deltaP `8.8381` edge `0.1704` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.608` n `155` status `ready` deltaP `4.803` edge `0.1148` maxDD `-5.0257`
- `market_context_high->fx_24h` score `0.5866` n `110` status `ready` deltaP `13.7721` edge `0.0466` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.58` n `155` status `ready` deltaP `6.7027` edge `0.1282` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.2063` n `155` status `ready` deltaP `6.7879` edge `0.1358` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1589` n `155` status `ready` deltaP `3.6623` edge `0.0144` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.1875` n `155` status `ready` deltaP `4.9208` edge `0.0481` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2457` n `155` status `ready` deltaP `3.0887` edge `0.0093` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2604` n `155` status `ready` deltaP `1.809` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.4656` n `110` status `ready` deltaP `13.5448` edge `0.0135` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6089` n `155` status `ready` deltaP `3.034` edge `0.0051` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6148` n `155` status `ready` deltaP `0.4259` edge `-0.0008` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.7843` n `155` status `ready` deltaP `4.0765` edge `0.0192` maxDD `-2.9391`
- `market_context_high->equity_24h` score `-1.0938` n `110` status `ready` deltaP `15.6219` edge `0.3185` maxDD `-40.0306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
