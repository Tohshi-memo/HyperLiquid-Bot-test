# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T05:50:33.523947+00:00`
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

- `market_context_high->crypto_major_24h` score `2.7657` n `73` status `ready` deltaP `7.3147` edge `0.3025` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.7401` n `73` status `ready` deltaP `12.6469` edge `0.1939` maxDD `-4.666`
- `market_context_high->metal_4h` score `0.7089` n `96` status `ready` deltaP `13.9735` edge `0.0235` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.3693` n `96` status `ready` deltaP `9.1717` edge `0.0883` maxDD `-3.1677`
- `market_context_high->equity_1h` score `0.3354` n `101` status `ready` deltaP `5.9495` edge `0.0394` maxDD `-0.8855`
- `market_context_high->index_1h` score `0.3311` n `101` status `ready` deltaP `9.3585` edge `0.0049` maxDD `-0.1759`
- `market_context_high->unknown_1h` score `0.2708` n `101` status `ready` deltaP `8.8412` edge `-0.0137` maxDD `-0.4807`
- `market_context_high->commodity_4h` score `-0.1006` n `96` status `ready` deltaP `7.6728` edge `0.0255` maxDD `-2.4692`
- `market_context_high->metal_24h` score `-0.1797` n `73` status `ready` deltaP `4.8384` edge `0.0634` maxDD `-3.1839`
- `market_context_high->metal_1h` score `-0.1848` n `101` status `ready` deltaP `1.4851` edge `0.0051` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.189` n `96` status `ready` deltaP `7.9015` edge `0.0834` maxDD `-6.4908`
- `market_context_high->fx_4h` score `-0.2854` n `96` status `ready` deltaP `2.0579` edge `0.0004` maxDD `-0.3904`
- `market_context_high->unknown_24h` score `-0.3079` n `73` status `ready` deltaP `10.9946` edge `-0.0716` maxDD `-0.5221`
- `market_context_high->fx_1h` score `-0.3431` n `101` status `ready` deltaP `-1.4273` edge `0.0017` maxDD `-0.2273`
- `market_context_high->crypto_alt_1h` score `-0.424` n `101` status `ready` deltaP `1.3354` edge `0.0169` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.6087` n `96` status `ready` deltaP `0.2795` edge `0.0086` maxDD `-0.2281`
- `market_context_high->crypto_major_1h` score `-0.6619` n `101` status `ready` deltaP `-0.5529` edge `0.0072` maxDD `-3.07`
- `market_context_high->equity_4h` score `-0.7295` n `96` status `ready` deltaP `-2.2104` edge `0.0444` maxDD `-2.5696`
- `market_context_high->commodity_1h` score `-0.7704` n `101` status `ready` deltaP `-5.5952` edge `-0.0002` maxDD `-1.5684`
- `market_context_high->index_24h` score `-1.9098` n `73` status `ready` deltaP `-2.6471` edge `-0.1019` maxDD `-4.3575`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
