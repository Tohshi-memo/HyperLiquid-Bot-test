# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T17:22:27.689907+00:00`
- Price records: `672`
- Market context records: `6837`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `0.9615` n `176` status `ready` deltaP `-1.5467` edge `0.5088` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0854` n `176` status `ready` deltaP `9.1856` edge `0.1327` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2836` n `215` status `ready` deltaP `1.6119` edge `0.0014` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.5176` n `215` status `ready` deltaP `4.4131` edge `0.0176` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.522` n `215` status `ready` deltaP `2.4029` edge `0.0169` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8921` n `215` status `ready` deltaP `-2.7239` edge `-0.0051` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0279` n `215` status `ready` deltaP `-6.5249` edge `-0.0115` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-1.0776` n `215` status `ready` deltaP `-2.3444` edge `-0.0057` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-1.1073` n `203` status `ready` deltaP `9.1824` edge `0.0032` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.6114` n `215` status `ready` deltaP `-3.237` edge `-0.0226` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0002` n `215` status `ready` deltaP `-0.1525` edge `-0.0374` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.1906` n `203` status `ready` deltaP `0.787` edge `-0.0345` maxDD `-10.7939`
- `market_context_high->commodity_4h` score `-2.3532` n `203` status `ready` deltaP `-4.7729` edge `-0.0153` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7185` n `203` status `ready` deltaP `-3.3912` edge `-0.0276` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.8762` n `203` status `ready` deltaP `0.5061` edge `-0.0394` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0662` n `203` status `ready` deltaP `0.5174` edge `-0.0382` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2381` n `203` status `ready` deltaP `-9.9123` edge `0.0328` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4576` n `176` status `ready` deltaP `-9.7853` edge `-0.0026` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5349` n `203` status `ready` deltaP `-1.4771` edge `-0.2143` maxDD `-52.3497`
- `market_context_high->metal_24h` score `-9.2942` n `176` status `ready` deltaP `-19.192` edge `-0.2151` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
