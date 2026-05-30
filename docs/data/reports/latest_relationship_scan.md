# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T08:52:22.018091+00:00`
- Price records: `672`
- Market context records: `2332`
- Flow alert records: `8604`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `20.7937` n `43` status `ready` deltaP `50.0363` edge `1.4581` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.5256` n `43` status `ready` deltaP `43.3341` edge `1.1322` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.2459` n `43` status `ready` deltaP `29.7925` edge `1.02` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.529` n `43` status `ready` deltaP `19.7674` edge `0.8037` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.2618` n `129` status `ready` deltaP `17.4419` edge `1.0448` maxDD `-25.1408`
- `market_context_high->unknown_24h` score `7.3234` n `129` status `ready` deltaP `24.3662` edge `0.489` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.1462` n `43` status `ready` deltaP `27.4669` edge `0.435` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.719` n `159` status `ready` deltaP `22.9368` edge `0.6749` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.6988` n `159` status `ready` deltaP `26.5397` edge `0.5623` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.3639` n `159` status `ready` deltaP `21.6981` edge `0.3633` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.348` n `43` status `ready` deltaP `11.8823` edge `0.325` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0065` n `43` status `ready` deltaP `33.9868` edge `0.3542` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4324` n `129` status `ready` deltaP `14.983` edge `0.2379` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4234` n `43` status `ready` deltaP `36.1879` edge `0.0625` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1476` n `43` status `ready` deltaP `27.2794` edge `0.0155` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.038` n `159` status `ready` deltaP `20.0423` edge `0.1188` maxDD `-2.2732`
- `market_context_high->equity_24h` score `1.946` n `129` status `ready` deltaP `18.9398` edge `0.1886` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `1.858` n `159` status `ready` deltaP `12.025` edge `0.1934` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.611` n `159` status `ready` deltaP `12.1747` edge `0.1725` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.5803` n `43` status `ready` deltaP `4.2878` edge `0.1848` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
