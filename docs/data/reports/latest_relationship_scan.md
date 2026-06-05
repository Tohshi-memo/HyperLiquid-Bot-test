# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T03:37:25.175153+00:00`
- Price records: `672`
- Market context records: `2932`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `15.2455` n `142` status `ready` deltaP `14.8548` edge `1.5631` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.3994` n `142` status `ready` deltaP `17.0676` edge `0.7032` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.4122` n `142` status `ready` deltaP `14.9281` edge `0.4813` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.5745` n `142` status `ready` deltaP `12.8423` edge `0.227` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8101` n `142` status `ready` deltaP `15.378` edge `0.3577` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8994` n `142` status `ready` deltaP `8.8221` edge `0.1541` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.745` n `142` status `ready` deltaP `15.1301` edge `0.0788` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.2337` n `142` status `ready` deltaP `15.8622` edge `0.3478` maxDD `-28.7261`
- `market_context_high->unknown_4h` score `0.0125` n `142` status `ready` deltaP `3.7465` edge `0.0814` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0155` n `143` status `ready` deltaP `4.3979` edge `0.0181` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.386` n `143` status `ready` deltaP `0.9035` edge `0.0451` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4602` n `143` status `ready` deltaP `5.7452` edge `0.0787` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.4979` n `143` status `ready` deltaP `3.2987` edge `0.0096` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.571` n `143` status `ready` deltaP `-0.9463` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.6273` n `143` status `ready` deltaP `5.7923` edge `0.0679` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6403` n `143` status `ready` deltaP `0.3967` edge `0.004` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6797` n `143` status `ready` deltaP `-1.5451` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-1.0176` n `142` status `ready` deltaP `-1.9237` edge `0.0059` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2907` n `142` status `ready` deltaP `1.6854` edge `0.0153` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2984` n `142` status `ready` deltaP `-1.7116` edge `-0.0096` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
