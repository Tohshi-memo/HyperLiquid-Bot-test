# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T12:52:29.247468+00:00`
- Price records: `672`
- Market context records: `7030`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_1h` score `-0.2714` n `215` status `ready` deltaP `1.8472` edge `0.001` maxDD `-0.5155`
- `market_context_high->fx_4h` score `-0.5212` n `215` status `ready` deltaP `11.7357` edge `0.0079` maxDD `-1.5701`
- `market_context_high->crypto_alt_1h` score `-0.5527` n `215` status `ready` deltaP `1.692` edge `0.0291` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6688` n `215` status `ready` deltaP `-1.5688` edge `0.0015` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6829` n `215` status `ready` deltaP `0.5055` edge `0.0002` maxDD `-2.2895`
- `market_context_high->unknown_24h` score `-1.0269` n `202` status `ready` deltaP `-7.3415` edge `0.3723` maxDD `-18.7342`
- `market_context_high->crypto_major_1h` score `-1.0496` n `215` status `ready` deltaP `3.205` edge `0.0264` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.1757` n `215` status `ready` deltaP `-2.6863` edge `0.0023` maxDD `-2.9228`
- `market_context_high->commodity_1h` score `-1.285` n `215` status `ready` deltaP `-3.9054` edge `-0.0182` maxDD `-2.0281`
- `market_context_high->index_4h` score `-1.8907` n `215` status `ready` deltaP `6.3457` edge `-0.0148` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9864` n `215` status `ready` deltaP `5.2127` edge `0.0089` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.0769` n `215` status `ready` deltaP `-6.0323` edge `0.0822` maxDD `-8.5384`
- `market_context_high->commodity_4h` score `-2.1226` n `215` status `ready` deltaP `-3.9968` edge `-0.0342` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.5332` n `202` status `ready` deltaP `-2.1624` edge `-0.0658` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.7116` n `215` status `ready` deltaP `1.1238` edge `0.0234` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.8944` n `215` status `ready` deltaP `3.1465` edge `-0.0154` maxDD `-15.0753`
- `market_context_high->crypto_major_4h` score `-3.0512` n `215` status `ready` deltaP `2.2299` edge `0.0224` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7824` n `202` status `ready` deltaP `-3.0665` edge `-0.0128` maxDD `-3.8899`
- `market_context_high->equity_4h` score `-7.2775` n `215` status `ready` deltaP `4.2938` edge `-0.0746` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.5998` n `202` status `ready` deltaP `-12.072` edge `-0.0559` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
