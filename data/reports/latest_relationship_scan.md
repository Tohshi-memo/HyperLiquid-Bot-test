# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T05:17:04.014243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.1792` n `73` status `ready` deltaP `9.7078` edge `0.321` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.6567` n `73` status `ready` deltaP `12.6469` edge `0.1832` maxDD `-4.666`
- `market_context_high->metal_4h` score `0.5735` n `98` status `ready` deltaP `12.6555` edge `0.021` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.3407` n `98` status `ready` deltaP `8.7855` edge `0.0872` maxDD `-3.1677`
- `market_context_high->equity_1h` score `0.1916` n `103` status `ready` deltaP `4.6422` edge `0.0342` maxDD `-1.2469`
- `market_context_high->index_1h` score `0.1355` n `103` status `ready` deltaP `8.0897` edge `0.004` maxDD `-0.2444`
- `market_context_high->unknown_1h` score `0.1331` n `103` status `ready` deltaP `8.4704` edge `-0.0227` maxDD `-0.4807`
- `market_context_high->metal_24h` score `0.0503` n `73` status `ready` deltaP `4.8384` edge `0.0682` maxDD `-2.7013`
- `market_context_high->commodity_4h` score `0.0215` n `98` status `ready` deltaP `8.3282` edge `0.0313` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.2492` n `98` status `ready` deltaP `2.7096` edge `0.0007` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.2574` n `103` status `ready` deltaP `0.6351` edge `0.0026` maxDD `-0.52`
- `market_context_high->crypto_alt_4h` score `-0.4264` n `98` status `ready` deltaP `6.7322` edge `0.0757` maxDD `-7.02`
- `market_context_high->fx_1h` score `-0.4679` n `103` status `ready` deltaP `-0.7078` edge `0.0019` maxDD `-0.2273`
- `market_context_high->crypto_alt_1h` score `-0.5035` n `103` status `ready` deltaP `0.3357` edge `0.0149` maxDD `-2.5355`
- `market_context_high->equity_4h` score `-0.6717` n `98` status `ready` deltaP `-3.5497` edge `0.028` maxDD `-2.5696`
- `market_context_high->crypto_major_1h` score `-0.6797` n `103` status `ready` deltaP `-0.7122` edge `0.0062` maxDD `-3.0871`
- `market_context_high->commodity_1h` score `-0.7253` n `103` status `ready` deltaP `-4.818` edge `0.0004` maxDD `-1.5684`
- `market_context_high->index_4h` score `-0.7424` n `98` status `ready` deltaP `-1.0173` edge `0.0061` maxDD `-0.2281`
- `market_context_high->unknown_24h` score `-0.7799` n `73` status `ready` deltaP `7.4049` edge `-0.0765` maxDD `-0.6954`
- `market_context_high->index_24h` score `-1.5572` n `73` status `ready` deltaP `-0.254` edge `-0.0905` maxDD `-3.5962`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
