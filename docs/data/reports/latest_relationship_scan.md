# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T16:37:30.027013+00:00`
- Price records: `672`
- Market context records: `7159`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.2604` n `156` status `ready` deltaP `11.8355` edge `0.0128` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3216` n `166` status `ready` deltaP `2.709` edge `0.0017` maxDD `-0.3912`
- `market_context_high->unknown_1h` score `-0.6049` n `166` status `ready` deltaP `-1.9822` edge `0.027` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6392` n `166` status `ready` deltaP `-0.4599` edge `0.025` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.6735` n `166` status `ready` deltaP `-1.1796` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->crypto_major_1h` score `-0.677` n `166` status `ready` deltaP `3.0084` edge `0.0342` maxDD `-7.6171`
- `market_context_high->index_1h` score `-0.7435` n `166` status `ready` deltaP `1.322` edge `-0.0043` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.8439` n `166` status `ready` deltaP `-7.1153` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.9693` n `156` status `ready` deltaP `-5.9998` edge `0.0135` maxDD `-6.0783`
- `market_context_high->commodity_4h` score `-2.0979` n `156` status `ready` deltaP `-4.964` edge `-0.0382` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9349` n `156` status `ready` deltaP `-10.3971` edge `-0.0121` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.6113` n `166` status `ready` deltaP `-1.2445` edge `-0.0403` maxDD `-15.5212`
- `market_context_high->index_4h` score `-3.9424` n `156` status `ready` deltaP `-2.3296` edge `-0.0431` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4976` n `133` status `ready` deltaP `-13.4581` edge `-0.1542` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.8807` n `133` status `ready` deltaP `-14.8366` edge `-0.0251` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.9394` n `156` status `ready` deltaP `2.3139` edge `0.0083` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5708` n `156` status `ready` deltaP `-3.5217` edge `-0.0311` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.0956` n `133` status `ready` deltaP `-32.7029` edge `-0.1086` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.755` n `133` status `ready` deltaP `-32.1232` edge `-0.1973` maxDD `-40.7836`
- `market_context_high->equity_4h` score `-14.7684` n `156` status `ready` deltaP `-4.2253` edge `-0.2171` maxDD `-66.5013`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
