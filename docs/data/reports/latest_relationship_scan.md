# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T02:37:29.882228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7608`

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

- `market_context_high->unknown_4h` score `54.1893` n `95` status `ready` deltaP `0.8408` edge `4.5437` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.5811` n `107` status `ready` deltaP `2.1574` edge `1.4996` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.5077` n `48` status `ready` deltaP `19.7916` edge `0.0846` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.2275` n `95` status `ready` deltaP `5.6884` edge `0.0456` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.357` n `107` status `ready` deltaP `1.5474` edge `0.01` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3746` n `107` status `ready` deltaP `-2.1826` edge `0.002` maxDD `-0.1712`
- `market_context_high->index_1h` score `-0.623` n `107` status `ready` deltaP `-1.2116` edge `-0.0066` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.7162` n `95` status `ready` deltaP `-5.398` edge `0.0042` maxDD `-0.4691`
- `market_context_high->metal_1h` score `-0.8587` n `107` status `ready` deltaP `1.9685` edge `-0.0054` maxDD `-1.6761`
- `market_context_high->fx_24h` score `-1.0219` n `48` status `ready` deltaP `-1.0416` edge `0.0` maxDD `-1.2569`
- `market_context_high->crypto_major_24h` score `-1.0286` n `48` status `ready` deltaP `6.9445` edge `0.0279` maxDD `-11.8186`
- `market_context_high->crypto_major_1h` score `-1.1589` n `107` status `ready` deltaP `4.6141` edge `-0.0205` maxDD `-9.374`
- `market_context_high->equity_1h` score `-2.5136` n `107` status `ready` deltaP `-0.3498` edge `-0.0912` maxDD `-12.2983`
- `market_context_high->metal_4h` score `-2.7812` n `95` status `ready` deltaP `-3.8013` edge `-0.0296` maxDD `-5.8128`
- `market_context_high->metal_24h` score `-2.9203` n `48` status `ready` deltaP `-8.8541` edge `-0.0037` maxDD `-6.7837`
- `market_context_high->crypto_alt_1h` score `-3.1163` n `107` status `ready` deltaP `-0.277` edge `-0.0577` maxDD `-13.0114`
- `market_context_high->crypto_alt_24h` score `-3.1972` n `48` status `ready` deltaP `10.0694` edge `0.007` maxDD `-33.7222`
- `market_context_high->index_4h` score `-4.3094` n `95` status `ready` deltaP `-17.1726` edge `-0.0495` maxDD `-4.9437`
- `market_context_high->index_24h` score `-7.2592` n `48` status `ready` deltaP `-36.4584` edge `-0.1845` maxDD `-6.19`
- `market_context_high->crypto_major_4h` score `-11.4658` n `95` status `ready` deltaP `-17.3251` edge `-0.2641` maxDD `-39.4037`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
