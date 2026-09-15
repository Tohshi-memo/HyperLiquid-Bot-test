# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T12:07:29.381035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11210`

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

- `news_risk_high->unknown_4h` score `396.7256` n `78` status `ready` deltaP `-22.4554` edge `33.2995` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `22.1625` n `78` status `ready` deltaP `46.0337` edge `1.5791` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `22.0836` n `78` status `ready` deltaP `19.9653` edge `1.7072` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.0543` n `78` status `ready` deltaP `36.9525` edge `1.3219` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.181` n `78` status `ready` deltaP `48.4642` edge `1.12` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5936` n `78` status `ready` deltaP `61.071` edge `0.3266` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.536` n `78` status `ready` deltaP `38.4882` edge `0.3335` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9539` n `52` status `ready` deltaP `37.6736` edge `0.245` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9539` n `52` status `ready` deltaP `37.6736` edge `0.245` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6569` n `137` status `ready` deltaP `30.3743` edge `0.2381` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.5653` n `52` status `ready` deltaP `41.8269` edge `0.0225` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.5653` n `52` status `ready` deltaP `41.8269` edge `0.0225` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.1683` n `137` status `ready` deltaP `38.6405` edge `0.028` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8454` n `52` status `ready` deltaP `24.3082` edge `0.0267` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8454` n `52` status `ready` deltaP `24.3082` edge `0.0267` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7451` n `149` status `ready` deltaP `20.8105` edge `0.0485` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8689` n `149` status `ready` deltaP `13.666` edge `0.019` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7201` n `78` status `ready` deltaP `17.5735` edge `0.038` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2456` n `52` status `ready` deltaP `6.7481` edge `0.0107` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2456` n `52` status `ready` deltaP `6.7481` edge `0.0107` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
