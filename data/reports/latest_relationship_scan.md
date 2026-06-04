# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T01:07:21.074594+00:00`
- Price records: `672`
- Market context records: `2818`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.4162` n `142` status `ready` deltaP `3.1225` edge `0.227` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9146` n `142` status `ready` deltaP `6.338` edge `0.1393` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6967` n `142` status `ready` deltaP `11.2114` edge `0.2927` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3192` n `142` status `ready` deltaP `13.3009` edge `0.0364` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1725` n `142` status `ready` deltaP `5.229` edge `0.0526` maxDD `-3.1801`
- `market_context_high->crypto_alt_24h` score `0.1254` n `142` status `ready` deltaP `-0.5966` edge `0.4061` maxDD `-22.6673`
- `market_context_high->index_1h` score `-0.0587` n `142` status `ready` deltaP `4.4974` edge `0.0119` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.4975` n `142` status `ready` deltaP `-0.0885` edge `0.0035` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6288` n `142` status `ready` deltaP `-0.1328` edge `-0.0044` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6692` n `142` status `ready` deltaP `0.4322` edge `-0.0041` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7615` n `142` status `ready` deltaP `4.7968` edge `0.0464` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8871` n `142` status `ready` deltaP `-2.5997` edge `0.0267` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9264` n `142` status `ready` deltaP `3.7763` edge `0.043` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0614` n `142` status `ready` deltaP `2.2673` edge `0.0344` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1739` n `142` status `ready` deltaP `-4.0579` edge `0.0071` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.4252` n `142` status `ready` deltaP `1.3805` edge `0.0001` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.4762` n `142` status `ready` deltaP `0.8632` edge `-0.0307` maxDD `-2.5127`
- `market_context_high->fx_24h` score `-1.7085` n `142` status `ready` deltaP `-4.663` edge `-0.0241` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-2.0655` n `142` status `ready` deltaP `13.1183` edge `0.1745` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.3243` n `142` status `ready` deltaP `-0.7708` edge `-0.0378` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
