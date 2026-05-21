# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T11:22:20.218362+00:00`
- Price records: `672`
- Market context records: `1418`
- Flow alert records: `5996`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.876` n `154` status `ready` deltaP `27.3539` edge `0.9205` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.5181` n `154` status `ready` deltaP `28.7811` edge `0.9696` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.4439` n `154` status `ready` deltaP `10.9465` edge `1.0474` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7233` n `154` status `ready` deltaP `19.3813` edge `0.2897` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3055` n `154` status `ready` deltaP `12.5271` edge `0.3413` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8785` n `202` status `ready` deltaP `5.0849` edge `0.1223` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0431` n `154` status `ready` deltaP `9.3592` edge `0.0461` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0912` n `204` status `ready` deltaP `4.2005` edge `0.0109` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.171` n `204` status `ready` deltaP `2.5948` edge `0.0243` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2837` n `204` status `ready` deltaP `3.6779` edge `-0.0016` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.432` n `204` status `ready` deltaP `1.1595` edge `0.0281` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7265` n `204` status `ready` deltaP `-0.9393` edge `0.0072` maxDD `-2.252`
- `market_context_high->metal_1h` score `-0.8184` n `204` status `ready` deltaP `4.6319` edge `-0.009` maxDD `-5.8104`
- `market_context_high->index_4h` score `-0.8246` n `202` status `ready` deltaP `-1.0821` edge `0.0474` maxDD `-3.7119`
- `market_context_high->crypto_alt_4h` score `-1.3875` n `202` status `ready` deltaP `7.0393` edge `0.1694` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.4008` n `202` status `ready` deltaP `5.1376` edge `0.1199` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.5765` n `204` status `ready` deltaP `-1.3737` edge `-0.0032` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.6128` n `202` status `ready` deltaP `-4.1159` edge `-0.0099` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5859` n `202` status `ready` deltaP `-10.0896` edge `-0.0096` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8495` n `202` status `ready` deltaP `4.149` edge `-0.0053` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
