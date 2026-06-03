# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T08:07:24.499231+00:00`
- Price records: `672`
- Market context records: `2745`
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

- `market_context_high->unknown_24h` score `7.5912` n `115` status `ready` deltaP `15.4378` edge `0.5625` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `6.2555` n `115` status `ready` deltaP `14.0021` edge `1.058` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `1.0281` n `143` status `ready` deltaP `6.7063` edge `0.1463` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1374` n `143` status `ready` deltaP `10.7038` edge `0.0304` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0992` n `143` status `ready` deltaP `3.4976` edge `0.0415` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.176` n `143` status `ready` deltaP `2.9009` edge `0.0075` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5219` n `143` status `ready` deltaP `-0.3475` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6305` n `143` status `ready` deltaP `5.9954` edge `0.0552` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.655` n `143` status `ready` deltaP `-0.3967` edge `-0.006` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7419` n `143` status `ready` deltaP `-0.9506` edge `-0.0042` maxDD `-3.0996`
- `market_context_high->crypto_alt_4h` score `-0.8908` n `143` status `ready` deltaP `15.9059` edge `0.2538` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.9643` n `143` status `ready` deltaP `3.4976` edge `0.04` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.1467` n `143` status `ready` deltaP `-3.7929` edge `0.0076` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2383` n `115` status `ready` deltaP `-0.0453` edge `-0.0157` maxDD `-0.6418`
- `market_context_high->crypto_major_24h` score `-1.2768` n `115` status `ready` deltaP `4.606` edge `0.7502` maxDD `-57.9015`
- `market_context_high->equity_1h` score `-1.2843` n `143` status `ready` deltaP `-4.8343` edge `0.0085` maxDD `-2.6634`
- `market_context_high->commodity_24h` score `-1.4367` n `115` status `ready` deltaP `3.9281` edge `0.099` maxDD `-12.4171`
- `market_context_high->commodity_4h` score `-1.5897` n `143` status `ready` deltaP `-0.1631` edge `-0.0107` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0267` n `143` status `ready` deltaP `-1.2493` edge `-0.0226` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3839` n `143` status `ready` deltaP `-2.1864` edge `-0.036` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
