# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T23:07:18.163282+00:00`
- Price records: `672`
- Market context records: `1366`
- Flow alert records: `5845`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.1876` n `139` status `ready` deltaP `31.9432` edge `0.9992` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.5618` n `139` status `ready` deltaP `13.6103` edge `1.1228` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.2509` n `139` status `ready` deltaP `28.5709` edge `0.8654` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1384` n `139` status `ready` deltaP `22.7406` edge `0.3019` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7011` n `139` status `ready` deltaP `15.7461` edge `0.3528` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.9945` n `164` status `ready` deltaP `10.3658` edge `0.1676` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.8757` n `139` status `ready` deltaP `11.8742` edge `0.0509` maxDD `-0.9002`
- `market_context_high->metal_4h` score `0.0284` n `164` status `ready` deltaP `11.8902` edge `0.0662` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0614` n `176` status `ready` deltaP `3.9059` edge `0.0126` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1496` n `176` status `ready` deltaP `1.9598` edge `0.0236` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.152` n `164` status `ready` deltaP `2.8963` edge `0.0701` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.3183` n `176` status `ready` deltaP `1.463` edge `-0.004` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4596` n `176` status `ready` deltaP `5.7669` edge `0.0015` maxDD `-3.5762`
- `market_context_high->crypto_alt_1h` score `-0.5863` n `176` status `ready` deltaP `-0.7519` edge `0.0169` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.6935` n `176` status `ready` deltaP `-0.2109` edge `0.0051` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.0832` n `176` status `ready` deltaP `-2.9328` edge `-0.0128` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4595` n `164` status `ready` deltaP `7.7743` edge `0.1585` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.9791` n `164` status `ready` deltaP `2.4391` edge `0.0897` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-2.0653` n `164` status `ready` deltaP `-9.2988` edge `-0.0151` maxDD `-1.2678`
- `market_context_high->commodity_24h` score `-2.2779` n `139` status `ready` deltaP `-11.0462` edge `0.2658` maxDD `-25.5589`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
