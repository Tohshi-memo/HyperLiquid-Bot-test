# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T16:37:28.600860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8860`

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

- `news_risk_high->unknown_4h` score `402.4247` n `80` status `ready` deltaP `-22.9573` edge `33.7779` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `10.5635` n `80` status `ready` deltaP `30.5556` edge `0.8145` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `10.4833` n `80` status `ready` deltaP `22.3958` edge `0.9238` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.4321` n `52` status `ready` deltaP `50.5208` edge `0.4492` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4321` n `52` status `ready` deltaP `50.5208` edge `0.4492` maxDD `0.0`
- `market_context_high->commodity_24h` score `8.1329` n `149` status `ready` deltaP `43.8094` edge `0.4382` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `8.072` n `80` status `ready` deltaP `30.9722` edge `0.6436` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.6217` n `80` status `ready` deltaP `37.8125` edge `0.234` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7453` n `80` status `ready` deltaP `29.4792` edge `0.161` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9335` n `52` status `ready` deltaP `32.5399` edge `0.0625` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9335` n `52` status `ready` deltaP `32.5399` edge `0.0625` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8332` n `149` status `ready` deltaP `29.0422` edge `0.0843` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.1217` n `52` status `ready` deltaP `28.8061` edge `-0.011` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.1217` n `52` status `ready` deltaP `28.8061` edge `-0.011` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.9868` n `149` status `ready` deltaP `26.0312` edge `0.0136` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1397` n `149` status `ready` deltaP `16.2109` edge `0.0246` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5164` n `52` status `ready` deltaP `9.293` edge `0.0163` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5164` n `52` status `ready` deltaP `9.293` edge `0.0163` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.3772` n `80` status `ready` deltaP `8.9024` edge `0.0198` maxDD `-0.4841`
- `market_context_high->fx_4h` score `0.1795` n `149` status `ready` deltaP `9.886` edge `0.0047` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
