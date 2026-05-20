# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T01:07:15.874870+00:00`
- Price records: `672`
- Market context records: `1273`
- Flow alert records: `5573`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `18.0073` n `128` status `ready` deltaP `41.5798` edge `1.3366` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.4663` n `128` status `ready` deltaP `6.0764` edge `0.9984` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.7615` n `128` status `ready` deltaP `25.434` edge `0.7622` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.9967` n `131` status `ready` deltaP `5.7171` edge `0.6666` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.1843` n `128` status `ready` deltaP `27.0833` edge `0.3601` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8831` n `128` status `ready` deltaP `25.1736` edge `0.5627` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.5584` n `131` status `ready` deltaP `17.8144` edge `0.2441` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3634` n `128` status `ready` deltaP `1.5625` edge `0.4595` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.8079` n `128` status `ready` deltaP `-12.3264` edge `0.381` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.8059` n `131` status `ready` deltaP `13.9942` edge `0.1255` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.96` n `131` status `ready` deltaP `18.5545` edge `0.0994` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.5217` n `143` status `ready` deltaP `12.242` edge `0.0229` maxDD `-2.2164`
- `market_context_high->index_1h` score `0.4965` n `143` status `ready` deltaP `8.2022` edge `0.0232` maxDD `-0.9206`
- `market_context_high->equity_1h` score `0.41` n `143` status `ready` deltaP `5.0072` edge `0.0435` maxDD `-1.7505`
- `market_context_high->crypto_major_4h` score `0.1488` n `131` status `ready` deltaP `8.1572` edge `0.1758` maxDD `-9.8882`
- `market_context_high->fx_24h` score `0.1024` n `128` status `ready` deltaP `3.7327` edge `0.0301` maxDD `-0.3831`
- `market_context_high->crypto_alt_1h` score `-0.3646` n `143` status `ready` deltaP `0.7517` edge `0.0353` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.3956` n `143` status `ready` deltaP `2.2508` edge `-0.0024` maxDD `-0.3124`
- `market_context_high->crypto_alt_4h` score `-0.464` n `131` status `ready` deltaP `9.0882` edge `0.1932` maxDD `-18.0619`
- `market_context_high->crypto_major_1h` score `-0.7559` n `143` status `ready` deltaP `0.3988` edge `0.0025` maxDD `-5.8323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
