# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T16:37:34.296665+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11967`

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

- `risk_on_high->crypto_alt_24h` score `19.208` n `91` status `ready` deltaP `36.1722` edge `1.3825` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.208` n `91` status `ready` deltaP `36.1722` edge `1.3825` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.6193` n `201` status `ready` deltaP `27.7364` edge `1.1161` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.197` n `91` status `ready` deltaP `43.3178` edge `0.5148` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.197` n `91` status `ready` deltaP `43.3178` edge `0.5148` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.8205` n `91` status `ready` deltaP `33.1161` edge `0.5168` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8205` n `91` status `ready` deltaP `33.1161` edge `0.5168` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.0381` n `91` status `ready` deltaP `25.021` edge `1.1423` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.0381` n `91` status `ready` deltaP `25.021` edge `1.1423` maxDD `-24.5429`
- `market_context_high->equity_24h` score `5.0978` n `201` status `ready` deltaP `22.7431` edge `0.2732` maxDD `0.0`
- `risk_on_high->index_24h` score `3.8835` n `91` status `ready` deltaP `38.5436` edge `0.0709` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.8835` n `91` status `ready` deltaP `38.5436` edge `0.0709` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.5042` n `91` status `ready` deltaP `22.7431` edge `0.1404` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.5042` n `91` status `ready` deltaP `22.7431` edge `0.1404` maxDD `0.0`
- `market_context_high->index_24h` score `3.0118` n `201` status `ready` deltaP `32.8851` edge `0.0711` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.0028` n `91` status `ready` deltaP `30.1444` edge `0.0586` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `3.0028` n `91` status `ready` deltaP `30.1444` edge `0.0586` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.8771` n `201` status `ready` deltaP `23.305` edge `0.0866` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.5214` n `91` status `ready` deltaP `6.0473` edge `0.1217` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.5214` n `91` status `ready` deltaP `6.0473` edge `0.1217` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
