# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T00:07:21.955799+00:00`
- Price records: `672`
- Market context records: `3126`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7027`

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

- `market_context_high->commodity_24h` score `14.3732` n `103` status `ready` deltaP `47.3385` edge `0.925` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.8958` n `103` status `ready` deltaP `20.8671` edge `0.901` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.2467` n `103` status `ready` deltaP `10.2026` edge `2.3192` maxDD `-66.9603`
- `market_context_high->index_24h` score `6.5702` n `103` status `ready` deltaP `31.9782` edge `0.8846` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.566` n `103` status `ready` deltaP `11.3976` edge `1.3205` maxDD `-52.2217`
- `market_context_high->commodity_4h` score `3.0468` n `129` status `ready` deltaP `19.2747` edge `0.1712` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0192` n `141` status `ready` deltaP `2.6638` edge `0.0261` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4198` n `141` status `ready` deltaP `4.9879` edge `0.0192` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5066` n `103` status `ready` deltaP `4.792` edge `-0.0014` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.6352` n `141` status `ready` deltaP `4.4284` edge `0.102` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.9248` n `141` status `ready` deltaP `1.9227` edge `0.0172` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1728` n `141` status `ready` deltaP `-11.4739` edge `-0.0057` maxDD `-0.7863`
- `market_context_high->crypto_major_1h` score `-1.1971` n `141` status `ready` deltaP `1.3069` edge `0.0641` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.2566` n `129` status `ready` deltaP `11.6846` edge `0.0519` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4657` n `129` status `ready` deltaP `-14.2147` edge `-0.008` maxDD `-1.1453`
- `market_context_high->metal_1h` score `-2.153` n `141` status `ready` deltaP `-5.2724` edge `-0.0049` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2277` n `129` status `ready` deltaP `2.6517` edge `0.0189` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0911` n `141` status `ready` deltaP `1.5374` edge `-0.0652` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.4135` n `129` status `ready` deltaP `15.3526` edge `0.2645` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.6309` n `129` status `ready` deltaP `9.0541` edge `0.0047` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
