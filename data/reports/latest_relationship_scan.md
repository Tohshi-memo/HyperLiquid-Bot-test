# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T03:52:33.875563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_4h` score `38.1064` n `149` status `ready` deltaP `-0.0061` edge `3.1989` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.9851` n `52` status `ready` deltaP `-7.2467` edge `1.0696` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.9851` n `52` status `ready` deltaP `-7.2467` edge `1.0696` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9848` n `52` status `ready` deltaP `50.0` edge `0.4154` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9848` n `52` status `ready` deltaP `50.0` edge `0.4154` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6857` n `149` status `ready` deltaP `43.2886` edge `0.4044` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `5.0509` n `35` status `ready` deltaP `25.2332` edge `0.3906` maxDD `-9.3661`
- `risk_on_high->commodity_4h` score `2.9957` n `52` status `ready` deltaP `33.3021` edge `0.0626` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9957` n `52` status `ready` deltaP `33.3021` edge `0.0626` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8954` n `149` status `ready` deltaP `29.8044` edge `0.0844` maxDD `-0.345`
- `news_risk_high->index_24h` score `2.7147` n `35` status `ready` deltaP `20.1339` edge `0.1096` maxDD `-0.075`
- `news_risk_high->unknown_4h` score `2.6294` n `68` status `ready` deltaP `-7.5861` edge `0.2979` maxDD `-0.9232`
- `risk_on_high->fx_24h` score `1.4677` n `52` status `ready` deltaP `23.0769` edge `-0.0273` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.4677` n `52` status `ready` deltaP `23.0769` edge `-0.0273` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.3329` n `149` status `ready` deltaP `20.302` edge `-0.0027` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2607` n `149` status `ready` deltaP `17.4085` edge `0.0267` maxDD `-0.3491`
- `news_risk_high->crypto_alt_4h` score `1.0296` n `68` status `ready` deltaP `13.6837` edge `0.2664` maxDD `-13.05`
- `risk_on_high->commodity_1h` score `0.6374` n `52` status `ready` deltaP `10.4906` edge `0.0184` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6374` n `52` status `ready` deltaP `10.4906` edge `0.0184` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.5865` n `68` status `ready` deltaP `9.7292` edge `0.0677` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
