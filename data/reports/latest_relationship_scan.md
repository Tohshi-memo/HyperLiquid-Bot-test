# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T04:37:17.775883+00:00`
- Price records: `672`
- Market context records: `940`
- Flow alert records: `2633`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `22.1583` n `32` status `ready` deltaP `33.3333` edge `1.6243` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.1583` n `32` status `ready` deltaP `33.3333` edge `1.6243` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.2848` n `169` status `ready` deltaP `30.3747` edge `1.0213` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `13.375` n `32` status `ready` deltaP `6.5972` edge `1.0706` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.375` n `32` status `ready` deltaP `6.5972` edge `1.0706` maxDD `0.0`
- `risk_on_high->equity_24h` score `12.836` n `32` status `ready` deltaP `25.0` edge `0.903` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.836` n `32` status `ready` deltaP `25.0` edge `0.903` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.3198` n `169` status `ready` deltaP `6.5972` edge `0.566` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9509` n `32` status `ready` deltaP `26.7361` edge `0.151` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9509` n `32` status `ready` deltaP `26.7361` edge `0.151` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.3639` n `32` status `ready` deltaP `24.314` edge `0.1387` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3639` n `32` status `ready` deltaP `24.314` edge `0.1387` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.0473` n `32` status `ready` deltaP `4.3445` edge `0.2615` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.0473` n `32` status `ready` deltaP `4.3445` edge `0.2615` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8967` n `32` status `ready` deltaP `21.4939` edge `0.1353` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8967` n `32` status `ready` deltaP `21.4939` edge `0.1353` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1497` n `32` status `ready` deltaP `9.8323` edge `0.1224` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1497` n `32` status `ready` deltaP `9.8323` edge `0.1224` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `0.9727` n `32` status `ready` deltaP `-13.0208` edge `0.2861` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `0.9727` n `32` status `ready` deltaP `-13.0208` edge `0.2861` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
