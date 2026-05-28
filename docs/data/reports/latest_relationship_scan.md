# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T03:37:17.258605+00:00`
- Price records: `672`
- Market context records: `2104`
- Flow alert records: `7951`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.7224` n `177` status `ready` deltaP `31.2301` edge `0.7998` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.5155` n `177` status `ready` deltaP `37.7678` edge `0.6775` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7964` n `177` status `ready` deltaP `23.6168` edge `0.4005` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1578` n `177` status `ready` deltaP `22.7298` edge `0.3044` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5325` n `177` status `ready` deltaP `18.9903` edge `0.1528` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.3343` n `176` status `ready` deltaP `11.8001` edge `0.2387` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.3321` n `176` status `ready` deltaP `23.1421` edge `0.5721` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `2.162` n `177` status `ready` deltaP `15.5223` edge `0.1753` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.9842` n `177` status `ready` deltaP `12.5283` edge `0.1932` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.5807` n `176` status `ready` deltaP `23.0202` edge `0.4681` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.1108` n `177` status `ready` deltaP `16.0026` edge `0.1835` maxDD `-9.4759`
- `market_context_high->equity_1h` score `0.822` n `177` status `ready` deltaP `10.9104` edge `0.0746` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.1586` n `177` status `ready` deltaP `5.2319` edge `0.0503` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1544` n `177` status `ready` deltaP `6.2265` edge `0.0304` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.1376` n `176` status `ready` deltaP `20.9028` edge `0.7307` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0757` n `176` status `ready` deltaP `14.8946` edge `0.0303` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.2281` n `177` status `ready` deltaP `6.7145` edge `0.0383` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8794` n `177` status `ready` deltaP `-1.7118` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-0.9297` n `176` status `ready` deltaP `10.0562` edge `0.2456` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.0587` n `177` status `ready` deltaP `-6.703` edge `-0.0029` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
