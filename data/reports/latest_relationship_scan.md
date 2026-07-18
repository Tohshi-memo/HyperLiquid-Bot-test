# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T17:52:27.252340+00:00`
- Price records: `672`
- Market context records: `7165`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `market_context_high->fx_4h` score `0.0566` n `158` status `ready` deltaP `11.267` edge `0.0121` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.4012` n `170` status `ready` deltaP `1.925` edge `0.0013` maxDD `-0.4717`
- `market_context_high->crypto_alt_1h` score `-0.5532` n `170` status `ready` deltaP `0.7591` edge `0.0279` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6039` n `170` status `ready` deltaP `3.9785` edge `0.0371` maxDD `-7.6171`
- `market_context_high->unknown_1h` score `-0.6089` n `170` status `ready` deltaP `-1.4019` edge `0.0228` maxDD `-1.4688`
- `market_context_high->commodity_1h` score `-0.623` n `170` status `ready` deltaP `-0.3734` edge `-0.0153` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7913` n `170` status `ready` deltaP `0.6939` edge `-0.0041` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3334` n `170` status `ready` deltaP `-7.242` edge `-0.0049` maxDD `-2.0882`
- `market_context_high->unknown_4h` score `-2.0736` n `158` status `ready` deltaP `-6.3812` edge `0.0122` maxDD `-6.1736`
- `market_context_high->commodity_4h` score `-2.1323` n `158` status `ready` deltaP `-5.3488` edge `-0.0385` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9364` n `158` status `ready` deltaP `-10.4006` edge `-0.0123` maxDD `-5.2523`
- `market_context_high->equity_1h` score `-3.5078` n `170` status `ready` deltaP `-0.3223` edge `-0.0375` maxDD `-15.5469`
- `market_context_high->index_4h` score `-3.9365` n `158` status `ready` deltaP `-2.3754` edge `-0.0423` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5341` n `132` status `ready` deltaP `-13.7942` edge `-0.155` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.837` n `132` status `ready` deltaP `-14.4413` edge `-0.0241` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.8405` n `158` status `ready` deltaP `2.9793` edge `0.0121` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.4628` n `158` status `ready` deltaP `-2.7265` edge `-0.0274` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.1122` n `132` status `ready` deltaP `-32.6862` edge `-0.1101` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7224` n `132` status `ready` deltaP `-32.2285` edge `-0.1994` maxDD `-40.6752`
- `market_context_high->equity_4h` score `-14.8221` n `158` status `ready` deltaP `-4.0619` edge `-0.2121` maxDD `-66.6799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
