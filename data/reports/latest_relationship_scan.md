# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T13:22:26.084349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10133`

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

- `risk_on_high->unknown_24h` score `116.2457` n `109` status `ready` deltaP `21.6537` edge `9.5628` maxDD `-0.6013`
- `risk_on_and_context->unknown_24h` score `116.2457` n `109` status `ready` deltaP `21.6537` edge `9.5628` maxDD `-0.6013`
- `risk_on_high->crypto_major_24h` score `6.6401` n `109` status `ready` deltaP `19.4014` edge `1.0352` maxDD `-39.8961`
- `risk_on_and_context->crypto_major_24h` score `6.6401` n `109` status `ready` deltaP `19.4014` edge `1.0352` maxDD `-39.8961`
- `market_context_high->equity_24h` score `1.7488` n `196` status `ready` deltaP `13.6657` edge `0.3374` maxDD `-13.2883`
- `risk_on_high->index_1h` score `-0.1491` n `140` status `ready` deltaP `4.3328` edge `-0.0033` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1491` n `140` status `ready` deltaP `4.3328` edge `-0.0033` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1859` n `140` status `ready` deltaP `7.2455` edge `-0.0009` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1859` n `140` status `ready` deltaP `7.2455` edge `-0.0009` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.4891` n `140` status `ready` deltaP `0.8897` edge `0.055` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.4891` n `140` status `ready` deltaP `0.8897` edge `0.055` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4936` n `140` status `ready` deltaP `5.6373` edge `-0.0134` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4936` n `140` status `ready` deltaP `5.6373` edge `-0.0134` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5454` n `140` status `ready` deltaP `0.7058` edge `0.0002` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5454` n `140` status `ready` deltaP `0.7058` edge `0.0002` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7699` n `250` status `ready` deltaP `0.3629` edge `-0.0016` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.9159` n `140` status `ready` deltaP `-0.3208` edge `0.0148` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.9159` n `140` status `ready` deltaP `-0.3208` edge `0.0148` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9896` n `250` status `ready` deltaP `3.0455` edge `-0.007` maxDD `-2.9947`
- `risk_on_high->equity_24h` score `-1.0101` n `109` status `ready` deltaP `3.1808` edge `0.167` maxDD `-12.7903`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
