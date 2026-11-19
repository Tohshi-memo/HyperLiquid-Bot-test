# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T17:07:27.706610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2626`

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

- `market_context_high->unknown_1h` score `12130.8855` n `107` status `ready` deltaP `0.5751` edge `1010.9231` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8051.2366` n `102` status `ready` deltaP `-0.3736` edge `670.9673` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.8776` n `88` status `ready` deltaP `44.9337` edge `1.8329` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.7536` n `88` status `ready` deltaP `23.7058` edge `1.4881` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `2.1878` n `102` status `ready` deltaP `4.4865` edge `0.4343` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.6059` n `102` status `ready` deltaP `5.4011` edge `0.3054` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.6125` n `102` status `ready` deltaP `19.1446` edge `0.0524` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.446` n `88` status `ready` deltaP `19.0656` edge `0.2189` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.2091` n `107` status `ready` deltaP `3.9104` edge `0.0136` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2286` n `107` status `ready` deltaP `4.5819` edge `0.0798` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3078` n `107` status `ready` deltaP `2.6764` edge `0.0039` maxDD `-1.2295`
- `market_context_high->index_4h` score `-1.1595` n `102` status `ready` deltaP `-2.463` edge `0.0021` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.1936` n `107` status `ready` deltaP `-2.2595` edge `0.0378` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.4716` n `107` status `ready` deltaP `5.4801` edge `0.0187` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6519` n `107` status `ready` deltaP `-11.9775` edge `-0.0021` maxDD `-0.4566`
- `market_context_high->fx_4h` score `-2.3922` n `102` status `ready` deltaP `-15.211` edge `-0.0037` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.5122` n `107` status `ready` deltaP `-10.521` edge `-0.0314` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1528` n `88` status `ready` deltaP `-23.769` edge `-0.0103` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.295` n `102` status `ready` deltaP `-30.7` edge `-0.1247` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-8.9388` n `102` status `ready` deltaP `-7.3231` edge `-0.0284` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
