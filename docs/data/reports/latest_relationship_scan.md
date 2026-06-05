# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T16:52:23.937544+00:00`
- Price records: `672`
- Market context records: `2987`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `16.2914` n `98` status `ready` deltaP `4.769` edge `1.7175` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.9831` n `98` status `ready` deltaP `41.5994` edge `0.7323` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.2172` n `98` status `ready` deltaP `17.1804` edge `0.8667` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.187` n `98` status `ready` deltaP `15.5684` edge `0.6955` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.5862` n `98` status `ready` deltaP `15.6994` edge `0.3756` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.3371` n `99` status `ready` deltaP `14.9144` edge `0.2176` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.3525` n `99` status `ready` deltaP `19.6015` edge `0.1442` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.3188` n `99` status `ready` deltaP `17.1825` edge `0.1434` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.938` n `99` status `ready` deltaP `24.4026` edge `0.4137` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3426` n `102` status `ready` deltaP `6.8627` edge `0.0297` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.073` n `102` status `ready` deltaP `5.3804` edge `0.0436` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2329` n `102` status `ready` deltaP `-0.5166` edge `0.017` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4912` n `102` status `ready` deltaP `-1.6467` edge `0.0013` maxDD `-0.1672`
- `market_context_high->crypto_alt_1h` score `-0.956` n `102` status `ready` deltaP `8.1425` edge `0.0413` maxDD `-11.6869`
- `market_context_high->crypto_major_1h` score `-1.0327` n `102` status `ready` deltaP `5.5536` edge `0.0137` maxDD `-11.9831`
- `market_context_high->fx_4h` score `-1.0367` n `99` status `ready` deltaP `-8.5859` edge `0.0022` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.0478` n `102` status `ready` deltaP `-2.2896` edge `-0.0056` maxDD `-5.4112`
- `market_context_high->unknown_4h` score `-1.1356` n `99` status `ready` deltaP `-0.3141` edge `0.0128` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.6982` n `102` status `ready` deltaP `1.9755` edge `-0.0816` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.9036` n `99` status `ready` deltaP `9.6128` edge `0.2044` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
