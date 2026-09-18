# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T18:52:29.975719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8296`

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

- `market_context_high->unknown_4h` score `39.0628` n `149` status `ready` deltaP `-0.9208` edge `3.2847` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `28.969` n `36` status `ready` deltaP `32.6389` edge `2.3344` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `17.4019` n `36` status `ready` deltaP `10.9375` edge `2.274` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `12.9415` n `52` status `ready` deltaP `-8.1614` edge `1.1554` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.9415` n `52` status `ready` deltaP `-8.1614` edge `1.1554` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6033` n `52` status `ready` deltaP `47.9167` edge `0.3975` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6033` n `52` status `ready` deltaP `47.9167` edge `0.3975` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.9008` n `87` status `ready` deltaP `26.216` edge `0.6004` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.3042` n `149` status `ready` deltaP `41.2053` edge `0.3865` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8273` n `52` status `ready` deltaP `32.9972` edge `0.0506` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8273` n `52` status `ready` deltaP `32.9972` edge `0.0506` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.727` n `149` status `ready` deltaP `29.4995` edge `0.0724` maxDD `-0.345`
- `news_risk_high->equity_24h` score `2.1784` n `36` status `ready` deltaP `14.0625` edge `0.2965` maxDD `-3.8776`
- `news_risk_high->crypto_major_4h` score `2.1334` n `87` status `ready` deltaP `17.3132` edge `0.3419` maxDD `-11.3716`
- `news_risk_high->equity_4h` score `1.8606` n `87` status `ready` deltaP `16.7612` edge `0.1333` maxDD `-4.1995`
- `market_context_high->commodity_1h` score `1.1469` n `149` status `ready` deltaP `16.5103` edge `0.0232` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.0022` n `87` status `ready` deltaP `12.7159` edge `0.0393` maxDD `-0.9112`
- `news_risk_high->crypto_alt_1h` score `0.8323` n `87` status `ready` deltaP `10.7268` edge `0.1244` maxDD `-4.4695`
- `news_risk_high->fx_4h` score `0.7374` n `87` status `ready` deltaP `10.2643` edge `0.0291` maxDD `-0.2198`
- `news_risk_high->crypto_major_1h` score `0.6771` n `87` status `ready` deltaP `13.1272` edge `0.0869` maxDD `-4.3419`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
