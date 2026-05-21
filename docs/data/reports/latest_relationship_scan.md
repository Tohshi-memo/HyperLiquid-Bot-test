# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T10:22:20.879953+00:00`
- Price records: `672`
- Market context records: `1414`
- Flow alert records: `5984`
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

- `market_context_high->crypto_major_24h` score `11.93` n `154` status `ready` deltaP `27.3539` edge `0.925` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.3789` n `154` status `ready` deltaP `28.7811` edge `0.958` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2948` n `154` status `ready` deltaP `10.252` edge `1.0396` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.6681` n `154` status `ready` deltaP `19.3813` edge `0.2851` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.1171` n `154` status `ready` deltaP `12.5271` edge `0.3256` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9038` n `202` status `ready` deltaP `5.2373` edge `0.1234` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0371` n `154` status `ready` deltaP `9.3592` edge `0.0456` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0783` n `202` status `ready` deltaP `4.2568` edge `0.0116` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1434` n `202` status `ready` deltaP `2.8057` edge `0.0252` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2967` n `202` status `ready` deltaP `3.5454` edge `-0.0018` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5855` n `202` status `ready` deltaP `1.2539` edge `0.0299` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.7365` n `202` status `ready` deltaP `4.7652` edge `-0.0087` maxDD `-5.0663`
- `market_context_high->commodity_1h` score `-0.7786` n `202` status `ready` deltaP `-1.1398` edge `0.0042` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.8621` n `202` status `ready` deltaP `-1.387` edge `0.0463` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.379` n `202` status `ready` deltaP `5.29` edge `0.1207` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.4405` n `202` status `ready` deltaP `-1.3132` edge `-0.0006` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4431` n `202` status `ready` deltaP `6.7344` edge `0.1668` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.5714` n `202` status `ready` deltaP `-3.6585` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5937` n `202` status `ready` deltaP `-10.0896` edge `-0.0106` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8097` n `202` status `ready` deltaP `4.3015` edge `-0.003` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
