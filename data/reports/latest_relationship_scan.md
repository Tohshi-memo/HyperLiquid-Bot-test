# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T00:07:28.002493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6775`

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

- `market_context_high->unknown_24h` score `3983.3149` n `82` status `ready` deltaP `-9.7815` edge `332.0511` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `141.4317` n `82` status `ready` deltaP `0.6097` edge `11.7952` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `76.4584` n `108` status `ready` deltaP `-5.1951` edge `6.4348` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `15.8207` n `90` status `ready` deltaP `37.0486` edge `1.1549` maxDD `-4.3468`
- `market_context_high->equity_24h` score `10.7086` n `82` status `ready` deltaP `21.0747` edge `1.0276` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.596` n `108` status `ready` deltaP `21.3415` edge `0.4627` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.0236` n `82` status `ready` deltaP `44.0465` edge `0.1433` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.0853` n `82` status `ready` deltaP `21.6464` edge `0.0712` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.3256` n `82` status `ready` deltaP `16.4634` edge `0.0432` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.9332` n `108` status `ready` deltaP `9.4755` edge `0.11` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7592` n `82` status `ready` deltaP `10.9318` edge `0.0194` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.7413` n `82` status `ready` deltaP `14.7866` edge `0.0023` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.5639` n `82` status `ready` deltaP `13.6082` edge `0.0` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.3763` n `82` status `ready` deltaP `1.8183` edge `0.1068` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.3` n `82` status `ready` deltaP `-1.9817` edge `0.191` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.0397` n `82` status `ready` deltaP `4.407` edge `0.0683` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3831` n `82` status `ready` deltaP `0.4053` edge `0.0168` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4309` n `82` status `ready` deltaP `-0.1497` edge `0.0016` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.7162` n `108` status `ready` deltaP `3.554` edge `-0.0034` maxDD `-1.3981`
- `market_context_high->metal_24h` score `-0.8371` n `82` status `ready` deltaP `2.9217` edge `0.1379` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
