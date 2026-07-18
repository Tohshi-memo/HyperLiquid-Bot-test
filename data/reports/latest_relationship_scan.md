# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T17:37:28.317492+00:00`
- Price records: `672`
- Market context records: `7164`
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

- `market_context_high->fx_4h` score `0.0432` n `158` status `ready` deltaP `11.1146` edge `0.012` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.4243` n `169` status `ready` deltaP `1.6361` edge `0.0013` maxDD `-0.4717`
- `market_context_high->crypto_alt_1h` score `-0.5766` n `169` status `ready` deltaP `0.4597` edge `0.0269` maxDD `-5.9775`
- `market_context_high->unknown_1h` score `-0.5889` n `169` status `ready` deltaP `-1.2871` edge `0.0237` maxDD `-1.4688`
- `market_context_high->crypto_major_1h` score `-0.6268` n `169` status `ready` deltaP `3.7035` edge `0.036` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.641` n `169` status `ready` deltaP `-0.6448` edge `-0.0158` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.8187` n `169` status `ready` deltaP `0.3667` edge `-0.0042` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-2.0707` n `169` status `ready` deltaP `-7.4682` edge `-0.005` maxDD `-2.0882`
- `market_context_high->unknown_4h` score `-2.0728` n `158` status `ready` deltaP `-6.3812` edge `0.0123` maxDD `-6.1736`
- `market_context_high->commodity_4h` score `-2.1311` n `158` status `ready` deltaP `-5.3488` edge `-0.0384` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9443` n `158` status `ready` deltaP `-10.5531` edge `-0.0123` maxDD `-5.2523`
- `market_context_high->equity_1h` score `-3.5456` n `169` status `ready` deltaP `-0.6599` edge `-0.0384` maxDD `-15.5469`
- `market_context_high->index_4h` score `-3.9499` n `158` status `ready` deltaP `-2.5278` edge `-0.0424` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5413` n `132` status `ready` deltaP `-13.7942` edge `-0.1556` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-4.8357` n `158` status `ready` deltaP `2.9793` edge `0.0125` maxDD `-25.1605`
- `market_context_high->fx_24h` score `-4.8545` n `132` status `ready` deltaP `-14.6149` edge `-0.0244` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.458` n `158` status `ready` deltaP `-2.7265` edge `-0.027` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.1369` n `132` status `ready` deltaP `-32.8598` edge `-0.111` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7061` n `132` status `ready` deltaP `-32.0549` edge `-0.1992` maxDD `-40.6752`
- `market_context_high->equity_4h` score `-14.8391` n `158` status `ready` deltaP `-4.2143` edge `-0.2125` maxDD `-66.6799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
