# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T12:37:28.596123+00:00`
- Price records: `672`
- Market context records: `7029`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11508`

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

- `market_context_high->fx_1h` score `-0.2857` n `216` status `ready` deltaP `1.619` edge `0.001` maxDD `-0.5407`
- `market_context_high->fx_4h` score `-0.5777` n `216` status `ready` deltaP `11.4838` edge `0.0076` maxDD `-1.6574`
- `market_context_high->crypto_alt_1h` score `-0.5797` n `216` status `ready` deltaP `1.4443` edge `0.0285` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6811` n `216` status `ready` deltaP `-1.7604` edge `0.0012` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6945` n `216` status `ready` deltaP `0.2966` edge `0.0001` maxDD `-2.2895`
- `market_context_high->unknown_24h` score `-0.9747` n `203` status `ready` deltaP `-7.2079` edge `0.3781` maxDD `-18.7342`
- `market_context_high->crypto_major_1h` score `-1.0924` n `216` status `ready` deltaP `2.9552` edge `0.0245` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.1913` n `216` status `ready` deltaP `-2.739` edge `0.0017` maxDD `-2.9508`
- `market_context_high->commodity_1h` score `-1.3276` n `216` status `ready` deltaP `-3.9754` edge `-0.0188` maxDD `-2.2263`
- `market_context_high->commodity_4h` score `-1.3976` n `216` status `ready` deltaP `-4.0876` edge `-0.0359` maxDD `-2.9494`
- `market_context_high->index_4h` score `-1.8758` n `216` status `ready` deltaP `6.5718` edge `-0.0144` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9795` n `216` status `ready` deltaP `5.3466` edge `0.0089` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.1199` n `216` status `ready` deltaP `-6.0242` edge `0.081` maxDD `-8.7331`
- `market_context_high->commodity_24h` score `-2.5851` n `203` status `ready` deltaP `-2.4819` edge `-0.068` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.7272` n `216` status `ready` deltaP `1.0501` edge `0.0219` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.9419` n `216` status `ready` deltaP `2.9247` edge `-0.0164` maxDD `-15.1941`
- `market_context_high->crypto_major_4h` score `-3.0759` n `216` status `ready` deltaP `2.1454` edge `0.0198` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.8201` n `203` status `ready` deltaP `-3.2909` edge `-0.0131` maxDD `-3.9973`
- `market_context_high->equity_4h` score `-7.2848` n `216` status `ready` deltaP `4.2288` edge `-0.0751` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.5804` n `203` status `ready` deltaP `-11.8603` edge `-0.0557` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
