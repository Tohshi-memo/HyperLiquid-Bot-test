# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T03:37:30.036415+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12585`

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

- `market_context_high->unknown_24h` score `16604.3135` n `59` status `ready` deltaP `12.5824` edge `1383.6141` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `380.2791` n `82` status `ready` deltaP `-4.8014` edge `31.7641` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.9945` n `82` status `ready` deltaP `32.406` edge `1.3323` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9548` n `82` status `ready` deltaP `38.8042` edge `1.3846` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.6798` n `59` status `ready` deltaP `47.7431` edge `0.5717` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.096` n `59` status `ready` deltaP `22.3606` edge `0.775` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.4227` n `82` status `ready` deltaP `17.2553` edge `0.5982` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1904` n `82` status `ready` deltaP `43.1741` edge `0.2457` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8737` n `82` status `ready` deltaP `26.8293` edge `0.2727` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2378` n `59` status `ready` deltaP `42.1875` edge `0.0719` maxDD `0.0`
- `market_context_high->index_24h` score `4.069` n `59` status `ready` deltaP `43.7736` edge `0.0865` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.2769` n `59` status `ready` deltaP `7.6271` edge `0.1044` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.2173` n `82` status `ready` deltaP `9.2988` edge `0.0287` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.1007` n `53` status `ready` deltaP `7.0611` edge `0.1333` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1007` n `53` status `ready` deltaP `7.0611` edge `0.1333` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.0769` n `62` status `ready` deltaP `2.3952` edge `0.0032` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `-0.0769` n `62` status `ready` deltaP `2.3952` edge `0.0032` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.1367` n `120` status `ready` deltaP `2.3952` edge `-0.0019` maxDD `-0.5274`
- `risk_on_high->metal_1h` score `-0.165` n `62` status `ready` deltaP `2.6946` edge `0.0013` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.165` n `62` status `ready` deltaP `2.6946` edge `0.0013` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
