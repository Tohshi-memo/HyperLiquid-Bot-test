# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T11:37:26.166771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `65.8782` n `47` status `ready` deltaP `10.2657` edge `5.4285` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.9868` n `46` status `ready` deltaP `30.2008` edge `3.3965` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `28.6947` n `46` status `ready` deltaP `25.1736` edge `2.2234` maxDD `0.0`
- `market_context_high->equity_24h` score `24.8474` n `46` status `ready` deltaP `27.5966` edge `1.8967` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.2456` n `103` status `ready` deltaP `2.5098` edge `1.658` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.1643` n `46` status `ready` deltaP `36.6244` edge `0.4449` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `6.4326` n `103` status `ready` deltaP `-0.0691` edge `1.2378` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5066` n `46` status `ready` deltaP `30.6009` edge `0.1116` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.0432` n `47` status `ready` deltaP `34.6361` edge `0.0381` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5887` n `47` status `ready` deltaP `17.4494` edge `0.1412` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4909` n `114` status `ready` deltaP `13.3969` edge `0.1673` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.1069` n `114` status `ready` deltaP `15.343` edge `0.1168` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6973` n `114` status `ready` deltaP `24.861` edge `0.0393` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.3634` n `103` status `ready` deltaP `17.6712` edge `0.1137` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.3043` n `103` status `ready` deltaP `30.1847` edge `0.1291` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.999` n `47` status `ready` deltaP `15.0592` edge `0.0107` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9461` n `103` status `ready` deltaP `22.4751` edge `0.1163` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.8947` n `47` status `ready` deltaP `10.8676` edge `0.0424` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.7151` n `114` status `ready` deltaP `15.5741` edge `0.0151` maxDD `-0.7468`
- `news_risk_high->crypto_major_4h` score `0.6824` n `114` status `ready` deltaP `12.6337` edge `0.1858` maxDD `-13.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
