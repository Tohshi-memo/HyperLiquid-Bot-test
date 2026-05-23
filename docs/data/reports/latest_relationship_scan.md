# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T03:07:16.788107+00:00`
- Price records: `672`
- Market context records: `1589`
- Flow alert records: `6489`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.79` n `182` status `ready` deltaP `29.3727` edge `1.0534` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.3625` n `182` status `ready` deltaP `27.171` edge `1.0507` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.6384` n `182` status `ready` deltaP `26.9135` edge `0.8203` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.7923` n `182` status `ready` deltaP `19.971` edge `0.4989` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.1832` n `182` status `ready` deltaP `21.9952` edge `0.3106` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.0815` n `199` status `ready` deltaP `9.2069` edge `0.1382` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2676` n `199` status `ready` deltaP `13.2545` edge `0.2779` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1028` n `199` status `ready` deltaP `9.2796` edge `0.2222` maxDD `-13.3376`
- `market_context_high->fx_24h` score `0.0054` n `182` status `ready` deltaP `9.7584` edge `0.0403` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3129` n `199` status `ready` deltaP `0.9674` edge `0.0558` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5635` n `199` status `ready` deltaP `0.7636` edge `0.0288` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5868` n `199` status `ready` deltaP `-1.2457` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6841` n `199` status `ready` deltaP `0.4747` edge `0.003` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7134` n `199` status `ready` deltaP `5.4472` edge `0.0058` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8224` n `199` status `ready` deltaP `-1.6948` edge `-0.002` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.835` n `199` status `ready` deltaP `0.0053` edge `0.0286` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0837` n `199` status `ready` deltaP `-1.696` edge `0.0299` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2862` n `199` status `ready` deltaP `10.516` edge `0.0919` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3791` n `199` status `ready` deltaP `-10.3973` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2588` n `199` status `ready` deltaP `-14.7001` edge `-0.1135` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
