# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T15:07:19.797330+00:00`
- Price records: `672`
- Market context records: `1434`
- Flow alert records: `6041`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `12.0977` n `154` status `ready` deltaP `28.7811` edge `1.0179` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.9874` n `154` status `ready` deltaP `13.0298` edge `1.0788` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6864` n `154` status `ready` deltaP `27.3539` edge `0.9047` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0005` n `154` status `ready` deltaP `19.3813` edge `0.3128` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1791` n `154` status `ready` deltaP `12.5271` edge `0.4141` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0477` n `207` status `ready` deltaP `6.0306` edge `0.1301` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1284` n `154` status `ready` deltaP `9.7065` edge `0.0509` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2227` n `219` status `ready` deltaP `2.8567` edge `0.0089` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3349` n `219` status `ready` deltaP `1.6815` edge `0.0209` maxDD `-2.8014`
- `market_context_high->commodity_1h` score `-0.6648` n `219` status `ready` deltaP `-0.6774` edge `0.0106` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.6685` n `207` status `ready` deltaP `-0.151` edge `0.0542` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.7369` n `219` status `ready` deltaP `0.7225` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.7669` n `219` status `ready` deltaP `1.3589` edge `0.0294` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9208` n `219` status `ready` deltaP `3.7993` edge `-0.0098` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.1602` n `207` status `ready` deltaP `8.3061` edge `0.1799` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3485` n `207` status `ready` deltaP `4.8471` edge `0.1262` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6058` n `207` status `ready` deltaP `-4.104` edge `-0.0094` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.7004` n `219` status `ready` deltaP `-1.0814` edge `0.0012` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7874` n `207` status `ready` deltaP `4.8191` edge `0.0079` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.1044` n `207` status `ready` deltaP `-10.2856` edge `-0.0188` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
