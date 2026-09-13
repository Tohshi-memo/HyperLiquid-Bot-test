# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T09:52:27.261173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12964`

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

- `market_context_high->unknown_24h` score `16664.6226` n `59` status `ready` deltaP `13.5068` edge `1388.6337` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `402.5955` n `82` status `ready` deltaP `-5.3113` edge `33.6272` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.7934` n `82` status `ready` deltaP `37.8512` edge `1.3775` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.756` n `82` status `ready` deltaP `32.4096` edge `1.3124` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `10.0363` n `59` status `ready` deltaP `22.3642` edge `0.77` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.7054` n `59` status `ready` deltaP `43.2495` edge `0.5131` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.3832` n `82` status `ready` deltaP `21.2363` edge `0.6517` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.5303` n `82` status `ready` deltaP `46.3877` edge `0.2526` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5852` n `82` status `ready` deltaP `24.2431` edge `0.2659` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1624` n `59` status `ready` deltaP `41.0345` edge `0.0733` maxDD `0.0`
- `market_context_high->index_24h` score `3.681` n `59` status `ready` deltaP `40.2075` edge `0.0808` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9162` n `59` status `ready` deltaP `13.5155` edge `0.1148` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.4325` n `65` status `ready` deltaP `10.7576` edge `0.1512` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4325` n `65` status `ready` deltaP `10.7576` edge `0.1512` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4031` n `82` status `ready` deltaP `12.3466` edge `0.0322` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.0964` n `65` status `ready` deltaP `4.5465` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0964` n `65` status `ready` deltaP `4.5465` edge `0.0033` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0731` n `65` status `ready` deltaP `3.7543` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0731` n `65` status `ready` deltaP `3.7543` edge `0.0019` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1572` n `138` status `ready` deltaP `2.9634` edge `-0.0012` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
