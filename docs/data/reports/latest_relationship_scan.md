# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T01:52:21.709026+00:00`
- Price records: `672`
- Market context records: `1997`
- Flow alert records: `7639`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.5195` n `222` status `ready` deltaP `29.9179` edge `0.5635` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `7.9416` n `222` status `ready` deltaP `23.7846` edge `0.6177` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `4.8913` n `222` status `ready` deltaP `16.8754` edge `0.3791` maxDD `-3.3862`
- `market_context_high->equity_4h` score `2.5342` n `222` status `ready` deltaP `15.3799` edge `0.2181` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.4297` n `187` status `ready` deltaP `15.8276` edge `0.629` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.6766` n `187` status `ready` deltaP `16.6682` edge `0.2712` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.2224` n `222` status `ready` deltaP `10.6625` edge `0.1294` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.1602` n `187` status `ready` deltaP `14.6738` edge `0.4887` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.9631` n `222` status `ready` deltaP `8.7191` edge `0.1335` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.8414` n `222` status `ready` deltaP `8.9211` edge `0.079` maxDD `-1.8022`
- `market_context_high->fx_24h` score `0.6443` n `187` status `ready` deltaP `15.3798` edge `0.0286` maxDD `-1.1952`
- `market_context_high->crypto_major_24h` score `0.5488` n `187` status `ready` deltaP `20.3272` edge `0.7688` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.1349` n `187` status `ready` deltaP `2.9668` edge `0.1143` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1056` n `222` status `ready` deltaP `4.5356` edge `0.0398` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.6038` n `222` status `ready` deltaP `-2.0985` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6391` n `222` status `ready` deltaP `-0.4234` edge `0.0086` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.9284` n `222` status `ready` deltaP `2.2644` edge `-0.0205` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.9449` n `222` status `ready` deltaP `1.8059` edge `0.0004` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.1383` n `222` status `ready` deltaP `-8.2042` edge `-0.0031` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8626` n `222` status `ready` deltaP `2.2509` edge `0.002` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
