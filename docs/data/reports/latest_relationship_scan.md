# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T12:37:16.280734+00:00`
- Price records: `672`
- Market context records: `1423`
- Flow alert records: `6011`
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

- `market_context_high->crypto_major_24h` score `11.804` n `154` status `ready` deltaP `27.3539` edge `0.9145` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.6489` n `154` status `ready` deltaP `28.7811` edge `0.9805` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.6178` n `154` status `ready` deltaP `11.8145` edge `1.0561` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7857` n `154` status `ready` deltaP `19.3813` edge `0.2949` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5431` n `154` status `ready` deltaP `12.5271` edge `0.3611` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8881` n `202` status `ready` deltaP `5.0849` edge `0.1231` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0599` n `154` status `ready` deltaP `9.3592` edge `0.0475` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1641` n `209` status `ready` deltaP `3.4245` edge `0.01` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2674` n `209` status `ready` deltaP `2.2856` edge `0.0225` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3988` n `209` status `ready` deltaP `2.3293` edge `-0.0022` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5929` n `209` status `ready` deltaP `0.5036` edge `0.023` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.6608` n `209` status `ready` deltaP `-0.7177` edge `0.0112` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.7336` n `202` status `ready` deltaP `-0.32` edge `0.0499` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.913` n `209` status `ready` deltaP `4.211` edge `-0.0131` maxDD `-6.2283`
- `market_context_high->crypto_major_1h` score `-1.2282` n `209` status `ready` deltaP `-2.1266` edge `-0.0076` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.2331` n `202` status `ready` deltaP `7.6491` edge `0.1782` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3046` n `202` status `ready` deltaP `5.29` edge `0.1269` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6128` n `202` status `ready` deltaP `-4.1159` edge `-0.0099` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5898` n `202` status `ready` deltaP `-10.0896` edge `-0.0101` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8483` n `202` status `ready` deltaP `4.149` edge `-0.0052` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
