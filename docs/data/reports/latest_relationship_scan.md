# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T12:37:30.321498+00:00`
- Price records: `672`
- Market context records: `4828`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.8006` n `109` status `ready` deltaP `11.8058` edge `1.1131` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.1789` n `109` status `ready` deltaP `17.4326` edge `0.6864` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0517` n `102` status `ready` deltaP `15.5944` edge `0.2192` maxDD `-2.8416`
- `market_context_high->index_4h` score `0.8742` n `109` status `ready` deltaP `10.6973` edge `0.0482` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.8145` n `109` status `ready` deltaP `12.535` edge `0.159` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.45` n `109` status `ready` deltaP `15.4202` edge `0.0721` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.3083` n `109` status `ready` deltaP `6.8038` edge `0.0285` maxDD `-1.1869`
- `market_context_high->equity_1h` score `0.029` n `109` status `ready` deltaP `4.5775` edge `0.0348` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4539` n `109` status `ready` deltaP `2.7481` edge `0.0001` maxDD `-1.462`
- `market_context_high->index_1h` score `-0.4772` n `109` status `ready` deltaP `0.9463` edge `0.008` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.1204` n `109` status `ready` deltaP `-3.5873` edge `-0.0045` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-1.9538` n `109` status `ready` deltaP `4.8577` edge `-0.007` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.1548` n `109` status `ready` deltaP `2.8155` edge `-0.0375` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.1621` n `109` status `ready` deltaP `0.0632` edge `-0.0673` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.3524` n `102` status `ready` deltaP `-11.3256` edge `-0.0195` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-2.4643` n `102` status `ready` deltaP `17.1058` edge `0.0809` maxDD `-27.5371`
- `market_context_high->crypto_alt_4h` score `-3.3502` n `109` status `ready` deltaP `9.0177` edge `0.0231` maxDD `-36.0184`
- `market_context_high->index_24h` score `-3.9902` n `102` status `ready` deltaP `-3.0331` edge `-0.1005` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-6.6037` n `109` status `ready` deltaP `5.8025` edge `-0.1179` maxDD `-56.3925`
- `market_context_high->metal_4h` score `-8.0859` n `109` status `ready` deltaP `5.941` edge `-0.3211` maxDD `-56.0791`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
