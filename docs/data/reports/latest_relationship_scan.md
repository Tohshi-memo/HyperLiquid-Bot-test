# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T09:07:20.413486+00:00`
- Price records: `672`
- Market context records: `2028`
- Flow alert records: `7728`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.8835` n `205` status `ready` deltaP `30.7927` edge `0.588` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3694` n `205` status `ready` deltaP `24.5427` edge `0.6483` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8761` n `205` status `ready` deltaP `18.689` edge `0.44` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0275` n `205` status `ready` deltaP `17.2561` edge `0.2467` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5356` n `205` status `ready` deltaP `12.4777` edge `0.1434` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4414` n `205` status `ready` deltaP `12.9269` edge `0.1023` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2461` n `205` status `ready` deltaP `10.0825` edge `0.148` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.8067` n `197` status `ready` deltaP `16.6148` edge `0.4885` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.3806` n `197` status `ready` deltaP `15.6239` edge `0.4174` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.2068` n `205` status `ready` deltaP `6.9104` edge `0.05` maxDD `-2.6402`
- `market_context_high->index_24h` score `0.191` n `197` status `ready` deltaP `3.9984` edge `0.1121` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `-0.0094` n `205` status `ready` deltaP `3.5965` edge `0.0472` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.3313` n `205` status `ready` deltaP `2.2543` edge `0.0164` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.3818` n `197` status `ready` deltaP `11.5995` edge `0.0236` maxDD `-2.2866`
- `market_context_high->fx_1h` score `-0.8649` n `205` status `ready` deltaP `-1.4415` edge `0.0003` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.897` n `205` status `ready` deltaP `3.6585` edge `0.0196` maxDD `-5.166`
- `market_context_high->metal_24h` score `-1.1626` n `197` status `ready` deltaP `10.5225` edge `0.1462` maxDD `-18.3918`
- `market_context_high->metal_4h` score `-1.232` n `205` status `ready` deltaP `8.4147` edge `0.1035` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.6353` n `205` status `ready` deltaP `-6.8903` edge `-0.0022` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8029` n `205` status `ready` deltaP `3.2043` edge `0.0033` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
