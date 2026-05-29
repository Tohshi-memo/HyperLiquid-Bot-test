# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T14:22:22.383767+00:00`
- Price records: `672`
- Market context records: `2252`
- Flow alert records: `8376`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `23.8926` n `43` status `ready` deltaP `54.3766` edge `1.6874` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.1695` n `43` status `ready` deltaP `44.0286` edge `1.0979` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.7138` n `43` status `ready` deltaP `35.0008` edge `1.1076` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.3913` n `43` status `ready` deltaP `24.9757` edge `1.0075` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `10.1469` n `115` status `ready` deltaP `31.2349` edge `0.6785` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.7104` n `43` status `ready` deltaP `35.2794` edge `0.5966` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `9.2161` n `135` status `ready` deltaP `28.8211` edge `0.8027` maxDD `-13.1468`
- `market_context_high->crypto_major_4h` score `8.6165` n `135` status `ready` deltaP `34.2039` edge `0.6426` maxDD `-8.54`
- `market_context_high->crypto_major_24h` score `6.9827` n `115` status `ready` deltaP `18.6866` edge `1.1599` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3123` n `135` status `ready` deltaP `20.5442` edge `0.3667` maxDD `-1.8773`
- `market_context_high->index_4h` score `3.9968` n `135` status `ready` deltaP `30.6357` edge `0.1662` maxDD `-0.3228`
- `news_risk_high->index_24h` score `3.8788` n `43` status `ready` deltaP `13.0976` edge `0.2778` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8032` n `43` status `ready` deltaP `32.4624` edge `0.3383` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6651` n `43` status `ready` deltaP `37.2295` edge `0.0757` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4891` n `115` status `ready` deltaP `14.8974` edge `0.2432` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.3527` n `115` status `ready` deltaP `22.5438` edge `0.2818` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9399` n `43` status `ready` deltaP `1.8572` edge `0.3143` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.6615` n `135` status `ready` deltaP `20.0486` edge `0.2147` maxDD `-4.7922`
- `news_risk_high->fx_4h` score `2.0819` n `43` status `ready` deltaP `26.5173` edge `0.0151` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9493` n `147` status `ready` deltaP `13.4832` edge `0.1893` maxDD `-6.0065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
